from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

from algos.sma_crossover import MultiResolutionAlgorithm
from providers.iex_provider import IexDataProvider

import os

dev_token = os.getenv("IEX_CLOUD_API_TOKEN_DEV")
prod_token = os.getenv("IEX_CLOUD_API_TOKEN_PROD")

app = Flask(__name__)
CORS(app)


dev_data_provider = IexDataProvider(dev_token)
data_provider = IexDataProvider(prod_token)


@app.route('/')
def home():
    return 'Hello there!', 200


@app.route('/dev/signals/<ticker>', methods=['GET'])
def get_dev_data(ticker):
    algorithm = MultiResolutionAlgorithm()
    algorithm.set_ticker(ticker)
    historical_data = dev_data_provider.request_ticker_data(ticker)
    return algorithm.create_details(historical_data)


@app.route('/signals/<ticker>', methods=['GET'])
def get_data(ticker):
    algorithm = MultiResolutionAlgorithm()
    algorithm.set_ticker(ticker)
    historical_data = data_provider.request_real_ticker_data(ticker)
    return algorithm.create_details(historical_data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
