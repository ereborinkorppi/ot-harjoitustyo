from entities.budget_item import BudgetItem

from repositories.budget_item_repository import (
    budget_item_repository as default_budget_item_repository
)

class BudgetService:
    """Sovelluslogiikasta huolehtiva luokka."""

    def __init__(
        self,
        budget_item_repository=default_budget_item_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikkaa hoitavan palvelun.

        Args:
            budget_item_repository:
                Vapaaehtoinen, oletuksena BudetItemRepository-olio.
                Olio, joka sisältää BudgetItemRepository-luokkaa vastaavat metodit.
        """
        self._budget_item_repository = budget_item_repository
        self.incomes = 0
        self.expenses = 0

    def create_budget_item (self, item_id, amount, item_type, desc):
        """Luo budjettimerkinnän.

        Args:
            item_id: int-arvo, yksilöi budjettimerkinnän.
            amount: float-arvo, tulon tai menon määrä.
            item_type: int-arvo, joka kertoo onko kyseessä tulo tai meno.
            desc: merkkijonoarvo, joka kuvaa mistä merkinnässä on kyse.

        Returns:
            Luotu budjettimerkintä BudgetItem-olion muodossa.
        """

        budget_item = self._budget_item_repository.create(
            BudgetItem(item_id, amount, item_type, desc)
        )

        return budget_item

    def get_next_id(self):
        """Etsii seuraavan vapaan id:n

        Returns:
            int-arvossa oleva next_id.
        """

        next_id = self._budget_item_repository.find_next_id()

        return next_id

    def get_budget(self):
        """Laskee mitä viivan alle jää, kun tuloista vähennetään menot

        Returns:
            float-arvossa oleva budget.
        """

        incomes = self._budget_item_repository.get_incomes_or_expenses(1)
        expenses = self._budget_item_repository.get_incomes_or_expenses(2)
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
            BudgetItem-oliota sisältävä lista kaikista tuloiksi tai
            menoiksi kirjatuista budjetti-itemeistä.
        """

        return self._budget_item_repository.find_all_budget_items(item_type)
    
    def get_incomes_or_expenses(self, item_type):
        """Hakee kaikki tuloiksi tai menoiksi merkityt budjettimerkinnät summattuna

        Args:
            item_type: Budjetti-itemin tyyppi eli tulo tai meno.

        Returns:
            float-arvossa oleva tulojen tai menojen summa.
        """

        incomes_expenses = round(self._budget_item_repository.get_incomes_or_expenses(item_type),2)
        if incomes_expenses is None:
            incomes_expenses = 0

        return incomes_expenses

budget_service = BudgetService()
