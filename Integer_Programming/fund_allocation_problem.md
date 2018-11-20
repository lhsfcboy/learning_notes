We have an order of 65 shares, which should be allocated to 3 funds.

| Fund | Quantity |
| ---- | -------- |
| A001 | 20       |
| A002 | 30       |
| A003 | 15       |

Execution is from 3 different brokers.

| Broke  | Quantity | Avg Price |
| ------ | -------- | --------- |
| SMBC   | 20       | p_1 = 101       |
| Citi   | 20       | p_2 = 100.85    |
| Nomura | 25       | p_3 = 102.16    |

We want to allocate trade to fund and make sure
the avg price on each fund are as close as possiblae.
And share should not be divided, share number must be non-negtive integer.

| Fund \ Broker | SMBC | Citi | Nomura | Fund Avg |
| ------------- | ---- | ---- | ------ | -------- |
| A001          | 3    | 9    | 8      | 101.3956 |
| A002          | 14   | 5    | 11     | 101.4003 |
| A003          | 3    | 6    | 6      | 101.4040 |

Now, let's try to figure out the best solution.

| Fund \ Broker | SMBC | Citi | Nomura | Fund Avg                                         |
| ------------- | ---- | ---- | ------ | ------------------------------------------------ |
| A001          | a1_1 | a1_2 | a1_3   | a1_m = (a1_1 * p_1 + a1_2 * p_2 + a1_3 * p_3)/20 |
| A002          | a2_1 | a2_2 | a2_3   | a2_m = (a2_1 * p_1 + a2_2 * p_2 + a2_3 * p_3)/30 |
| A003          | a3_1 | a3_2 | a3_3   | a3_m = (a3_1 * p_1 + a3_2 * p_2 + a3_3 * p_3)/15 |

- All 9 variables must be non-negtive integer.
- At each row, the amount should match each fund's quantity.
```
a1_1 + a1_2 + a1_3 = 20
a2_1 + a2_2 + a2_3 = 30
a3_1 + a3_2 + a3_3 = 15
```
- At each column, the amount should match each broker's quantity
```
a1_1 + a2_1 + a3_1 = 20
a1_2 + a2_2 + a3_2 = 20
a1_3 + a2_3 + a3_3 = 25
```
- Each fund's avg price should be as same as possiable.

a1_m, a2_m, a3_m should have minimum variance.

Note: that this is **NOT** a liner function, as the object expression have square power.

## 混合整数二次計画法

这是一个整数二次规划问题吗?
