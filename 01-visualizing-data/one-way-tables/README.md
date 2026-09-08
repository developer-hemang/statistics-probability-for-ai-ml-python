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