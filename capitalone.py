import numpy as np
import pandas as pd

import requests


class CapitalOne:

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def get_points(self):
        http = requests.get('https://api.devexhacks.com/rewards/accounts/', headers={
                'Authorization': 'Bearer ' + self.bearer_token
            })

        json = http.json()
        point_accounts = [
            account['rewardsAccountReferenceId']
            for account in json.get('rewardsAccounts', {})
            if account['rewardsCurrency'] == 'Points'
        ]

        json = requests.get('https://api.devexhacks.com/rewards/accounts/' + point_accounts[0], headers={
                    'Authorization': 'Bearer ' + self.bearer_token
                }).json()

        return json # {'rewardsBalance': json['rewardsBalance']}

    def get_spend(self, transactions_csv):
        txns = pd.read_csv(transactions_csv)
        processed = (txns
            .groupby(['Category', 'SubCategory'])
            .apply(self._get_stats)
            .apply(pd.Series)
            .reset_index())

        processed['pct_spend'] = processed['tot_spend'] / processed['tot_spend'].sum()
        return list(processed.to_dict('index').values())

    def _get_stats(self, group):
        return {
            'tot_spend': group['Amount'].sum(),
            'avg_spend': group['Amount'].mean(),
            'txn_count': group['Amount'].count()
        }
