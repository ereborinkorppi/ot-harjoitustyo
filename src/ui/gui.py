from tkinter import Tk
from ui.home_view import HomeView
from ui.add_new_view import AddNewView
from ui.list_budget_items_view import ListBudgetItemsView

class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_home_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_add_new(self):
        self._show_add_new_view()

    def _handle_home(self):
        self._show_home_view()

    def _handle_list_budget_items(self):
        self._show_list_budget_items_view()

    def _show_home_view(self):
        self._hide_current_view()

        self._current_view = HomeView(
            self._root,
            self._handle_add_new,
            self._handle_list_budget_items
        )

        self._current_view.pack()

    def _show_add_new_view(self):
        self._hide_current_view()

        self._current_view = AddNewView(
            self._root,
            self._handle_home
        )

        self._current_view.pack()

    def _show_list_budget_items_view(self):
        self._hide_current_view()

        self._current_view = ListBudgetItemsView(
            self._root,
            self._handle_home
        )

        self._current_view.pack()