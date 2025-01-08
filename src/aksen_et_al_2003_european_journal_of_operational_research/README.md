## Aksen, Altinkemer & Chand (2003) - Single-Item Lot-Sizing Problem with Immediate Lost Sales

This repository contains a replication of the seminal paper by Aksen, Altinkemer & Chand (2003) published in the European Journal of Operational Research (https://doi.org/10.1016/S0377-2217(02)00331-4). The paper extends the classical lot-sizing problem by introducing the concept of **lost sales** and provides a dynamic programming (DP) approach to solve it.

### Problem Overview

The **single-item lot-sizing problem with immediate lost sales** involves determining the optimal order quantities over a finite planning horizon such that the total cost is minimized. The cost components include:

1. Fixed ordering costs: Cost incurred every time an order is placed, irrespective of the order size.
2. Inventory holding costs: Proportional cost for carrying inventory forward in time.
3. Lost sales costs: Penalty or revenue loss associated with unfulfilled demand in a given period.

The model assumes:

- A deterministic demand for each period is vailable.
- Demand not met is immediately lost (*lost sales*).
- Orders are fulfilled instantly (*no lead time*).

The algorithm introduced by Aksen, Altinkemer & Chand is an exact method that identifies the optimal production schedule using a recursive DP approach.
