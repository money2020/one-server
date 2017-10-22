import os
import redis

class OfferManager:

    def __init__(self):
        self.r = redis.from_url(os.environ.get('REDIS_URL'))