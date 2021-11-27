from tkinter import ttk, constants
from services.budget_service import budget_service

class HomeView:
    def __init__(self, root, handle_add_new):
        self._root = root
        self._handle_add_new = handle_add_new
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="Kotinäkymä")
        incomes = ttk.Label(master=self._frame, text="Tulot:")
        incomes_amount = ttk.Label(master=self._frame, text=budget_service.get_incomes())
        expenses = ttk.Label(master=self._frame, text="Menot:")
        expenses_amount = ttk.Label(master=self._frame, text=budget_service.get_expenses())
        budget = ttk.Label(master=self._frame, text="Budjettitilanne:")
        budget_amount = ttk.Label(master=self._frame, text=budget_service.get_budget())
        
        button = ttk.Button(
            master=self._frame,
            text="Lisää tulo/meno",
            command=self._handle_add_new
        )

        heading.grid(row=0, column=0)
        incomes.grid(row=1, column=0)
        incomes_amount.grid(row=1, column=1)
        expenses.grid(row=2, column=0)
        expenses_amount.grid(row=2, column=1)
        budget.grid(row=3, column=0)
        budget_amount.grid(row=3, column=1)
        button.grid(row=4, column=0)