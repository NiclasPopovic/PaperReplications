## Wagner & Whitin (1958) - Dynamic Version of the Economic Lot Size Model
This repository contains a replication of the seminal paper by Wagner & Whitin (1958) published in Management Science (https://doi.org/10.1287/mnsc.5.1.89). The paper introduced a dynamic programming (DP) approach to solving the deterministic lot-sizing problem, which is a foundational model in inventory management and operations research.

### Problem Overview
The **deterministic** lot-sizing problem involves determining the optimal order quantities over a finite planning horizon such that the total cost is minimized. The cost components include:

1. Fixed ordering costs: Cost incurred every time an order is placed, irrespective of the order size.
2. Inventory holding costs: Proportional cost for carrying inventory forward in time.

The model assumes:

- A deterministic demand for each period.
- No backorders or stockouts allowed.
- Orders are fulfilled instantly (no lead time).

The Wagner-Whitin algorithm is an exact method that identifies the optimal production schedule using a recursive DP approach.
