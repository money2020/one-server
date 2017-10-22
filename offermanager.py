import json
import os
import redis

from config import ICONS
from utils import cat_to_color


CURRENT_LOCATION = 'Las Vegas'
MERCHANT_NAME = '*VENETIAN*'

AVAILABLE_USER_TAGS = [
    'new_customers',
    'repeat_traffic',
    'recent_activity',
    'weather',
    'location',
    'like_for_like',
    'personal_preference',
    'social_data'
]


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

    def filter_offers(self, cardmember, offerlist):

        # Credit Card Offer
        initial_offer_list = [o for o in offerlist if o.get('isCardOffer', False) is True]


        
        for o in offerlist:

            # skip if exists
            if o['id'] in (s['id'] for s in initial_offer_list):
                continue

            target = o.get('target', None)
            try:
                smart_target = target.split(',')
            except:
                smart_target = []

            # No Targetting or Specific to user
            if target in [cardmember.username, None]:
                initial_offer_list.append(o)

            for tgt in smart_target:
                # Target based on location
                if tgt == 'location':
                    if cardmember.get_currenct_city() == CURRENT_LOCATION and o['id'] not in (s['id'] for s in initial_offer_list):
                        print("adding based on location!")
                        initial_offer_list.append(o)

                if tgt == 'new_customers':
                    if not cardmember.get_is_repeat_traffic(MERCHANT_NAME) and o['id'] not in (s['id'] for s in initial_offer_list):
                        print("adding based on new_customers")
                        initial_offer_list.append(o)

        return initial_offer_list


    def remove_offers(self):
        return self.r.delete('offers')
