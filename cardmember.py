import numpy as np
import pandas as pd


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


class CardMember:
    """ Represents a card member profile along with targeting information """

    def __init__(self, username):
        self.transactions = None
        self.processed = None
        self.username = username

    def process_transactions(self):

        def __get_stats(group):
            return {
                'tot_spend': group['Amount'].sum(),
                'avg_spend': group['Amount'].mean(),
                'txn_count': group['Amount'].count()
            }

        self.transactions = pd.read_csv('transactions/{}.csv'.format(self.username))

        processed = (self.transactions
            .groupby(['Category', 'SubCategory'])
            .apply(__get_stats)
            .apply(pd.Series)
            .reset_index())

        processed['pct_spend'] = processed['tot_spend'] / processed['tot_spend'].sum()

        self.processed = list(processed.to_dict('index').values())

        return self.processed

    def get_transactions(self):
        if self.transactions is None:
            self.process_transactions()

        return self.transactions

    def get_tags(self):
        if self.processed is None:
            self.process_transactions()

        return self.processed
