from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class PortfolioConfig:
    tickers: List[str] = field(default_factory=lambda: ["TSLA", "BND", "SPY"])
    start_date: str = "2015-01-01"
    end_date: str = "2025-01-31"
    window_size: int = 60
    batch_size: int = 32
    epochs: int = 5
    risk_free_rate: float = 0.02
