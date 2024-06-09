# Cash-Flow-Minimizer
This project involves calculating the minimum number of transactions required to settle debts among a group of friends.


## Overview

The Cash Flow Minimizer project is a Python application designed to calculate the minimum number of transactions required to settle debts among a group of friends. The application uses graph algorithms to efficiently settle debts and minimize cash flow.

## Features

- Add transactions between friends
- Calculate the net amount each person owes or is owed
- Determine the minimum number of transactions to settle all debts
- Output the transactions required to minimize cash flow

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cash-flow-minimizer.git
    cd cash-flow-minimizer
    ```

2. (Optional) Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Create an instance of `CashFlowMinimizer` with the number of friends:
    ```python
    from cash_flow_minimizer import CashFlowMinimizer
    cfm = CashFlowMinimizer(friends)
    ```

2. Add transactions:
    ```python
    cfm.add_transaction(giver, receiver, amount)
    ```

3. Calculate the minimum number of transactions:
    ```python
    transactions = cfm.get_min_transactions()
    for t in transactions:
        print(f"Person {t[0]} pays Person {t[1]}: {t[2]}")
    ```

### Example

```python
from cash_flow_minimizer import CashFlowMinimizer

# Initialize with 3 friends
cfm = CashFlowMinimizer(3)

# Add transactions: Person 0 gives Person 1 $1000, and so on.
cfm.add_transaction(0, 1, 1000)
cfm.add_transaction(1, 2, 5000)
cfm.add_transaction(2, 0, 2000)

# Get the list of minimal transactions to settle all debts
transactions = cfm.get_min_transactions()

# Output the transactions
for t in transactions:
    print(f"Person {t[0]} pays Person {t[1]}: {t[2]}")

