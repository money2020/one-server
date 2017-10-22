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


    def get_preapproved(self):
        body = {
          "firstName":"Eugene",
          "middleName":"",
          "lastName":"Beaupre",
          "nameSuffix":"Jr.",
          "address":{
            "addressLine1":"5151 N Cedar Ave",
            "addressLine2":"",
            "addressLine3":"",
            "addressLine4":"",
            "city":"Fresno",
            "stateCode":"CA",
            "postalCode":"93710",
            "addressType":"Home"
          },
          "taxId":"666666666",
          "dateOfBirth":"1970-06-29",
          "emailAddress":"ray@wyliehubbard.com",
          "annualIncome":75000,
          "selfAssessedCreditRating":"Average",
          "bankAccountSummary":"CheckingOnly",
          "requestedBenefit":"LowInterest"
        }

        new_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwicGNrIjoxLCJhbGciOiJkaXIiLCJ0diI6Miwia2lkIjoiYTdxIn0..Jn908J-yYgcKMNJnBlhrJg.J15niJBubgAPK5cSeKL6g78C1yBxirQW9HKZ0k1usVdsFOWY392OlR_qUazosk6EiCW2ge-4ahSUo5x-qooNPNz7bb2hWAXmj4MY81oF3oLMHi6JcAPzjYsVHlZQsAYEKjyUCFR7h8h4WHNSukDgidJ6fqumOHflRWCex_eODLYGlJl-B5ksgMByssOZCOFNX-l8ylDscykKpj79steWwPI_mscsEszAbihjXIliQNw7ysEp0Xyxypcc3YCshYIbVpWNcvA1gvmXPeeC4BB0EhwMbtkPdKHAPohnH-Y0y2xJfqQJ64-sG_k_vIIryQTrzQS_cBDldnvbHWWjR1DdJ0B4bFlQz4ciiIt0j7TH6jJPdWPUzII5mKweoNNrSxtkiR0U5ZHPsOuh9dMB7dlaYJQEDm9f4bm8RGoVyLN4NHBhAGL2LAkwCQ7osIVxEvP5nfeP9qZsZTCzQGzvT-a0V8MycVPxAbP1Nem9BV4oY9SbtVaTCwZv948gYOnNEAGW.ysGRHpe2a1rWDtGh30nRdw'

        json = requests.post('https://api.devexhacks.com/credit-offers/prequalifications', json=body, headers={
                    'Authorization': 'Bearer ' + new_token
                }).json()

        return json


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
