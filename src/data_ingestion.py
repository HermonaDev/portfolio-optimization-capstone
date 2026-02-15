import yfinance as yf
import pandas as pd
import logging
from typing import Optional
from src.config import PortfolioConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    """Production-grade data fetcher with fallback logic."""
    def __init__(self, config: PortfolioConfig):
        self.config = config

    def fetch_data(self) -> Optional[pd.DataFrame]:
        try:
            logger.info(f"Fetching data for {self.config.tickers}")
            # Download data
            data = yf.download(
                self.config.tickers, 
                start=self.config.start_date, 
                end=self.config.end_date,
                progress=False
            )
            
            # Robust column selection
            if 'Adj Close' in data.columns:
                processed_data = data['Adj Close']
            elif 'Close' in data.columns:
                logger.warning("'Adj Close' missing, using 'Close' columns.")
                processed_data = data['Close']
            else:
                raise ValueError("Required price columns not found in yfinance response")

            if processed_data.empty:
                raise ValueError("No data returned from yfinance")
                
            return processed_data.dropna()
        except Exception as e:
            logger.error(f"Ingestion failed: {e}")
            return None
