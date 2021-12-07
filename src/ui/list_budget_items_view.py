from tkinter import ttk, constants
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
        heading.grid(row=0, column=0, columnspan=2, pady=5)
        incomes = ttk.Label(master=self._frame, text="Tulot:", font="Arial 12 underline")
        incomes.grid(row=1, column=0, pady=2)
        incomes_list = budget_service.get_budget_items(1)
        expenses_list = budget_service.get_budget_items(2)
        i = 2
        for x in range(len(incomes_list)):
            desc = incomes_list[x].desc
            amount = incomes_list[x].amount
            income_item_desc = ttk.Label(master=self._frame, text=desc)
            income_item_amount = ttk.Label(master=self._frame, text=amount)
            income_item_desc.grid (row=i, column=0)
            income_item_amount.grid (row=i, column=1)
            i = i+1
        expenses = ttk.Label(master=self._frame, text="Menot:", font="Arial 12 underline")
        expenses.grid(row=i, column=0, pady=2)
        i = i+1
        for x in range(len(expenses_list)):
            desc = expenses_list[x].desc
            amount = expenses_list[x].amount
            expense_item_desc = ttk.Label(master=self._frame, text=desc)
            expense_item_amount = ttk.Label(master=self._frame, text=amount)
            expense_item_desc.grid (row=i, column=0)
            expense_item_amount.grid (row=i, column=1)
            i = i+1

        button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_home
        )

        button.grid(row=i, column=0, columnspan=2, pady=5)