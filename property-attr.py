class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("New balance has to be non-negative!")
        self._balance = new_bal

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("New balance has to be non-negative!")
        self._balance = new_bal
        print("Setter method is called")

     
cust = Customer('Belinda Lutz', 2000)
cust.balance = 3000
print(cust.balance)
