from entities.budget_item import BudgetItem

from repositories.budget_item_repository import (
    budget_item_repository as default_budget_item_repository
)

class BudgetService:
    
    def __init__(
        self,
        budget_item_repository=default_budget_item_repository
    ):

        self._budget_item_repository = budget_item_repository
        self.incomes = 0
        self.expenses = 0
    
    def create_budget_item (self, id, sum, type):
        budget_item = self._budget_item_repository.create(BudgetItem(id, sum, type))
        
        return budget_item
    
    def get_next_id(self):
        next_id = self._budget_item_repository.find_next_id()
        
        return next_id
    
    def get_incomes(self):
        incomes = self._budget_item_repository.get_incomes()
        if incomes == None:
            incomes = 0
        
        return incomes
    
    def get_expenses(self):
        expenses = self._budget_item_repository.get_expenses()
        if expenses == None:
            expenses = 0
        
        return expenses
    
    def get_budget(self):
        incomes = self._budget_item_repository.get_incomes()
        expenses = self._budget_item_repository.get_expenses()
        if incomes == None:
            incomes = 0
        if expenses == None:
            expenses = 0
        budget = round(incomes - expenses, 2)
        
        return budget
    
budget_service = BudgetService()