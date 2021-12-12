import unittest
from entities.budget_item import BudgetItem
from services.budget_service import BudgetService

class FakeBudgetItemRepository:
    def __init__(self, budget=None):
        self.budget = budget or []
    
    def create(self, budget_item):
        self.budget.append(budget_item)

        return budget_item
    
    def find_next_id(self):
        next_id = len(self.budget)
        
        return next_id
    
    def get_incomes(self):
        incomes = sum(budget_item.amount for budget_item in self.budget if budget_item.item_type==1)

        return incomes

    def get_expenses(self):
        expenses = sum(budget_item.amount for budget_item in self.budget if budget_item.item_type==2)

        return expenses
    
    def delete_all(self):
        self.budget = []

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(
            FakeBudgetItemRepository()
        )
        self.budget_service.create_budget_item(0, 500, 1, "palkka")
        self.budget_service.create_budget_item(0, 300, 2, "vuokra")
    
    def test_get_next_id(self):
        self.assertEqual(self.budget_service.get_next_id(), 2)

    def test_get_incomes(self):
        self.assertEqual(self.budget_service.get_incomes(), 500)

    def test_get_expenses(self):
        self.assertEqual(self.budget_service.get_expenses(), 300)

    def test_get_budget(self):
        incomes = self.budget_service.get_incomes()
        expenses = self.budget_service.get_expenses()
        budget = incomes - expenses
        self.assertEqual(budget, 200)