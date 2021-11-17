
class BankAccount()
    def __init__(self, account_id, full_name_owner, balance):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance

    def __str__(self):
        # nice string of the values
        return f'Hello {self.full_name_owner}! your account ID is:{self.account_id}, and your current balance is:{self.balance}'

    def __repr__(self):
        return f'Account ID :{self.account_id}, Name of owner:{self.full_name_owner}, balance: {self.balance}'

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        elif type(other) in [int, float]:
            return self.account_id == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __add__(self, other):
        self.balance += other
        return self

    b1 = BankAccount(1, 'Liza Chelishev', 100000)
    b2 = BankAccount(2, 'May Chelishev', 200000)
