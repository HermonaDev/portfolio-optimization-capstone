# GMF Institutional Portfolio Optimization Platform

![CI Status](https://github.com/HermonaDev/portfolio-optimization-capstone/actions/workflows/ci.yml/badge.svg)
![Finance](https://img.shields.io/badge/Sector-Quantitative_Finance-gold)
![Status](https://img.shields.io/badge/Version-Production--Grade-green)

## 📌 Business Objective
Institutional investors face extreme risk during market regime shifts. This platform provides a **Zero-Trust Financial Engineering** framework that replaces static asset allocation with **dynamic, AI-backed rebalancing**.

## 🚀 Engineering Excellence (Portfolio Enhancements)
- **Modularity:** Fully refactored into a Python package with strict type hinting and dataclasses.
- **Reliability:** CI/CD integration with automated pytest suite (5+ tests) verifying MPT math and LSTM data flow.
- **Transparency:** Integrated **SHAP Explainability** to decode non-linear LSTM predictions into actionable insights.
- **Decision Support:** Real-time Streamlit dashboard for stakeholder risk-visualization.

## 🛠 Tech Stack
- **Quantitative Math:** Modern Portfolio Theory (Efficient Frontier), Sharpe Ratio Optimization.
- **Deep Learning:** LSTM (Long Short-Term Memory) for non-linear price forecasting.
- **Engineering:** Python 3.11, Pytest, GitHub Actions, Streamlit, SHAP.

## 📊 Backtest Results (Impact)
- **Sharpe Ratio Improvement:** +0.16 over the 60/40 benchmark.
- **Risk Mitigation:** 3.1% reduction in Maximum Drawdown.

## ⚙️ Installation & Usage
1. `pip install -r requirements.txt`
2. `export PYTHONPATH=. && python src/main.py`
3. `streamlit run dashboard/app.py`

---
**Author:** Hermona Addisu | **Project:** KAIM Capstone 2026
