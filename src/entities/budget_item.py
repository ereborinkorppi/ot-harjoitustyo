class BudgetItem:
    """Luokka, joka kuvaa yksittäistä budjettiriviä.

    Attributes:
        item_id: int-arvo, joka yksilöi budjettimerkinnän.
        amount: float-arvo, joka kuvaa tulon tai menon määrää.
        item_type: int-arvo, joka kertoo onko kyseessä tulo tai meno.
        desc: merkkijonoarvo, joka kuvaa mistä merkinnässä on kyse.
    """

    def __init__(self, item_id, amount, item_type, desc):
        """Luokan konstruktori, joka luo uuden budjettimerkinnän

        Args:
            item_id: int-arvo, yksilöi budjettimerkinnän.
            amount: float-arvo, tulon tai menon määrä.
            item_type: int-arvo, joka kertoo onko kyseessä tulo tai meno.
            desc: merkkijonoarvo, joka kuvaa mistä merkinnässä on kyse.
        """

        self.item_id = item_id
        self.amount = amount
        self.item_type = item_type
        self.desc = desc