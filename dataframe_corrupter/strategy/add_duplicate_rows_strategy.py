import pandas as pd
import numpy as np
from .base_strategy import DataCorruptionStrategy

class AddDuplicateRowsStrategy(DataCorruptionStrategy):
    def __init__(self, probability: float):
        self.probability = probability

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        mask = np.random.rand(df.shape[0]) < self.probability
        return pd.concat([df, df[mask]]).reset_index(drop=True)
        