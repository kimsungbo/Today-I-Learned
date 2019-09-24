# Pandas Basic

## Object Creation

### Series

* initialization

    ```python
    s = pd.Series([1, 2, 3, 4, 5, np.nan, 8])
    ```

* length

    ```python
    len(s)
    ```

### Dataframe

* initialization

    ```python
    df = pd.DataFrame({'A': 1, 
                    'B': 'String',
                    'C': s,
                    'D': pd.Series([2, 3, 4, 5, 6, 7, 8])})
    ```

* Data type

    ```python
    df.dtypes
    ```

### Read Data From Outside

* Read data from csv file

    ```python
    house_price = pd.read_csv('https://raw.githubusercontent.com/dataitgirls3/Data/master/house_price_sample.csv')
    ```

## Viewing Data

* Retrieve part of data

    ```python
    df.head()
    df.head(2)
    df.tail()
    ```

* Retrieve columns

    ```python
    df.columns
    ```
* Simple summary

    ```python
    df.describe()
    ```

* Dataframe transpose

    ```python
    df.T
    ```

* sort data
    ```python
    df.sort_index(axis=0, ascending=False)
    df.sort_values(by='D', ascending=False)
    ```

## Selection

 * simple selection (should put list if retrieving multiple fields)

    ```python
    df['C']
    df[['C','D']]
    ```

* select by label

    ```python
    df.loc[dates[0]]
    df.loc['20190801':'20190803', ['A', 'B']]
    df.loc[:,['A', 'B']]
    ```
* select by position(index)

    ```python
    df.iloc[0]
    df.iloc[1]
    df.iloc[0:1, 0:2]
    df.iloc[[0, 1], [0, 1]]
    ```