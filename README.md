# Pandas-Data-Frame-Corrupter-For-Data-Pipeline-Tests

<p align="center">
  <img src="ReadMeAssets/logo.png" alt="Pandas-Data-Frame-Corrupter-For-Data-Pipeline-Tests">
</p>

`DataFrameCorrupter` is a Python tool designed for data engineering and testing pipelines. It allows you to apply various data corruption strategies to Pandas DataFrames, helping simulate data anomalies and edge cases for testing and development purposes.

## Features

- Apply multiple data corruption strategies to Pandas DataFrames.
- Customize strategies with optional columns to target specific data subsets.
- Easily integrate into data pipeline testing and development workflows.

## Installation

- Clone repository and open it
- run the command `pip install .`, make sure that you are in the `Pandas-Data-Frame-Corrupter-For-Data-Pipeline-Tests` directory

## Usage

### Example Usage

```python
import pandas as pd
from dataframe_corrupter import DataFrameCorrupter
from dataframe_corrupter.strategy import (
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
    (AddDuplicateRowsStrategy(probability=0.2), None),
    (AddNegativeValuesStrategy(probability=0.3), ['A']),
    (AddNullsStrategy(probability=0.1), ['C']),
    (AddNoiseStrategy(std=0.1), columns=['B', 'C']),
    (AddTyposStrategy(probability=0.1), ['B']),
    (DropRowsStrategy(fraction=0.2), None)
])

# Apply corruption strategies
corrupted_df = corrupter.corrupt(df)

print("Original DataFrame:")
print(df)

print("\nCorrupted DataFrame:")
print(corrupted_df)
```
### Output
```plaintext
Original DataFrame:
   A     B    C
0  1   foo  0.1
1  2   bar  0.2
2  3   baz  0.3
3  4   qux  0.4
4  5  quux  0.5

Corrupted DataFrame:
     A     B    C
0  3.0   baz  NaN
1 -4.0   qux  NaN
2  2.0   bar  0.2
3  2.0   baq  0.2
4 -5.0  quux  0.5
5 -3.0   baz  NaN
6 -5.0  quux  NaN
7  4.0   qux  0.4
8  1.0   foo  0.1
```

### Strategies Available

- **AddDuplicateRowsStrategy**: Adds duplicate rows based on a given probability.
- **AddNegativeValuesStrategy**: Adds negative values to specified columns.
- **AddNullsStrategy**: Adds null values to specified columns.
- **AddNoiseStrategy**: Adds noise to numerical columns.
- **AddTyposStrategy**: Introduces typos to string columns.
- **DropRowsStrategy**: Drops a fraction of rows from the DataFrame.

### Customization

You can customize the application of strategies by specifying columns when adding strategies to `DataFrameCorrupter`.

```python
corrupter.add_strategy(AddNegativeValuesStrategy(probability=0.3), columns=['A', 'C'])
```
### Chain of Corruptions
You can chain multiple data corruption strategies together using DataFrameCorrupter to simulate various data anomalies and edge cases for testing and development purposes. Each strategy can be applied to specific columns or the entire DataFrame.
#### Example
```python
    corrupter = DataFrameCorrupter()
    corrupter.add_strategy(AddDuplicateRowsStrategy(probability=0.2))
    corrupter.add_strategy(DropRowsStrategy(fraction=0.2), columns=['A', 'B'])
    corrupter.add_strategy(AddNoiseStrategy(noise_level=0.1), columns=['B', 'C'])
    corrupter.add_strategy(AddNegativeValuesStrategy(probability=0.3), columns=['A', 'C'])
    corrupter.add_strategy(AddNullsStrategy(probability=0.2), columns=['B'])  # Add Nulls to column B
    corrupter.add_strategy(AddTyposStrategy(probability=0.2), columns=['D'])  # Add typos to column D
```

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
