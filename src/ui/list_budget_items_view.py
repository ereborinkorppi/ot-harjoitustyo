from tkinter import ttk, constants
from ScrollableFrame import *
from services.budget_service import budget_service

class ListBudgetItemsView:
    def __init__(self, root, handle_home):
        self._root = root
        self._handle_home = handle_home
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="Tulo- ja menoerittely", font="Arial 14 bold")
        incomes = ttk.Label(master=self._frame, text="Tulot:", font="Arial 12 underline")
        self.scrollable_incomes = ScrollableFrame(self._frame, orient=0, height=200, width=400)
        incomes_list = budget_service.get_budget_items(1)
        for x in range(len(incomes_list)):
            desc = incomes_list[x].desc
            amount = round(incomes_list[x].amount,2)
            income_item = ttk.Label(
                self.scrollable_incomes.frame,
                text=str(amount)+ "   " + desc
            ).pack(anchor=W)
        expenses = ttk.Label(master=self._frame, text="Menot:", font="Arial 12 underline")
        self.scrollable_expenses = ScrollableFrame(self._frame, orient=0, height=200, width=400)
        expenses_list = budget_service.get_budget_items(2)
        for x in range(len(expenses_list)):
            desc = expenses_list[x].desc
            amount = round(expenses_list[x].amount,2)
            expense_item = ttk.Label(
                self.scrollable_expenses.frame,
                text=str(amount)+ "   " + desc
            ).pack(anchor=W)

        button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_home
        )

        heading.grid(row=0, column=0, pady=5, columnspan=2)
        incomes.grid(row=1, column=0, pady=5)
        self.scrollable_incomes.grid(row=2, column=0, padx=5, columnspan=2)
        expenses.grid(row=3, column=0, pady=5)
        self.scrollable_expenses.grid(row=4, column=0, padx=5, columnspan=2)
        button.grid(row=5, column=0, pady=5, columnspan=2)
