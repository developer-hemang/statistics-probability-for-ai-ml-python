# One Way Tables

# Individuals and Variables

## Individual:

An individual is a single entity or observation that we are studying.

It could be:
- One person
- One customer
- One company
- One stock
- One transaction
- One day of market data
- One trade

## 📊 What is a Variable?

A variable is a characteristic or measurement that can have different values for different individuals.

Together, individuals and variables are called data. 

# 📈 Nifty + OHLCV Example

Suppose you have Nifty 50 daily OHLCV data:

When we organize data into a table like this one, we call it a data table, here is a example of data table of NIFTY 50 OHLC Data

| Date   |   Open |   High |    Low |  Close | Volume |
| ------ | -----: | -----: | -----: | -----: | -----: |
| 01-Sep | 24,500 | 24,650 | 24,400 | 24,600 |   125M |
| 02-Sep | 24,600 | 24,750 | 24,550 | 24,700 |   118M |
| 03-Sep | 24,700 | 24,800 | 24,580 | 24,650 |   132M |


Here, each trading day is an observation/individual.

For example:

- 01-Sep → one observation/individual
- 02-Sep → one observation/individual
- 03-Sep → one observation/individual


And the variables are:

- Date
- Open
- High
- Low
- Close
- Volume


Variables can be categorical or quantitative. 

## Categorical variables 

Categorial variables are non-numerical variables. Categorical variables are also called "Qualitative" variables Their values aren't represented with numbers 

> Simple definition: A categorical variable tells us which category an observation belongs to.

# Example 

| Variable          | Example values                | Type        |
| ----------------- | ----------------------------- | ----------- |
| Market Condition  | Bullish, Bearish, Neutral     | Categorical |
| Signal            | Buy, Hold, Sell               | Categorical |
| Trend             | Uptrend, Downtrend, Sideways  | Categorical |
| RSI Condition     | Oversold, Neutral, Overbought | Categorical |
| Sector            | IT, Banking, Pharma, Energy   | Categorical |
| Candle Type       | Bullish, Bearish, Doji        | Categorical |
| Volatility Regime | Low, Medium, High             | Categorical |


# quantitative variable
A quantitative variable is a variable whose values are numbers that represent a measurable quantity.

> Simple definition: A quantitative variable tells us how much, how many, or what numerical value something has.

# Example 

| Variable       |     Example | Type         |
| -------------- | ----------: | ------------ |
| Open Price     |     ₹24,500 | Quantitative |
| High Price     |     ₹24,650 | Quantitative |
| Low Price      |     ₹24,400 | Quantitative |
| Close Price    |     ₹24,600 | Quantitative |
| Volume         | 125,000,000 | Quantitative |
| RSI            |        28.5 | Quantitative |
| Daily Return   |       0.82% | Quantitative |
| Volatility     |       1.35% | Quantitative |
| Moving Average |     ₹24,320 | Quantitative |


## Quantitative variables are generally divided into two types: discrete and continuous variables.

Quantitative Variables
        │
        ├── Discrete
        │
        └── Continuous

## 1. 🔢 Discrete Variables
A discrete variable is a quantitative variable that can take countable, separate values.

### > Simple definition: Discrete variables are values that we count.

## 📈 Examples

| Variable                              | Example |
| ------------------------------------- | ------: |
| Number of trades                      |     250 |
| Number of transactions                |   1,250 |
| Number of bullish days                |      15 |
| Number of times price touched a level |       8 |
| Number of stocks in a portfolio       |      25 |


##  2. 📏 Continuous Variables

A continuous variable is a quantitative variable that can take any value within a range, including decimal values.

> Simple definition: Continuous variables are values that we measure.

### Note: 
> Discrete does not simply mean "integer," and continuous does not simply mean "decimal."


## 🧠 Important AI/ML connection

In machine learning, we often use the word feature for a variable that is used as an input to a model.

> Individual/observation = one row of your dataset.
> Variable = one column describing that observation.
> Feature = a variable used as an input to an ML model.



# 📏 Levels of Measurement

Level of measurement tells us what kind of information a variable provides and what mathematical operations make sense to perform on it.

There are four levels of measurement:


Levels of Measurement
│
├── 1. Nominal
├── 2. Ordinal
├── 3. Interval
└── 4. Ratio

A simple way to remember the progression:

> Nominal → names
> Ordinal → order
> Interval → equal intervals
> Ratio → equal intervals + true zero

