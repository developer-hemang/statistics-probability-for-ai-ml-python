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


# 📈 Nifty + OHLCV Example

Suppose you have Nifty 50 daily OHLCV data:

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

## 🧠 Important AI/ML connection

In machine learning, we often use the word feature for a variable that is used as an input to a model.

> Individual/observation = one row of your dataset.
> Variable = one column describing that observation.
> Feature = a variable used as an input to an ML model.