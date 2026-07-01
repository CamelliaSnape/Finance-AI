class AppState:

    def __init__(self):

        self.transactions = []

        self.current_user = None

    # ==========================
    # USER
    # ==========================

    def set_user(self, user):
        self.current_user = user

    def get_user(self):
        return self.current_user

    # ==========================
    # TRANSACTIONS
    # ==========================

    def set_transactions(self, transactions):
        self.transactions = list(transactions)

    def get_transactions(self):
        return self.transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction):
        if transaction in self.transactions:
            self.transactions.remove(transaction)

    def clear_transactions(self):
        self.transactions.clear()