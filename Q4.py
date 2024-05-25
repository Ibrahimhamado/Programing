def main():
   bank_account=BanckAcount("0959738239","Ibrahim Hamado")
   bank_account.deposit(1000)
   bank_account.withdraw(500)
   print(bank_account.get_balance())
   saving_account=SavingAcount('0933838607','Ibrahim saving account', 0.01)
   saving_account.deposit(1000)
   saving_account.apply_interest()
   saving_account.__str__()
class BanckAcount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self._acount_number=account_number
        self._acount_holder=account_holder
        self._balance=balance
    def deposit(self , amount):
        self._balance=self._balance+amount
    def withdraw(self,amount):
        self._balance=self._balance-amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return (str(self._acount_holder )+str( self._acount_number )+str( self._balance))
class SavingAcount(BanckAcount):
     def __init__(self,account_number,accpunt_holder,interest_rate,balance=0.0):
         super().__init__(account_number,accpunt_holder,balance)
         self._interest_rate=interest_rate
     def apply_interest(self):
         interest = self._balance*self._interest_rate
         super().deposit(interest)
     def __str__(self):
         print(super().__str__() ,self._interest_rate)
main()