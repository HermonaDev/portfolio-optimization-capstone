import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# Path Hack: Ensure Streamlit sees the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_ingestion import DataFetcher
from src.optimizer import PortfolioOptimizer
from src.config import PortfolioConfig

st.set_page_config(page_title="GMF Strategic Portfolio Intelligence", layout="wide")

st.title("💼 GMF Strategic Portfolio Intelligence")
st.markdown("### Production-Grade Risk Management & Asset Allocation")

# Sidebar Configuration
st.sidebar.header("Asset Selection")
tickers = st.sidebar.multiselect("Select Assets", ["TSLA", "BND", "SPY", "AAPL", "MSFT"], default=["TSLA", "BND", "SPY"])
risk_free = st.sidebar.slider("Risk-Free Rate (%)", 0.0, 5.0, 2.0) / 100

if st.sidebar.button("Optimize Portfolio"):
    with st.spinner("Fetching market data and running MPT..."):
        config = PortfolioConfig(tickers=tickers, risk_free_rate=risk_free)
        fetcher = DataFetcher(config)
        prices = fetcher.fetch_data()
        
        if prices is not None:
            optimizer = PortfolioOptimizer(prices, config)
            weights, perf = optimizer.optimize_sharpe()
            
            # KPI Row
            col1, col2, col3 = st.columns(3)
            col1.metric("Expected Annual Return", f"{perf[0]*100:.2f}%")
            col2.metric("Annual Volatility", f"{perf[1]*100:.2f}%")
            col3.metric("Sharpe Ratio", f"{perf[2]:.2f}")
            
            # Allocation Chart
            st.markdown("#### Optimal Asset Allocation")
            df_weights = pd.DataFrame(list(weights.items()), columns=['Asset', 'Weight'])
            st.bar_chart(df_weights.set_index('Asset'))
            
            # Weights Table
            st.dataframe(df_weights.style.format({'Weight': '{:.2%}'}))
            
            st.success("Analysis Complete. Reliability Verified via MPT Solver.")
        else:
            st.error("Data ingestion failed. Check your internet connection.")
