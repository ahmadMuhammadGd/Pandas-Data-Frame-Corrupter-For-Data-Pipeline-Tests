from dataframe_corrupter import DataFrameCorrupter
from dataframe_corrupter import AddDuplicateRowsStrategy, AddNegativeValuesStrategy, AddNoiseStrategy, AddNullsStrategy, AddTyposStrategy, DropRowsStrategy

import pandas as pd

if __name__ == "__main__":
    # Sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 20, 30, 40, 50],
        'D': ['apple', 'banana', 'cherry', 'date', 'elderberry']
    }
    df = pd.DataFrame(data)

    # Initialize the corrupter with no initial strategies
    corrupter = DataFrameCorrupter()

    # Add strategies with specified columns
    corrupter.add_strategy(AddDuplicateRowsStrategy(probability=0.2))
    corrupter.add_strategy(DropRowsStrategy(fraction=0.2), columns=['A', 'B'])
    corrupter.add_strategy(AddNoiseStrategy(noise_level=0.1), columns=['B', 'C'])
    corrupter.add_strategy(AddNegativeValuesStrategy(probability=0.3), columns=['A', 'C'])
    corrupter.add_strategy(AddNullsStrategy(probability=0.2), columns=['B'])  # Add Nulls to column B
    corrupter.add_strategy(AddTyposStrategy(probability=0.2), columns=['D'])  # Add typos to column D

    # Apply the corruptions
    corrupted_df = corrupter.corrupt(df)
    print("After Applying Chained Corruptions:")
    print(corrupted_df)
