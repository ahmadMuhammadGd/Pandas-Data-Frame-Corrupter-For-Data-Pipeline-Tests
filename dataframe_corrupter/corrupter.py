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

'''
usage examle:

if __name__ == "__main__":
    # Sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)

    # Initialize the corrupter with no initial strategies
    corrupter = DataFrameCorrupter()

    # Add strategies with specified columns
    corrupter.add_strategy(DropRowsStrategy(fraction=0.2), columns=['A', 'B'])
    corrupter.add_strategy(AddNoiseStrategy(noise_level=0.1), columns=['B', 'C'])
    corrupter.add_strategy(ShuffleColumnsStrategy())  # This strategy applies to the whole DataFrame

    # Apply the corruptions
    corrupted_df = corrupter.corrupt(df)
    print("After Applying Chained Corruptions:")
    print(corrupted_df)
    
'''