import pytest
import pandas as pd
import numpy as np
from src.optimizer import PortfolioOptimizer
from src.config import PortfolioConfig
from src.models import LSTMForecaster

def test_optimization_weights_sum():
    """Test 1: Optimization logic (Weights sum to 1.0)"""
    dates = pd.date_range(start="2020-01-01", periods=100)
    data = pd.DataFrame(np.random.rand(100, 3), columns=["TSLA", "BND", "SPY"], index=dates)
    config = PortfolioConfig()
    optimizer = PortfolioOptimizer(data, config)
    weights, perf = optimizer.optimize_sharpe()
    assert sum(weights.values()) == pytest.approx(1.0, abs=1e-4)

def test_config_tickers():
    """Test 2: Configuration (Correct default tickers)"""
    config = PortfolioConfig()
    assert "TSLA" in config.tickers
    assert len(config.tickers) == 3

def test_lstm_sequence_generation():
    """Test 3: LSTM Data Prep (Correct sequence shape)"""
    forecaster = LSTMForecaster(window_size=10)
    data = np.random.rand(50, 1)
    X, y = forecaster.create_sequences(data)
    # 50 total - 10 window = 40 sequences
    assert X.shape == (40, 10)
    assert y.shape == (40,)

def test_data_structure():
    """Test 4: Data Layer (DataFrame constraints)"""
    dates = pd.date_range(start="2020-01-01", periods=10)
    data = pd.DataFrame(np.random.rand(10, 3), columns=["TSLA", "BND", "SPY"], index=dates)
    assert not data.empty
    assert list(data.columns) == ["TSLA", "BND", "SPY"]

def test_risk_free_rate_config():
    """Test 5: Config (Risk-free rate type)"""
    config = PortfolioConfig()
    assert isinstance(config.risk_free_rate, float)
    assert config.risk_free_rate >= 0
