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
# Terminology & Abbreviations
- **Txn**: Transaction  
- **Promo Txn**: A transaction occurring during an active promotion window  
- **Lift**: Percentage change in average quantity per transaction relative to baseline  
- **Avg Qty / Txn**: Average quantity per transaction

**Promo Effectiveness (Behavioral Lift)**
This study measures promotion impact using Avg Quantity Per Transaction, which avoids revenue distortion caused purely by discounting.
**Headline results (from CSVs):**
- Avg Quantity With Promotion: 1.4149
- Avg Quantity Without Promotion: 1.1475
- Promotional Lift: +23.30%
- Highest Regional Lift: East (+26.01%)
<p align="center"> <img src="assets/Dashboard.png" alt="Tableau dashboard overview" width="600"> </p>

These results are combined into an interactive, executive-facing manner in the Tableau dashboard. While regional and product-level charts allow stakeholders to dig deeper into areas of interest, KPI tiles offer instant visibility into the overall promotional impact.

The dashboard is intended to assist with: 
- Strategic planning (where promotions are most effective)
- Execution of strategy (items to promote)
- Performance tracking (how lift varies by segment or over time)

The analysis guarantees consistency between underlying logic and visual output by directly matching dashboard measurements with developed SQL KPIs.

## Dataset and Schema
<table align="center">
  
**Dataset Structure**
<div align="center">
  <img width="500" src="assets/Schema.png">
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
      <td>2024-01-01 to 2024-12-30</td>
      <td>365 unique days</td></tr> 
    <tr>
      <td>Total Transactions</td>
      <td>63,890</td>
      <td>Transaction rows</td>
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
The KPI framework purposefully places more emphasis on behavioral measurements than just profits. Measuring based on revenue may overestimate promotional performance even in cases when customer behavior does not significantly change since promotions simply lower prices. This study separates variations in basket size, which more accurately represent extra demand, by concentrating on average amount per transaction. This method provides an answer to a more strategic question: _Do consumers genuinely purchase more goods during a promotion, or do they just pay less for the same item?_ 

In order to ensure that findings may be interpreted as progressive impacts rather than absolute differences, Promotional Lift is defined in relation to the non-promoted baseline. This KPI design is in line with typical retail analytics procedures used to assess campaign efficacy and promotional ROI.

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
The findings demonstrate a unique and significant behavioral reaction to promotions. During promotional periods, the average amount per transaction rises from 1.1475 units under normal circumstances to 1.4149 units, representing a 23.30% promotional lift. This suggests that promotions are encouraging people to add more products to their baskets rather than just lowering their current purchases. Considering the very small percentage of transactions exposed to promotions, the size of this rise is significant.

Crucially, this impact is seen even when promotions are brief and product-specific, indicating that, when properly targeted, even a little amount of promotional exposure can result in significant behavioral changes. However, these findings should be understood as demand-side effect rather than profitability because this research concentrates on quantity rather than margin or revenue. If discount level is not covered by incremental units, promotions may still be unproductive.

**Highest Regional Lift Results**

<div align="center">
  <img width="300" src="assets/Regional Lift.png">
</div>
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

Regional differences in promotional efficacy are significant. With a 26.01% boost, the East area shows the highest reaction, surpassing both the West (22.44%) and Central (21.67%) regions.

The differences imply that consumer openness to marketing changes by region. Regional variations in price sensitivity, client demographics, competition pressure, or baseline purchase habit are examples of potential factors.

These findings suggest that distributing promotional capital evenly throughout regions might not be the best course of action from a strategic standpoint. While locations with lower lift could need other tactics like product bundling or non-price incentives, regions with more responsiveness might be able to justify more frequent or deeper discounts. The precise causes of regional variations are controlled rather than seen since the dataset is synthetic. Nonetheless, the structure is similar to actual retail trends, where promotional strategy heavily relies on geographic variability.

**Top Products By Promotional Lift (Top 5)**

<div align="center">
  <img width="680" src="assets/Product Lift.png">
</div>
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

A subset of items exhibit a high concentration of promotional lift, according to product-level data. The best-performing products have lift values that are much higher than the average, ranging from about 33% to over 42%.

Notably, these items fall under several categories, such as shorts, accessories, and outerwear. This implies that specific product attributes like price point, frequency of purchases, and perceived voluntary nature have an impact on promotional interest in addition to category-driven factors.

While expensive goods (like the Rain Rebel Jacket) could profit from promotion by lowering psychological purchase barriers, cheaper accessories (like the Light Locks Scrunchie) show considerable lift, perhaps as a result of impulsive buying behavior.

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

Nearly half of all promoted transactions occur under 30% discounts, with smaller shares attributable to 10% and 20% promotions. This distribution suggests a strong reliance on deeper discounts to drive promotional activity.

While deeper discounts appear effective in generating transaction volume, they also carry higher margin risk. Without revenue and cost data, it is not possible to determine whether 30% discounts produce superior net returns relative to shallower promotions.

From an analytical standpoint, this finding highlights an important next step: evaluating lift efficiency, defined as incremental quantity gained per percentage point of discount. Such an analysis would help determine whether smaller discounts could achieve comparable behavioral effects at lower cost.

## Recommendations

**Prioritize Promotions in High-Response Regions**
Outperforming both the West and Central areas, the East region has the highest promotional lift (~26%). This implies that consumers in the East are more receptive to promotional offers, either because they are more aware of promotions or because they are more price sensitive. Lululemon can take actions such as
- Give the East area a larger portion of advertising campaigns.
- While keeping longer or deeper campaigns in high-lift locations, test slightly shorter marketing periods in lower-lift regions.
- When choosing where to use new marketing tactics, use regional lift as a restriction indicator.
This in turn will enhance effectiveness of advertisements by focusing discounts on areas with the best behavioral return.

**Products**
Promotional impact is concentrated among just a handful of products. The top five goods show a 30-40%+ boost, well above the total average.
Actionable Steps:
- Create a short list of "promo-responsive" items based on historical lift.
- Discounts on certain goods should be prioritized above wide category-level promotions.
- Avoid marketing low-response goods that don't significantly improve basket size.
This will increase demand per promotion and decrease in margins.

**Discounts**
Nearly half of advertised transactions are at 30% discounts, indicating a dependence on bigger price drops to generate demand. While successful, deeper discounts have a larger margin risk.
Actionable Steps:
- Test if 20% reductions result in a comparable rise for high-response goods.
- Determine lift efficiency (incremental amount per percentage point of discount).
- Save larger discounts for items or times that have demonstrated responsiveness.
This will maintain promotional effectiveness while lowering discount costs and improving profitability potential.


