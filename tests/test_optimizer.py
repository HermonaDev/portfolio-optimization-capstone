import pytest
import pd
import numpy as np
from src.optimizer import PortfolioOptimizer
from src.config import PortfolioConfig

def test_optimization_logic():
    dates = pd.date_range(start="2020-01-01", periods=100)
    data = pd.DataFrame(np.random.rand(100, 3), columns=["TSLA", "BND", "SPY"], index=dates)
    config = PortfolioConfig()
    
    optimizer = PortfolioOptimizer(data, config)
    weights, perf = optimizer.optimize_sharpe()
    
    assert isinstance(weights, dict)
    # Increased tolerance to 1e-4 to account for solver rounding
    assert sum(weights.values()) == pytest.approx(1.0, abs=1e-4)
