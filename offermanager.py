import json
import os
import redis

class OfferManager:

    def __init__(self):
        self.r = redis.from_url(os.environ.get('REDIS_URL'))


    def get_offers(self):
        return json.loads(self.r.get('offers') or '[]')


    def create_offers(self):

        offers = [
            {
                'id': 1,
                'title': 'Happy Birthday, Lucas!',
                'icon': '&#xf1fd;',
                'text': '$20 off Italianos when you pay with points',
                'category': 'Food & Dining',
                'subcategory': 'Restaurant'
            },
            {
                'id': 2,
                'title': 'Drink More Coffee',
                'icon': '&#xf0f4;',
                'text': 'Free Pumpkin Spice Latte at Starbucks',
                'category': 'Food & Dining',
                'subcategory': 'Coffee Shop'
            }
        ]

        return self.r.set('offers', json.dumps(offers))


    def remove_offers(self):
        return self.r.delete('offers')