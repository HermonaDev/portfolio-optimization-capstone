import yfinance as yf
import pandas as pd
import logging
from typing import Optional
from src.config import PortfolioConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    """Production-grade data fetcher with error handling."""
    def __init__(self, config: PortfolioConfig):
        self.config = config

    def fetch_data(self) -> Optional[pd.DataFrame]:
        try:
            logger.info(f"Fetching data for {self.config.tickers}")
            data = yf.download(
                self.config.tickers, 
                start=self.config.start_date, 
                end=self.config.end_date
            )['Adj Close']
            if data.empty:
                raise ValueError("No data returned from yfinance")
            return data.dropna()
        except Exception as e:
            logger.error(f"Ingestion failed: {e}")
            return None
