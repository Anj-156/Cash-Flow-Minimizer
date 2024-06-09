class CashFlowMinimizer:
    def __init__(self, friends):
        self.friends = friends
        self.net_amount = [0] * friends

    def add_transaction(self, giver, receiver, amount):
        self.net_amount[giver] -= amount
        self.net_amount[receiver] += amount

    def get_min_transactions(self):
        def min_cash_flow_rec(net_amount):
            max_credit = max(net_amount)
            max_debit = min(net_amount)
            max_credit_index = net_amount.index(max_credit)
            max_debit_index = net_amount.index(max_debit)

            if net_amount[max_credit_index] == 0 and net_amount[max_debit_index] == 0:
                return []

            min_amount = min(-max_debit, max_credit)
            net_amount[max_credit_index] -= min_amount
            net_amount[max_debit_index] += min_amount

            transactions = [(max_debit_index, max_credit_index, min_amount)]
            return transactions + min_cash_flow_rec(net_amount)

        return min_cash_flow_rec(self.net_amount.copy())




friends = 3
cfm = CashFlowMinimizer(friends)
cfm.add_transaction(0, 1, 1000)
cfm.add_transaction(1, 2, 5000)
cfm.add_transaction(2, 0, 2000)

transactions = cfm.get_min_transactions()
for t in transactions:
    print(f"Person {t[0]} pays Person {t[1]}: {t[2]}")
