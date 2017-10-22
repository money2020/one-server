import json
import os
import redis

from utils import cat_to_color

class OfferManager:

    SCAFFOLDING_OFFERS = [
        {
            'id': 1,
            'title': 'Happy Birthday, Lucas! ***EXCLUSIVE***',
            'icon': '&#xf1fd;',
            'text': '$20 off Italianos when you pay with points',
            'category': 'Food & Dining',
            'subcategory': 'Restaurant',
            'color': cat_to_color('Food & Dining')
        },
        {
            'id': 2,
            'title': 'Book Your Holiday Escape Early.',
            'icon': '&#xf236;',
            'text': '25% bonus points at you Hilton stay. Exp 11/25/2017.',
            'category': 'Travel',
            'subcategory': 'Hotels',
            'color': cat_to_color('Shopping')
        },
        {
            'id': 3,
            'title': 'Refill your prescription.',
            'icon': '&#xf004;',
            'text': '+200 pts from CVS. Exp 10/31/2017.',
            'category': 'Health & Fitness',
            'subcategory': 'Health',
            'color': cat_to_color('Food & Dining')
        },
        {
            'id': 4,
            'title': 'Fall Coffee is Here.',
            'icon': '&#xf0f4;',
            'text': 'FREE Pumpkin Spice Latte at Starbucks. Exp 11/11/2017.',
            'category': 'Food & Dining',
            'subcategory': 'Coffee Shop',
            'color': cat_to_color('Shopping')
        },
        {
            'id': 5,
            'title': 'Gear up your camera for Christmas!',
            'icon': '&#xf030;',
            'text': '+1,000 pts and free shipping from B&H Photo. Exp 11/25/2017',
            'category': 'Shopping',
            'subcategory': 'Electronics',
            'color': cat_to_color('Food & Dining')
        },
        {
            'id': 6,
            'title': 'Turkey Time?',
            'icon': '&#xf099;',
            'text': '+500 points when you redeem at Wholefoods. Exp 11/26/2017.',
            'category': 'Food & Dining',
            'subcategory': 'Groceries',
            'color': cat_to_color('Shopping')
        },
        {
            'id': 7,
            'title': 'Let\'s Get Moving',
            'icon': '&#xf1bb;',
            'text': 'Stream Spotify playlist for your Yosemite hike.',
            'category': 'Travel',
            'subcategory': 'Activities',
            'color': cat_to_color('Food & Dining')
        },
    ]


    def __init__(self):
        self.r = redis.from_url(os.environ.get('REDIS_URL'))


    def get_offers(self):
        return json.loads(self.r.get('offers') or '[]')


    def add_offer(self, offer):

        # Validate Offer
        for k in ['title', 'icon', 'text', 'category', 'subcategory']:
            if offer[k] == '':
                return False

        offers = self.get_offers()

        offer['color'] = cat_to_color(offer['category'])
        offer['id'] = max([o['id'] for o in offers]) + 1

        offers.append(offer)

        return self.create_offers(offers)


    def create_offers(self, offers=SCAFFOLDING_OFFERS):
        return self.r.set('offers', json.dumps(offers))


    def remove_offers(self):
        return self.r.delete('offers')