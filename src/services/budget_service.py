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

    def create_budget_item (self, item_id, amount, item_type, desc):
        budget_item = self._budget_item_repository.create(BudgetItem(item_id, amount, item_type, desc))

        return budget_item

    def get_next_id(self):
        next_id = self._budget_item_repository.find_next_id()

        return next_id

    def get_incomes(self):
        incomes = self._budget_item_repository.get_incomes()
        if incomes is None:
            incomes = 0

        return incomes

    def get_expenses(self):
        expenses = self._budget_item_repository.get_expenses()
        if expenses is None:
            expenses = 0

        return expenses

    def get_budget(self):
        incomes = self._budget_item_repository.get_incomes()
        expenses = self._budget_item_repository.get_expenses()
        if incomes is None:
            incomes = 0
        if expenses is None:
            expenses = 0
        budget = round(incomes - expenses, 2)

        return budget
    
    def get_budget_items(self, item_type):
        """Palauttaa kaikki lisätyt yksittäiset tulot tai menot.
        
        Args:
            item_type: Budjetti-itemin tyyppi eli tulo tai meno.

        Returns:
            BudgetItem-oliota sisältävä lista kaikista tuloiksi tai menoiksi kirjatuista budjetti-itemeistä.
        """
        return self._budget_item_repository.find_all_budget_items(item_type)

budget_service = BudgetService()