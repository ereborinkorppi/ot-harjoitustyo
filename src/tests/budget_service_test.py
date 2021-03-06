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
    
    def get_incomes_or_expenses(self, item_type):
        if item_type == 1:
            incomes_expenses = sum(budget_item.amount for budget_item in self.budget if budget_item.item_type==1)

        if item_type == 2:
            incomes_expenses = sum(budget_item.amount for budget_item in self.budget if budget_item.item_type==2)
        
        return incomes_expenses
    
    def delete_all(self):
        self.budget = []

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(
            FakeBudgetItemRepository()
        )
        self.budget_service.create_budget_item(0, 500, 1, "palkka")
        self.budget_service.create_budget_item(1, 300, 2, "vuokra")

    def test_create(self):
        self.budget_service.create_budget_item(self.budget_service.get_next_id(), 100, 2, "ravintola")
        self.assertEqual(self.budget_service.get_next_id(), 3)
    
    def test_get_next_id(self):
        self.assertEqual(self.budget_service.get_next_id(), 2)

    def test_get_incomes(self):
        self.assertEqual(self.budget_service.get_incomes_or_expenses(1), 500)

    def test_get_expenses(self):
        self.assertEqual(self.budget_service.get_incomes_or_expenses(2), 300)

    def test_get_budget(self):
        incomes = self.budget_service.get_incomes_or_expenses(1)
        expenses = self.budget_service.get_incomes_or_expenses(2)
        budget = incomes - expenses
        self.assertEqual(budget, 200)
