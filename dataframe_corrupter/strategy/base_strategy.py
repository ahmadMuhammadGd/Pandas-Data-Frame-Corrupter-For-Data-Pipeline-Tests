import pandas as pd
from abc import ABC, abstractmethod

class DataCorruptionStrategy(ABC):
    @abstractmethod
    def corrupt(self, df: pd.DataFrame) -> pd.DataFrame:
        pass