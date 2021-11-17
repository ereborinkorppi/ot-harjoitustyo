class Budget:
    
    def __init__(self):
        self.incomes = 0
        self.expenses = 0
    
    def add_income(self, income):
        if income > 0:
            self.incomes = self.incomes + income
            return income
        else:
            return "Tulon on oltava suurempi kuin 0"
    
    def get_incomes(self):
        return self.incomes
    
    def add_expense(self, expense):
        if expense > 0:
            self.expenses = self.expenses + expense
            return expense
        else:
            return "Menon on oltava suurempi kuin 0"
    
    def get_expenses(self):
        return self.expenses