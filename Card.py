

class Card:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def pay(self, amount):
        if self.balance < amount:
            print ( "Insufficient funds on the card" )
        else:
            self.balance -= amount
            print ( f"Successful payment in the amount of {amount} dinars. New balance: {self.balance} dinars." )


class Visa ( Card ):
    def __init__(self, number, balance):
        super ().__init__ ( number, balance )

    def pay(self, amount):
        tax = amount * 0.05
        total_amount = amount + tax
        if self.balance < total_amount:
            print ( "Insufficient funds on the card" )
        else:
            self.balance -= total_amount
            print (f"Successful payment in the amount of {amount} dinars with tax of {tax} dinars. New balance: {self.balance} dinars." )


class Master ( Card ):
    def __init__(self, number, balance):
        super ().__init__ ( number, balance )

    def pay(self, amount):
        tax = amount * 0.08
        total_amount = amount + tax
        if self.balance < total_amount:
            print ( "Insufficient funds on the card" )
        else:
            self.balance -= total_amount
            print (f"Successful payment in the amount of {amount} dinars with tax of {tax} dinars. New balance: {self.balance} dinars." )


visa_card = Visa(123456, 1000)
visa_card.pay(500)
master_card = Master(987654, 2000)
master_card.pay(1000)



















