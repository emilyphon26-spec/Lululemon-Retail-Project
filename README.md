<h1>
  <img src="assets/logo.png" alt="Lululemon Sales" width="32" style="margin-right: 8px; padding-top: 10px" />
  Lululemon Promotional Effectiveness Analysis
  (Synthetic Retail Dataset | SQL | Tableau)
</h1>

## Overview
This research analyses whether promotion is efficient for **Lululemon** retail transactions, with a special focus on understanding how promotions influence consumer purchase behavior, especially average amount per transaction. Synthetic data was purposefully used to provide full control over advertising structure, timing, and product behavior, allowing for full evaluation without confidentiality limitations.

Instead of considering promotions as basic revenue sources, this research focuses on additional behavioral lift by comparing transactions with and without promotions, separated by region and product. The byproduct of this analysis is a Tableau dashboard powered by SQL-driven metric programming.

## Business Context
The following features of a Lululemon retail chain are simulated by the synthetic dataset:
- Ten physical locations spread over different regions.
- 50 items in five different categories
- Daily transaction statistics for a year
- Periodically, discounts of 10%, 20%, or 30% are used to promote specific items.
- Promotions are product-specific and have a time limit.

The goal is to determine if promotions encourage more purchases.

## Objectives
The key goals of this project are:
- Measure the promotional additional revenue.
- Examine the typical basket size both with and without promotions.
- Find the regions where promotions work best.
- Find out which goods react best to reductions.
- Use sales data to demonstrate solid data modeling and metric design principles.

## Dataset
Why Use Synthetic Data?
Real retail transaction data is rarely made available. Instead of working with low-quality or unclear datasets, this project provides realistic, customizable retail data in Python.

This method allows:
- Exact modeling of promotion time and discount depth
- A simple difference between promoted and non-promoted transactions.
- Reproducibility and transparency.
> Data has been cleaned and preprocessed to handle missing values, outliers, and inconsistencies.

## Schema Overview
<h1>
  <img src="assets/Schema.png" alt="Schema" width="32" style="margin-right: 8px; padding-top: 10px" />
</h1>
