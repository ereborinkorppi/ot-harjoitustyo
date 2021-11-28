import unittest
from repositories.budget_item_repository import budget_item_repository
from entities.budget_item import BudgetItem

class TestBudgetItemRepository(unittest.TestCase):
    def setUp(self):
        budget_item_repository.delete_all()
        self.budget_item_tulo = BudgetItem(0, 500, 1)
        self.budget_item_meno = BudgetItem(1, 200, 2)

    def test_create(self):
        budget_item_repository.create(self.budget_item_tulo)
        next_id = budget_item_repository.find_next_id()

        self.assertEqual(next_id, 1)
        self.assertEqual(budget_item_repository.get_incomes(), 500)