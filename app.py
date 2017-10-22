import config
import json
import os
import requests

from capitalone import CapitalOne
from cardmember import CardMember
from offermanager import OfferManager

from flask import Flask, jsonify, request, render_template
from flask.ext.cors import CORS



c1 = CapitalOne(config.token)
om = OfferManager()
cardmembers = {}
def get_cardmember(username='nick'):
    if username not in cardmembers:
        cardmembers[username] = CardMember(username)

    return cardmembers[username]

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

    cm = get_cardmember(request.args.get('user', 'nick'))

    return jsonify(cm.process_transactions())


@app.route('/api/one/offers', methods=['GET'])
def one_offers():
    """ Returns personalized offers """

    # Step 1: Get the CardMember
    cm = get_cardmember(request.args.get('user', 'nick'))

    # Step 2: Get the Offers
    all_offers = om.get_offers() + om.inject_card_offer(c1.get_preapproved())

    # Step 3: Personalize the Offers
    targetted_offers = om.filter_offers(cm, all_offers)

    # Step 4: Profit!
    return jsonify(targetted_offers)


@app.route('/api/one/offers/create', methods=['GET', 'POST'])
def one_offers_create():
    if request.method == 'GET':
        return render_template('add_ad.html')
    else:
        offer = {}

        if request.form.get('json'):
            json_offer = json.loads(request.form.get('json'))

            for k in ['title', 'icon', 'text', 'category', 'expiration', 'subcategory']:
                if k in json_offer['copy']:
                    offer[k] = json_offer['copy'][k]
                else:
                    return k + ' is empty, please fill it out'

        else:
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
