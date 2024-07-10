import pandas as pd
import numpy as np
import random
import string
from .base_strategy import DataCorruptionStrategy

class AddTyposStrategy(DataCorruptionStrategy):
    def __init__(self, probability: float):
        self.probability = probability

    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        corrupted_df = df.copy()
        
        for col in corrupted_df.select_dtypes(include=['object']).columns:
            corrupted_df[col] = corrupted_df[col].apply(self._introduce_typos)
        
        return corrupted_df

    def _introduce_typos(self, value: str) -> str:
        if pd.isnull(value) or not isinstance(value, str):
            return value

        chars = list(value)
        for i in range(len(chars)):
            if random.random() < self.probability:
                chars[i] = random.choice(string.ascii_letters)
        
        return ''.join(chars)