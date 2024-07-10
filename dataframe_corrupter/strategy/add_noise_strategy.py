import pandas as pd
import numpy as np
from .base_strategy import DataCorruptionStrategy

class AddNoiseStrategy(DataCorruptionStrategy):
    def __init__(self, noise_level: float):
        self.noise_level = noise_level

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        noise = np.random.normal(0, self.noise_level, df.shape)
        return df + noise