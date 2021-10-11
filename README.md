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
Algorithms and analysis have been removed from this repository for privacy.

## UI Sample:
![image](https://user-images.githubusercontent.com/55768082/136721093-2a09f76a-41ea-45e9-ab2a-859e1e3adb6e.png)
