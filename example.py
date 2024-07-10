import pandas as pd
from dataframe_corrupter import DataFrameCorrupter
from dataframe_corrupter import (
    AddDuplicateRowsStrategy,
    AddNegativeValuesStrategy,
    AddNullsStrategy,
    AddNoiseStrategy,
    AddTyposStrategy,
    DropRowsStrategy
)

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['foo', 'bar', 'baz', 'qux', 'quux'],
    'C': [0.1, 0.2, 0.3, 0.4, 0.5]
}
df = pd.DataFrame(data)

# Initialize DataFrameCorrupter with strategies
corrupter = DataFrameCorrupter([
    (AddDuplicateRowsStrategy(probability=0.7), None),
    (AddNegativeValuesStrategy(probability=0.3), ['A']),
    (AddNullsStrategy(probability=0.4), ['C']),
    (AddNoiseStrategy(noise_level=0), ['A', 'C']),
    (AddTyposStrategy(probability=0.1), ['B']),
    (DropRowsStrategy(fraction=0.02), None)
])

# Apply corruption strategies
corrupted_df = corrupter.corrupt(df)

print("Original DataFrame:")
print(df)

print("\nCorrupted DataFrame:")
print(corrupted_df)
