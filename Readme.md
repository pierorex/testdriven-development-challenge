# Feature description

**Scenario:** invoice calculator.
A store carries a variety of different products. The sales tax for these products is different by product category.
For example cigarettes and alcohol might have a higher tax rate than medicine.

**Goals:** Given a list of products the shopping cart needs to calculate:
* the total price before tax
* the total after tax and the total amount of taxes (split by category).

**Example input:**
```
product id   quantity
---------------------
apple               5
orange              4
milk                2
red wine            3
stamps              4
```

**Desired output:**
```
product id   quantity   price (each)  price (total)   tax rate  tax amount
--------------------------------------------------------------------------
apple               5         0.80 €         4.00 €         7%      0.26 €
orange              4         0.90 €         3.60 €         7%      0.24 €
milk                2         1.19 €         2.38 €         7%      0.16 €
red wine            3         6.99 €        20.97 €        19%      3.35 €
stamps              4         0.65 €         2.60 €         0%      0.00 €
==========================================================================
grand total        18                       12.30 €                 4.00 €
--------------------------------------------------------------------------
subtotal  0% tax    4                        0.65 €                 0.00 €
subtotal  7% tax   11                        2.89 €                 0.65 €
subtotal 19% tax    3                        6.99 €                 3.35 €
```

**Base:** Each supported programming language includes a simple product database implementation with mock data. Prices in the database include tax. A basic skeleton for your result is provided but it's not complete.
