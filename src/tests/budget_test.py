import unittest
from services.budget import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()
        
    def test_budget_created(self):
        self.assertNotEqual(self.budget, None)
    
    def test_incomes_right(self):
        self.assertEqual(self.budget.incomes, 0)
        
    def test_expenses_right(self):
        self.assertEqual(self.budget.expenses, 0)
        
    def test_add_income(self):
        self.budget.add_income(300.5)
        self.assertEqual(self.budget.incomes, 300.5)
        
    def test_add_expense(self):
        self.budget.add_expense(112)
        self.assertEqual(self.budget.expenses, 112)
        
    