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
<p align="center"> <img src="assets/Dashboard.png" alt="Tableau dashboard overview" width="900"> </p>

## Dataset and Schema
<table align="center">
**Dataset Structure**
<div align="center">
  <img width="680" src="assets/Schema.png">
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
KPI Behavioral definitions
<table> 
  <thead> 
    <tr> 
      <th>KPI</th> 
      <th>Definition</th> 
      <th>Why it matters</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Avg Quantity Per Transaction</td> 
      <td>SUM(quantity) / COUNT(DISTINCT transaction_id)</td> 
      <td>Measures the quantities of goods without being distorted by discounting</td> 
    </tr> 
    <tr> 
      <td>Avg With Promo</td> 
      <td>Avg Qty Per Txn where transaction occurs during promo window</td> 
      <td>Purchasing behavior with discounts</td> 
    </tr> 
    <tr> 
      <td>Avg Without Promo</td> 
      <td>Avg Qty Per Txn outside promo window</td> 
      <td>Baseline behavior</td> 
    </tr> 
    <tr> 
      <td>Promotional Lift</td> 
      <td>(Avg With Promo − Avg Without Promo) / Avg Without Promo</td> 
      <td>Behavioral effect due to promotions</td> 
    </tr> 
    <tr> 
      <td>Highest Regional Lift</td> 
      <td>Max lift across regions</td> 
      <td>Targets the region where promos work best</td> 
    </tr> 
  </tbody> 
</table>

## Findings (Based On CSV data)
**Promotional Lift Results**
<table> 
  <thead> 
    <tr> 
      <th>Metric</th> 
      <th>Value</th> 
      <th>Interpretation</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr> 
      <td>Avg With Promotion</td> 
      <td>1.4149</td> 
      <td>Customers buy ~1.41 units/txn during promos</td> 
    </tr> 
    <tr> 
      <td>Avg Without Promotion</td> 
      <td>1.1475</td> 
      <td>Baseline basket size is ~1.15 units/txn</td> 
    </tr> 
    <tr> 
      <td>Promotional Lift</td> 
      <td><b>+23.30%</b></td> <td>Promotions increase basket size by ~23%</td> 
    </tr> 
    <tr> 
      <td>Promoted Transaction Share</td> 
      <td>3.61%</td> 
      <td>Promos are infrequent but impactful</td> 
    </tr> 
  </tbody> 
</table>

**Highest Regional Lift Results**

<table> 
  <thead> 
    <tr> 
      <th>Region</th> 
      <th>Avg With Promo</th> 
      <th>Avg Without Promo</th> 
      <th>Lift</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr>
      <td>
        <b>East</b>
      </td>
      <td>1.4429</td>
      <td>1.1450</td>
      <td>
        <b>+26.01%</b>
      </td>
    </tr> 
    <tr>
      <td>West</td>
      <td>1.4018</td>
      <td>1.1449</td>
      <td>+22.44%</td>
    </tr> 
    <tr>
      <td>Central</td>
      <td>1.4035</td>
      <td>1.1535</td>
      <td>+21.67%</td>
    </tr> 
  </tbody> 
</table>

**Top Products By Promotional Lift (Top 5)**
<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Product</th>
      <th>Category</th>
      <th>Base Price</th>
      <th>Promo Txns</th>
      <th>Avg With Promo</th>
      <th>Avg Without Promo</th>
      <th>Lift</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Rain Rebel Jacket</td>
      <td>Outerwear</td>
      <td>148</td>
      <td>11</td>
      <td>1.6364</td>
      <td>1.1484</td>
      <td><b>+42.49%</b></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Festival Bag</td>
      <td>Accessories</td>
      <td>68</td>
      <td>40</td>
      <td>1.5750</td>
      <td>1.1475</td>
      <td><b>+37.26%</b></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Surge Short</td>
      <td>Shorts</td>
      <td>68</td>
      <td>68</td>
      <td>1.5441</td>
      <td>1.1330</td>
      <td><b>+36.28%</b></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Fast and Free Short</td>
      <td>Shorts</td>
      <td>68</td>
      <td>35</td>
      <td>1.5429</td>
      <td>1.1349</td>
      <td><b>+35.95%</b></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Light Locks Scrunchie</td>
      <td>Accessories</td>
      <td>18</td>
      <td>49</td>
      <td>1.5306</td>
      <td>1.1511</td>
      <td><b>+32.97%</b></td>
    </tr>
  </tbody>
</table>

**Discount Mix During Promotions**
<table> 
  <thead> 
    <tr> 
      <th>Discount Level</th> 
      <th>Promoted Transactions</th> 
      <th>Share</th> 
    </tr> 
  </thead> 
  <tbody> 
    <tr>
      <td>10%</td>
      <td>780</td>
      <td>33.85%</td>
    </tr> 
    <tr>
      <td>20%</td>
      <td>390</td>
      <td>16.93%</td>
    </tr> 
    <tr>
      <td>30%</td>
      <td>1,134</td>
      <td>49.22%</td>
    </tr> 
  </tbody> 
</table>
