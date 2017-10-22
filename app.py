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


@app.route('/api/one/spend', methods=['GET'])
def one_transactions():
    """ Returns top spending categories """
    return jsonify(c1.get_spend('transactions/user1.csv'))


@app.route('/api/one/offers', methods=['GET'])
def one_offers():
    """ Returns personalized offers """
    return jsonify(om.get_offers())


@app.route('/api/one/offers/create', methods=['GET'])
def one_offers_create():
    """ Scaffolding: Create personalized offers """
    return jsonify(om.create_offers())


@app.route('/api/one/offers/remove', methods=['GET'])
def one_offers_remove():
    """ Scaffolding: Clear all personalized offers """
    return jsonify(om.remove_offers())


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
