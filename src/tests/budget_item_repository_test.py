import unittest
from repositories.budget_item_repository import budget_item_repository
from entities.budget_item import BudgetItem

class TestBudgetItemRepository(unittest.TestCase):
    def setUp(self):
        budget_item_repository.delete_all()
        self.budget_item_income1 = BudgetItem(0, 500, 1, "tulo")
        self.budget_item_expense1 = BudgetItem(1, 200, 2, "meno")
        budget_item_repository.create(self.budget_item_income1)
        budget_item_repository.create(self.budget_item_expense1)
    
    def test_create(self):
        next_id = budget_item_repository.find_next_id()
        self.assertNotEqual(next_id, 0)

    def test_find_next_id(self):
        next_id = budget_item_repository.find_next_id()

        self.assertEqual(next_id, 2)
    
    def test_get_incomes(self):
        self.budget_item_income2 = BudgetItem(2, 100, 1, "palkka")
        budget_item_repository.create(self.budget_item_income2)
        self.assertEqual(budget_item_repository.get_incomes(), 600)
        
    def test_get_expenses(self):
        self.assertEqual(budget_item_repository.get_expenses(), 200)