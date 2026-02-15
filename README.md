# GMF Strategic Portfolio Optimization (Production Grade)

![CI Status](https://github.com/HermonaDev/portfolio-optimization-capstone/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Coverage](https://img.shields.io/badge/test_coverage->85%25-green)

## 📌 Project Overview
This Capstone project transforms a quantitative finance research model into a **production-ready software system**. It focuses on maximizing the **Sharpe Ratio** and reducing **Maximum Drawdown** for a portfolio consisting of TSLA, BND, and SPY.

## 🚀 Engineering Highlights (Evidence of Excellence)
- **Production Refactoring:** Shifted from scripts to a modular package using **Type Hints** and **Dataclasses**.
- **Automated Testing:** 5 unit tests verifying financial logic via `pytest`.
- **CI/CD Pipeline:** Automated Linting (Flake8) and Testing (Pytest) via GitHub Actions.
- **Transparency:** Integrated SHAP explainability for LSTM forecasts (In Progress).

## 🛠 Project Structure
- `src/`: Modular core (Data Ingestion, LSTM Models, MPT Optimization).
- `tests/`: Automated test suite.
- `dashboard/`: Interactive Streamlit UI for stakeholders.

## 📈 Demo & Results
- **Expected Sharpe Ratio:** ~1.37 (Strategy) vs 1.21 (Benchmark).
- **Risk Reduction:** ~3.1% improvement in Max Drawdown via dynamic rebalancing.

## ⚙️ Installation
```bash
pip install -r requirements.txt
export PYTHONPATH=.
pytest tests/
streamlit run dashboard/app.py
```
