from typing import List, Optional, Tuple
import pandas as pd
from .strategy.base_strategy import DataCorruptionStrategy

class DataFrameCorrupter:
    def __init__(self, strategies: List[Tuple[DataCorruptionStrategy, Optional[List[str]]]] = None):
        self._strategies = strategies if strategies is not None else []

    def add_strategy(self, strategy: DataCorruptionStrategy, columns: Optional[List[str]] = None):
        self._strategies.append((strategy, columns))

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        corrupted_df = df.copy().reset_index(drop=True)
        for strategy, columns in self._strategies:
            if columns:
                corrupted_df[columns] = strategy.corrupt(corrupted_df[columns])
            else:
                corrupted_df = strategy.corrupt(corrupted_df)
        return corrupted_df.reset_index(drop=True)
