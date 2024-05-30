import backtrader as bt

class MeanReversionStrategy(bt.Strategy):
    params = (('period', 20), ('devfactor', 1.5),)

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.sma = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=self.params.period)
        self.stddev = bt.indicators.StandardDeviation(
            self.datas[0], period=self.params.period)
        self.upper_band = self.sma + self.params.devfactor * self.stddev
        self.lower_band = self.sma - self.params.devfactor * self.stddev

    def next(self):
        if self.order:
            return

        if self.dataclose[0] < self.lower_band[0]:
            self.order = self.buy()

        elif self.dataclose[0] > self.upper_band[0]:
            self.order = self.sell()

# Load historical data
data = bt.feeds.YahooFinanceData(
    dataname='AAPL', fromdate=datetime(2020, 1, 1),
    todate=datetime(2021, 1, 1))

# Initialize Cerebro engine
cerebro = bt.Cerebro()

# Add strategy
cerebro.addstrategy(MeanReversionStrategy)

# Add data feed
cerebro.adddata(data)

# Set initial cash
cerebro.broker.setcash(100000.0)

# Run backtest
cerebro.run()

# Plot results
cerebro.plot()
