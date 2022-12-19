class CreditCard: 
    """A consumer credit card."""

    def __init__(self, customer, bank, account, limit): 
        """Create a new credit card instance. 

        The initial balance is zero. 

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        account     the account identifier (e.g., '1234 5678 3456 1234')
        limit       credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank 
        self._account = account 
        self._limit = limit 
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer 

    def get_bank(self): 
        """Return the bank's name."""
        return self._bank

    def get_account(self): 
        """Return the card identifying number (typically stored as a string).""" 
        return self._account 

    def get_limit(self): 
        """return current credit limit."""
        return self._limit

    def get_balance(self): 
        """Return current balance"""
        return self._balance

    def charge(self, price): 
        """Charge given price to the card, assuming sufficient credit limit. 

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit: 
            return False
        else: 
            self._balance += price 
            return True
    
    def make_payment(self, amount): 
        """Process customer payment that reduces balance."""
        self._balance -= amount


class PredatoryCreditCard(CreditCard): 
    """An extension to CreditCard that compounds interest and fees."""

    OVERLIMIT_FEE = 5       # this is a class-level member
    def __init__(self, customer, bank, account, limit, apr): 
        """Create a new predatory credit card instance.
        
        The initial balance is zero.
        
        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        account     the account identifier (e.g., '1234 5678 3456 1234')
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR
        """
        super().__init__(customer, bank, account, limit) # call super constructor
        self._apr = apr 

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit. 

        Return True if charge was processed
        Return False and assess $5 fee if charge is denied.
        """        
        success = super().charge(price) # call inherited method
        if not success: 
            self._balance += 5          # assess penalty
        return success                  # caller expects return value

    def process_month(self): 
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0: 
            # if positive balance, convert APR to monthly multiplicative factor 
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == '__main__': 
    wallet = [] 
    wallet.append(CreditCard('Prince Okpoziakpo', '1st Bank', '1111 2222 3333 4444', 2500)) 
    wallet.append(CreditCard('Prince Okpoziakpo', '2nd Bank', '1212, 2323 4545 6565', 3500)) 
    wallet.append(CreditCard('Prince Okpoziakpo', '3rd Bank', '1122 2233 4455 6677', 5000))
    for val in range(1, 17): 
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(3): 
        print('Customer =', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100: 
            wallet[c].make_payment(100)
            print('New cbalance = ', wallet[c].get_balance())
        print()
        