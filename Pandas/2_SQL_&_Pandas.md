# SQL & Pandas

## SELECT

* select specific fields

    ```python
    tips[['total_bill', 'tip']]
    tips[['total_bill', 'tip']].head(5)
    ```

* calculate mean of the column

    ```python
    tips['tip_percentage'].mean()
    ```

* unique

    ```python
    tips['smoker'].unique()
    ```

## WHERE

* condition

    ```sql
    SELECT *
    FROM tips
    WHERE tips.smoker = 'Yes'
    ```

    ```python
    tips[tips['smoker'] == 'Yes'].head(5)
    ```

* multiple conditions

    ```python
    tips[(tips['smoker'] == 'Yes') & (tips['sex'] == 'Female')].head(5)
    ```

## GROUP BY

* group by specific field with count

    ```python
    tips.groupby('day').size()
    ```

* group by with function

    ```python
    tips.groupby('sex')['tip_percentage'].mean()
    tips.groupby(['smoker'])['tip_percentage'].mean()
    tips.groupby(['sex', 'smoker'])['tip_percentage'].mean()
    ```