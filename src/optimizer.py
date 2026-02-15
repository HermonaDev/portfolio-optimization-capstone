import pandas as pd
import numpy as np
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns
from src.config import PortfolioConfig

class PortfolioOptimizer:
    def __init__(self, prices: pd.DataFrame, config: PortfolioConfig):
        self.prices = prices
        self.config = config
        self.returns = prices.pct_change().dropna()

    def optimize_sharpe(self):
        """Finds weights that maximize Sharpe Ratio."""
        mu = expected_returns.mean_historical_return(self.prices)
        S = risk_models.sample_cov(self.prices)
        
        ef = EfficientFrontier(mu, S)
        weights = ef.max_sharpe(risk_free_rate=self.config.risk_free_rate)
        cleaned_weights = ef.clean_weights()
        performance = ef.portfolio_performance(verbose=False)
        
        return cleaned_weights, performance
