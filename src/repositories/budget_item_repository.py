from database_connection import get_database_connection

class BudgetItemRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, budget_item):

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into budget (id, sum, type, desc) values (?, ?, ?, ?)',
            (budget_item.id, budget_item.sum, budget_item.type, budget_item.desc)
        )

        self._connection.commit()

        return budget_item
        
    def find_next_id(self):
        cursor = self._connection.cursor()

        cursor.execute('select count(id) from budget')

        next_id = cursor.fetchone()[0]

        return next_id

    def get_incomes(self):
        cursor = self._connection.cursor()

        cursor.execute('select sum(sum) from budget where type = 1')

        incomes = cursor.fetchone()[0]

        return incomes

    def get_expenses(self):
        cursor = self._connection.cursor()

        cursor.execute('select sum(sum) from budget where type = 2')

        expenses = cursor.fetchone()[0]

        return expenses
    
    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute('delete from budget')

        self._connection.commit()

budget_item_repository = BudgetItemRepository(get_database_connection())