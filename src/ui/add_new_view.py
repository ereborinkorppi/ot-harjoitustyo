from tkinter import ttk, constants, IntVar
from tkinter import messagebox
from services.budget_service import budget_service

class AddNewView:
    def __init__(self, root, handle_home):
        self._root = root
        self._handle_home = handle_home
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def new_budget_item(self, amount_entry, var, desc_entry):
        try:
            self.amount = float(amount_entry)
            if self.amount > 0:
                item_id = budget_service.get_next_id()
                if desc_entry:
                    if var == 1:
                        messagebox.showinfo("Vahvistus", str(self.amount) + " lisätty tuloihin.")
                        budget_service.create_budget_item(item_id, self.amount, var, desc_entry)
                    if var == 2:
                        messagebox.showinfo("Vahvistus", str(self.amount) + " lisätty menoihin.")
                        budget_service.create_budget_item(item_id, self.amount, var, desc_entry)
                else:
                    messagebox.showerror("Virhe!", "Kuvaus ei voi olla tyhjä.")
            else:
                messagebox.showerror("Virhe!", "Summan on oltava suurempi kuin 0.")
        except ValueError:
            messagebox.showerror("Virhe!", "Syötä summa numeroina (esim. 1500 tai 12.5)")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="Lisää uusi:", font="Arial 14 bold")
        var = IntVar()
        income = ttk.Radiobutton(master=self._frame, text="Tulo", variable=var, value=1)
        expense = ttk.Radiobutton(master=self._frame, text="Meno", variable=var, value=2)
        var.set(1)
        amount_entry = ttk.Entry(master=self._frame, text="0")
        amount_label = ttk.Label(master=self._frame, text="Summa")
        desc_entry = ttk.Entry(master=self._frame, text="1")
        desc_label = ttk.Label(master=self._frame, text="Kuvaus")

        button1 = ttk.Button(
            master=self._frame,
            text="Lisää uusi",
            command=lambda: [self.new_budget_item(amount_entry.get(), var.get(), desc_entry.get()),
                             amount_entry.delete(0, 'end'), desc_entry.delete(0, 'end')]
        )
        button2 = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_home
        )

        heading.grid(row=0, column=0, pady=5)
        income.grid(row=1, column=0)
        expense.grid(row=1, column=1)
        amount_entry.grid(row=2, column=0)
        amount_label.grid(row=2, column=1)
        desc_entry.grid(row=3, column=0)
        desc_label.grid(row=3, column=1)
        button1.grid(row=4, column=0, pady=5)
        button2.grid(row=4, column=1, pady=5)
