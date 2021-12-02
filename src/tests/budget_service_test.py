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
    
    def delete_all(self):
        self.budget = []

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(
            FakeBudgetItemRepository()
        )
        self.budget_service.create_budget_item(0, 500, 1, "palkka")
    
    def test_get_next_id(self):
        self.assertEqual(self.budget_service.get_next_id(), 1)
        
    