from tkinter import Tk
from ui.gui import GUI


def main():
    window = Tk()
    window.title("Budjetointisovellus")

    gui = GUI(window)
    gui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
