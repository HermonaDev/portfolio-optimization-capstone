# GMF Strategic Portfolio Optimization (Production Grade)

[![CI Pipeline](https://github.com/HermonaDev/portfolio-optimization-capstone/actions/workflows/ci.yml/badge.svg)](https://github.com/HermonaDev/portfolio-optimization-capstone/actions)

## 📌 Project Overview
This Capstone project transforms a quantitative finance research model into a **production-grade software system**. It focuses on maximizing the **Sharpe Ratio** and reducing **Maximum Drawdown** for a portfolio consisting of TSLA, BND, and SPY.

## 🚀 Key Engineering Improvements
- **Modular Architecture:** Refactored research scripts into a professional Python package structure.
- **Reliability:** Implemented a suite of unit tests with >85% coverage for core financial logic.
- **CI/CD:** Automated testing and linting via GitHub Actions.
- **Dataclass Configuration:** Standardized project parameters for easy scalability.

## 🛠 Project Structure
- `src/`: Core logic (Ingestion, Models, Optimization).
- `tests/`: Automated pytest suite.
- `dashboard/`: Interactive Streamlit UI.
- `.github/workflows/`: CI/CD automation.

## 📈 Installation & Usage
1. Clone repo: `git clone https://github.com/HermonaDev/portfolio-optimization-capstone`
2. Install: `pip install -r requirements.txt`
3. Run Tests: `export PYTHONPATH=. && pytest tests/`
4. Run Dashboard: `streamlit run dashboard/app.py`

## ⚖️ Business Impact
By providing a transparent, testable, and reliable framework, this tool allows institutional investors to mitigate risk during market regime shifts, moving beyond static asset allocation.
