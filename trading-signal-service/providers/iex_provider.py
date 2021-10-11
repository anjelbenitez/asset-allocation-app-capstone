import requests
import pandas as pd
from providers.historical_provider import HistoricalDataProvider


class IexDataProvider(HistoricalDataProvider):
    def __init__(self, token):
      super().__init__()
      self.token = token

    def request_ticker_data(self, ticker):
        api = f'https://sandbox.iexapis.com/stable/stock/{ticker}/chart/1y?token={self.token}'
        data = requests.get(api).json()
        data_frame = pd.DataFrame(data)
        return data_frame.set_index('date')

    def request_real_ticker_data(self, ticker):
        api = f'https://cloud.iexapis.com/stable/stock/{ticker}/chart/1y?token={self.token}'
        data = requests.get(api).json()
        data_frame = pd.DataFrame(data)
        return data_frame.set_index('date')
