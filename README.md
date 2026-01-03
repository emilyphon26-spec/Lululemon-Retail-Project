<h1>
  <img src="assets/logo.png" alt="Lululemon Sales" width="32" style="margin-right: 8px; padding-top: 10px" />
  Lululemon Promotional Effectiveness Analysis
  (Synthetic Retail Dataset | SQL | Tableau)
</h1>

## Client Background
Lululemon is a worldwide athletic wear shop with strong brand loyalty and premium pricing. Promotions are used strategically to drive demand, move inventory, and attract consumers; however, discounts must be carefully considered because they might cut profit without delivering substantial additional volume. This study assesses promotion-driven behavioral lift with a controlled synthetic dataset that simulates genuine retail dynamics (product catalog, store regions, promotions within a time frame, and daily transactions).

## Business Context
The following features of a Lululemon retail chain are simulated by the synthetic dataset:
- Ten physical locations spread over different regions.
- 50 items in five different categories
- Daily transaction statistics for a year
- Periodically, discounts of 10%, 20%, or 30% are used to promote specific items.
- Promotions are product-specific and have a time limit.

## Objectives
The key goals of this project are:
- Measure the promotional additional revenue.
- Examine the typical basket size both with and without promotions.
- Find the regions where promotions work best.
- Find out which goods react best to reductions.
- Use sales data to demonstrate solid data modeling and metric design principles.

## Summary
**Promo Effectiveness (Behavioral Lift)**
This study measures promotion impact using Avg Quantity Per Transaction, which avoids revenue distortion caused purely by discounting.
**Headline results (from CSVs):**
- Avg Quantity With Promotion: 1.4149
- Avg Quantity Without Promotion: 1.1475
- Promotional Lift: +23.30%
- Highest Regional Lift: East (+26.01%)
<p align="center"> <img src="Dashboard.pdf" alt="Tableau dashboard overview" width="900"> </p>

## Dataset and Schema
<table align="center">
**Dataset Structure**
<div align="center">
  <img width="680" src="Schema.png">
</div>
<table> 
  <thead> 
    <tr> 
      <th>Component</th> 
      <th>Value</th> 
      <th>Notes</th> </tr> 
  </thead> 
  <tbody> 
    <tr>
      <td>Date Range</td>
      <td>2024-01-01 → 2024-12-30</td>
      <td>365 unique days</td></tr> 
    <tr>
      <td>Total Transactions</td>
      <td>63,890</td>
      <td>Transaction-level rows</td>
    </tr> 
    <tr>
      <td>Stores</td>
      <td>10</td>
      <td>Across 3 regions</td>
    </tr> 
    <tr>
      <td>Regions</td>
      <td>3</td>
      <td>Central, East, West</td>
    </tr> 
    <tr>
      <td>Products</td>
      <td>50</td>
      <td>Across 5 categories</td>
    </tr> 
    <tr>
      <td>Promotions</td>
      <td>47</td>
      <td>Product-level date-range promos</td>
    </tr> 
    <tr>
      <td>Promoted Txn Share</td>
      <td>3.61%</td>
      <td>Transactions during promo windows</td>
    </tr> 
  </tbody> 
</table>

## KPI Framework


