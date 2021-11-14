from tkinter import ttk, constants

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
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="Lisää uusi")
        income = ttk.Radiobutton(master=self._frame, text="Tulo")
        expense = ttk.Radiobutton(master=self._frame, text="Meno")
        amount_entry = ttk.Entry(master=self._frame)
        amount_label = ttk.Label(master=self._frame, text="Summa")

        button = ttk.Button(
            master=self._frame,
            text="Lisää uusi",
            command=self._handle_home
        )

        heading.grid(row=0, column=0)
        income.grid(row=1, column=0)
        expense.grid(row=1, column=1)
        amount_entry.grid(row=2, column=0)
        amount_label.grid(row=2, column=1)
        button.grid(row=3, column=0)
