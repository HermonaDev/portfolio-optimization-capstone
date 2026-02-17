import logging
from src.config import PortfolioConfig
from src.data_ingestion import DataFetcher
from src.models import LSTMForecaster
from src.optimizer import PortfolioOptimizer
from src.backtest import PortfolioBacktester
from src.explainability import ModelExplainer
import joblib
import os
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    config = PortfolioConfig()
    os.makedirs("models", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # 1. FETCH
    prices = DataFetcher(config).fetch_data()
    if prices is None: return
    returns = prices.pct_change().dropna()

    # 2. OPTIMIZE
    weights, perf = PortfolioOptimizer(prices, config).optimize_sharpe()
    joblib.dump(weights, "models/optimal_weights.joblib")
    
    # 3. BACKTEST
    strat_cum, bench_cum, metrics = PortfolioBacktester(returns, weights).run()
    joblib.dump(metrics, "models/backtest_metrics.joblib")

    # 4. EXPLAIN (Using a small window of TSLA for SHAP)
    forecaster = LSTMForecaster(window_size=config.window_size)
    # Train dummy/sample to initialize model for SHAP
    model = forecaster.train(prices['TSLA'], epochs=1) 
    
    # Generate background data for SHAP
    scaled_data = forecaster.scaler.transform(prices['TSLA'].values.reshape(-1, 1))
    X, _ = forecaster.create_sequences(scaled_data)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    explainer = ModelExplainer(model, X)
    explainer.explain(X[-5:]) # Explain the last 5 days

    logger.info("Production Pipeline successfully completed.")

if __name__ == "__main__":
    main()
