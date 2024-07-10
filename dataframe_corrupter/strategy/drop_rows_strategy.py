from dataframe_corrupter.corrupter import DataCorruptionStrategy
import pandas as pd

class DropRowsStrategy(DataCorruptionStrategy):
    def __init__(self, fraction: float):
        self.fraction = fraction

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.sample(frac=(1 - self.fraction))