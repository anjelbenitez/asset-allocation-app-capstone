# asset-allocation-app-capstone
Capstone Project

## Overview:

The high-level requirement of this project is to develop a stock market recommendation
application that will provide buy and sell signals for a set of 3x ETFs, and one or two
other high-risk assets.

In addition to developing and testing the end-to-end system, the project involves testing
the performance of the underlying multi resolution algorithm and reporting results using
the backtesting capabilities of QuantConnect.

Back testing and optimization efforts consisted of testing varying lengths of SMAs both
individually and combined over different time periods, experimenting with different
resolutions, and writing code for other widely used trading strategies in QuantConnect
for comparison.

## Use case:

1.	The user selects an asset (TQQQ, UPRO, TNA to start)
2.	The system acquires end-of-day data for the selected asset (OHLC)
3.	Using the data, an algorithm produces buy/sell signals.
4.	The buy/sell signals are transformed into an allocation recommendation. (%)
5.	The recommendation is presented to the user.

### Note:
Files related to trading algorithm and analysis have been removed from this repository for privacy.

## TQQQ Backtest Results using QuantConnect:
![image](https://user-images.githubusercontent.com/55768082/136721188-9e04bebd-7601-4404-a34c-f7a3041ed744.png)

## TQQQ Equity Overview:
![image](https://user-images.githubusercontent.com/55768082/136721212-72462961-cc06-4230-be02-ca70899940e2.png)

## UI Sample:
![image](https://user-images.githubusercontent.com/55768082/136721246-513fb6d0-55ca-4940-9918-3a17552bb068.png)
