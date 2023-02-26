"""
Vežba 1:

Kreirati klasu Card koja ima polja broj i stanje i metodu pay.

Metoda pay skida određenu sumu sa stanja kartice.

Kreirati klase Visa i Master, koje nasleđuju klasu Card, ali prilikom naplate naplaćuju i porez, koji za Visa karticu
iznosi 5%, a za Master karticu 8%.
"""


class Card:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def pay(self, amount):
        if self.balance < amount:
            print ( "Nedovoljno sredstava na kartici" )
        else:
            self.balance -= amount
            print ( f"Uspesno placanje u iznosu od {amount} dinara. Novo stanje: {self.balance} dinara." )


class Visa ( Card ):
    def __init__(self, number, balance):
        super ().__init__ ( number, balance )

    def pay(self, amount):
        tax = amount * 0.05
        total_amount = amount + tax
        if self.balance < total_amount:
            print ( "Nedovoljno sredstava na kartici" )
        else:
            self.balance -= total_amount
            print (
                f"Uspesno placanje u iznosu od {amount} dinara uz porez od {tax} dinara. Novo stanje: {self.balance} dinara." )


class Master ( Card ):
    def __init__(self, number, balance):
        super ().__init__ ( number, balance )

    def pay(self, amount):
        tax = amount * 0.08
        total_amount = amount + tax
        if self.balance < total_amount:
            print ( "Nedovoljno sredstava na kartici" )
        else:
            self.balance -= total_amount
            print (
                f"Uspesno placanje u iznosu od {amount} dinara uz porez od {tax} dinara. Novo stanje: {self.balance} dinara." )


visa_card = Visa(123456, 1000)
visa_card.pay(500)
master_card = Master(987654, 2000)
master_card.pay(1000)



















