import json
import os
import redis

from config import ICONS
from utils import cat_to_color

class OfferManager:

    def __init__(self):
        self.r = redis.from_url(os.environ.get('REDIS_URL'))


    def set_offers(self, offers):
        return self.r.set('offers', json.dumps(offers))


    def get_offers(self):
        return json.loads(self.r.get('offers') or '[]')


    def remove_offer(self, id):
        offers = self.get_offers()
        offers = [offer for offer in offers if offer['id'] != id]
        return self.set_offers(offers)


    def add_offer(self, offer):

        # Validate Offer
        for k in ['title', 'icon', 'text', 'category', 'expiration', 'subcategory']:
            if offer[k] == '':
                return False

        offers = self.get_offers()

        offer['color'] = cat_to_color(offer['category'])
        offer['id'] = max([o['id'] for o in offers]) + 1

        offers.append(offer)

        return self.set_offers(offers)

    def inject_card_offer(self, card_offer):
        return [{
            'id': 2.5, # lol
            'title': card_offer['products'][0]['productName'],
            'icon': ICONS['fa-credit-card'],
            'text': card_offer['products'][0]['images'][0]['alternateText'],
            'expiration': '10/25/2017',
            'category': 'Unknown',
            'subcategory': 'Unknown',
            'color': cat_to_color('Unknown'),
            'target': 'lucas',
            'co_url': card_offer['products'][0]['applicationUrl'],
            'isCardOffer': True
        }]


    def remove_offers(self):
        return self.r.delete('offers')
