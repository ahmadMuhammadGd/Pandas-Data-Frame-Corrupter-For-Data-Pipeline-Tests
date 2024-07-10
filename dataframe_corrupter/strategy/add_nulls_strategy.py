import pandas as pd
import numpy as np
from .base_strategy import DataCorruptionStrategy

class AddNullsStrategy(DataCorruptionStrategy):
    def __init__(self, probability: float):
        self.probability = probability

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in df.columns:
            df.loc[df.sample(frac=self.probability).index, col] = None
        return df