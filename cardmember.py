import fnmatch

import numpy as np
import pandas as pd


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
        """ TOOD: Not yet implemented """
        if self.processed is None:
            self.process_transactions()

        return self.processed

    #### Building a custom profile for the user ####
    def get_currenct_city(self):
        return self.transactions.iloc[0]['Location']

    def get_username(self):
        return self.username

    def get_is_repeat_traffic(self, glob):
        return len(fnmatch.filter(self.transactions['Description'], glob)) > 0
