import json
import os
import redis

from utils import cat_to_color

class OfferManager:

    SCAFFOLDING_OFFERS = [
        # {
        #     'id': 1,
        #     'title': 'Happy Birthday, Lucas! ***EXCLUSIVE***',
        #     'icon': '&#xf1fd;',
        #     'text': '$20 off Italianos, pay with pts',
        #     'category': 'Food & Dining',
        #     'subcategory': 'Restaurant',
        #     'color': cat_to_color('Food & Dining'),
        #     'target': 'lucas'
        # },

        # Lucas Offers
        {
            'id': 2,
            'title': 'Early Holiday Escape.',
            'icon': '&#xf236;',
            'text': '25% bonus pts at Hilton.',
            'expiration': '11/25/2017',
            'category': 'Travel',
            'subcategory': 'Hotels',
            'color': cat_to_color('Travel'),
            'target': 'lucas'
        },
        {
            'id': 3,
            'title': 'Refill your prescription.',
            'icon': '&#xf004;',
            'text': '+200 pts at CVS.',
            'expiration': '10/31/2017',
            'category': 'Health & Fitness',
            'subcategory': 'Health',
            'color': cat_to_color('Health & Fitness'),
            'target': 'lucas'
        },
        {
            'id': 4,
            'title': 'Fall Coffee is Here.',
            'icon': '&#xf0f4;',
            'text': 'FREE Pumpkin Spice at Starbucks.',
            'expiration': '11/11/2017',
            'category': 'Food & Dining',
            'subcategory': 'Coffee Shop',
            'color': cat_to_color('Food & Dining'),
            'target': 'lucas'
        },
        {
            'id': 5,
            'title': 'Gear up your camera for Christmas!',
            'icon': '&#xf030;',
            'text': '+1,000 pts, free shipping from B&H Photo.',
            'expiration': '12/1/2017',
            'category': 'Shopping',
            'subcategory': 'Electronics',
            'color': cat_to_color('Shopping'),
            'target': 'lucas'
        },

        # Tatiana Offers
        {
            'id': 6,
            'title': 'Beach time!',
            'icon': '&#xf236;',
            'text': '25% bonus pts at Cubana.',
            'expiration': '11/25/2017',
            'category': 'Travel',
            'subcategory': 'Hotels',
            'color': cat_to_color('Travel'),
            'target': 'tatiana'
        },
        {
            'id': 7,
            'title': 'Turkey Time?',
            'icon': '&#xf099;',
            'text': '+500 pts at Wholefoods.',
            'expiration': '11/30/2017',
            'category': 'Shopping',
            'subcategory': 'Groceries',
            'color': cat_to_color('Shopping'),
            'target': 'tatiana'
        },
        {
            'id': 8,
            'title': 'Let\'s Get Moving',
            'icon': '&#xf1bb;',
            'text': 'Stream Spotify hiking playlist.',
            'expiration': 'Fun never expires.',
            'category': 'Travel',
            'subcategory': 'Activities',
            'color': cat_to_color('Travel'),
            'target': 'tatiana'
        },
    ]


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

        return self.create_offers(offers)


    def create_offers(self, offers=SCAFFOLDING_OFFERS):
        """ Deprecated """
        return self.set_offers(offers)


    def remove_offers(self):
        return self.r.delete('offers')
