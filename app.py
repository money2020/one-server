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
    """ This endpoint takes in an Authorization token and returns the amount of points available in the account. """
    return jsonify(c1.get_points())


@app.route('/api/one/spend', methods=['GET'])
def one_transactions():
    return jsonify(c1.get_spend('transactions/user1.csv'))

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
