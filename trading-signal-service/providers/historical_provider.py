from abc import abstractmethod


class HistoricalDataProvider():
    @abstractmethod
    def request_year_ticker_chart_data(self, ticker):
        """Request ticker data over a period"""
        pass
