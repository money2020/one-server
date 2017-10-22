import config
import os
import requests

from capitalone import CapitalOne
from offermanager import OfferManager

from flask import Flask, jsonify, request, render_template
from flask.ext.cors import CORS


c1 = CapitalOne(config.token)
om = OfferManager()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return 'Hello, One!'


@app.route('/api/one/rewards', methods=['GET'])
def one_rewards():
    """ Returns the amount of points available in the account. """
    return jsonify(c1.get_points())


@app.route('/api/one/preapproved', methods=['GET'])
def one_preapproved():
    """ Returns preapproved credit offers """
    return jsonify(c1.get_preapproved())


@app.route('/api/one/spend', methods=['GET'])
def one_transactions():
    """ Returns top spending categories """
    return jsonify(c1.get_spend('transactions/user1.csv'))


@app.route('/api/one/offers', methods=['GET'])
def one_offers():
    """ Returns personalized offers """

    all_offers = om.get_offers() + om.inject_card_offer(c1.get_preapproved())

    return jsonify(all_offers)


@app.route('/api/one/offers/create', methods=['GET', 'POST'])
def one_offers_create():
    if request.method == 'GET':
        return render_template('add_ad.html')
    else:
        offer = {}
        for k in ['title', 'icon', 'text', 'category', 'expiration', 'subcategory']:
            if request.form.get(k):
                offer[k] = request.form.get(k)
            else:
                return k + ' is empty, please fill it out'

        return jsonify(om.add_offer(offer))


@app.route('/api/one/offers/bootstrap', methods=['GET'])
def one_offers_bootstrap():
    """ Scaffolding: Create personalized offers """
    return jsonify(om.set_offers(config.SCAFFOLDING_OFFERS))


@app.route('/api/one/offers/clear', methods=['GET'])
def one_offers_clear():
    """ Scaffolding: Clear all personalized offers """
    return jsonify(om.remove_offers())


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
