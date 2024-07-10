import pandas as pd
import numpy as np
from .base_strategy import DataCorruptionStrategy

class AddNegativeValuesStrategy(DataCorruptionStrategy):
    def __init__(self, probability: float):
        self.probability = probability

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        mask = np.random.rand(*df.shape) < self.probability
        df[mask] = -df[mask]
        return df