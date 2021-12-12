from entities.budget_item import BudgetItem
from database_connection import get_database_connection

def get_budget_item_by_row(row):
    return BudgetItem(row['item_id'], row['amount'], row['item_type'], row['desc']) if row else None

class BudgetItemRepository:
    """Budjettimerkintöihin kohdistuvista tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Connection-olio tietokantayhteyttä varten.
        """

        self._connection = connection

    def create(self, budget_item):
        """Tallentaa budjettimerkinnän tietokantaan.

        Args:
            budget_item: Tallennettava budjettimerkintä BudgetItem-oliona.

        Returns:
            Tallennettu budjettimerkinä BudgetItem-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into budget (item_id, amount, item_type, desc) values (?, ?, ?, ?)',
            (budget_item.item_id, budget_item.amount, budget_item.item_type, budget_item.desc)
        )

        self._connection.commit()

        return budget_item

    def find_next_id(self):
        """Hakee tietokannasta seuraavan vapaan id:n.

        Returns:
            int-arvossa seuraava vapaa id.
        """

        cursor = self._connection.cursor()

        cursor.execute('select count(item_id) from budget')

        next_id = cursor.fetchone()[0]

        return next_id

    def get_incomes(self):
        """Hakee tietokannasta summattuna kaikki tulot.

        Returns:
            float-arvossa kaikki tulot summattuna.
        """

        cursor = self._connection.cursor()

        cursor.execute('select sum(amount) from budget where item_type = 1')

        incomes = cursor.fetchone()[0]

        return incomes

    def get_expenses(self):
        """Hakee tietokannasta summattuna kaikki menot.

        Returns:
            float-arvossa kaikki menot summattuna.
        """

        cursor = self._connection.cursor()

        cursor.execute('select sum(amount) from budget where item_type = 2')

        expenses = cursor.fetchone()[0]

        return expenses

    def delete_all(self):
        """Poistaa tietokannasta kaikkirivit.
        """

        cursor = self._connection.cursor()

        cursor.execute('delete from budget')

        self._connection.commit()

    def find_all_budget_items(self, item_type):
        """Palauttaa kaikki tulot tai menot.

        Args:
            item_type: Budjetti-itemin tyyppi eli tulo tai meno.

        Returns:
            Palauttaa listan BudgetItem-olioita.
        """

        cursor = self._connection.cursor()

        if item_type == 1:
            cursor.execute('select * from budget where item_type = 1')

        if item_type == 2:
            cursor.execute('select * from budget where item_type = 2')
    
        rows = cursor.fetchall()

        return list(map(get_budget_item_by_row, rows))


budget_item_repository = BudgetItemRepository(get_database_connection())