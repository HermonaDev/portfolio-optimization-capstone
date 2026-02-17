import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PortfolioBacktester:
    """Computes risk metrics to demonstrate business impact."""
    
    def __init__(self, daily_returns: pd.DataFrame, weights: dict):
        self.returns = daily_returns
        self.weights = np.array(list(weights.values()))
        self.tickers = list(weights.keys())

    def run(self):
        # 1. Strategy Returns
        strat_daily = self.returns[self.tickers].dot(self.weights)
        strat_cum = (1 + strat_daily).cumprod()

        # 2. Benchmark Returns (Equal Weight or 60/40)
        bench_daily = self.returns.mean(axis=1) # Simple benchmark
        bench_cum = (1 + bench_daily).cumprod()

        # 3. Calculate Drawdown
        strat_dd = (strat_cum / strat_cum.expanding().max()) - 1
        
        metrics = {
            "Total Return": strat_cum.iloc[-1] - 1,
            "Max Drawdown": strat_dd.min(),
            "Daily Volatility": strat_daily.std()
        }
        
        return strat_cum, bench_cum, metrics