### 1. 🏷️ Nominal

A nominal variable divides observations into different categories or names, but the categories have no natural order.

> Nominal = Name/Category

Example : Suppose you classify companies by sector:

| Company   | Sector  |
| --------- | ------- |
| Company A | Banking |
| Company B | IT      |
| Company C | Pharma  |
| Company D | Banking |

Sector is nominal because:

```python
Banking
IT
Pharma
```

There is no meaningful order such as:

```python
Banking > IT > Pharma

```

### 2. 🥇 Ordinal

An ordinal variable has categories that can be ordered or ranked, but the difference between the categories is not necessarily equal or measurable.

> Ordinal = Order/Rank

## Example Trend Strength :

| Day   | Sentiment |
| ----- | --------- |
| Day 1 | Bearish   |
| Day 2 | Neutral   |
| Day 3 | Bullish   |


There is an order:

```python
Bearish → Neutral → Bullish
```

But we cannot say the difference between:

```python
Bearish → Neutral
```


### 3. 🌡️ Interval

An interval variable has:

- Ordered values
- Equal differences between values
- But no meaningful true zero

> Interval = Equal intervals, but zero doesn't mean "none."

> Simple Defination: Interval measurement is a scale where the order and differences between values are meaningful, but zero is not a true "none" point.

An interval measurement is a measurement scale where:

- The values have a meaningful order.
- The difference between values is equal and meaningful.
- There is no true zero point.

## 🌡️ Interval Measurement — Simple Example

Imagine the temperature outside:

| City   | Temperature |
| ------ | ----------: |
| Mumbai |        30°C |
| Delhi  |        35°C |
| Jaipur |        40°C |

### What makes this an interval measurement?

The difference between temperatures is meaningful:

- Delhi − Mumbai = 5°C
- Jaipur − Delhi = 5°C

So the intervals are equal.

But 0°C does not mean "no temperature."

0°C simply represents a particular temperature point on the Celsius scale.

That's why we cannot say:

> 40°C is twice as hot as 20°C.

So the intervals are equal.

The difference between them is 20°C, but the ratio 40 / 20 = 2 does not have the same meaningful interpretation.


# ⚖️ Ratio Measurement

Simple definition

> A ratio variable tells us how much, has equal measurement intervals, and has a meaningful zero, so statements like “twice as much” are meaningful.

A ratio measurement is a measurement scale where:

- Values can be ordered.
- The difference between values is meaningful.
- The intervals between values are equal.
- There is a true zero, meaning zero represents the complete absence of the quantity.
- Because of the true zero, ratios are meaningful.


## 📈 Stock Market Example: Trading Volume

Trading volume is a very good ratio-scale example.

| Stock | Trading Volume |
| ----- | -------------: |
| A     |   1,000 shares |
| B     |   2,000 shares |
| C     |   4,000 shares |

 
### 1. There is an order

```python
1,000 < 2,000 < 4,000
```

So we know which has more volume.

### 2. Differences are meaningful

```python
2,000 - 1,000 = 1,000
4,000 - 2,000 = 2,000
```

A difference of 1,000 shares always represents 1,000 shares.


### 3. There is a true zero

```python
0 shares traded
```
means no shares were traded.


### 4. Ratios are meaningful

This is the important part:

```python
4,000 / 2,000 = 2
```

So we can correctly say:

> 4,000 shares is twice the trading volume of 2,000 shares.

And:

```python
So 4,000 shares is four times 1,000 shares.
```
### That's why trading volume is a strong real-world example of ratio measurement.

# 📊 One-Way Table

A one-way table is a table that summarizes one variable by showing its different values or categories and how many observations fall into each category.

> One variable → count how often each value/category occurs → one-way table

## 📈 Example with NIFTY

| Day | Market Condition |
| --- | ---------------- |
| 1   | Bullish          |
| 2   | Neutral          |
| 3   | Bullish          |
| 4   | Bearish          |
| 5   | Neutral          |
| 6   | Bullish          |
| 7   | Bearish          |
| 8   | Neutral          |
| 9   | Bullish          |
| 10  | Neutral          |


We have 10 observations, but we're studying only one variable:

```
Market Condition
```

We can summarize it:

| Market Condition | Frequency |
| ---------------- | --------: |
| Bullish          |         4 |
| Neutral          |         4 |
| Bearish          |         2 |
| **Total**        |    **10** |

This is a one-way frequency table.