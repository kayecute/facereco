import unittest
from unittest.mock import patch
from tkinter import Tk
from tkinter.messagebox import askokcancel

from app import on_closing

class TestOnClosing(unittest.TestCase):

    @patch('tkinter.messagebox.askokcancel', return_value=True)
    def test_on_closing_exit_true(self, mock_askokcancel):
        root = Tk()
        root.withdraw()  # Hide the root window
        on_closing()
        self.assertTrue(mock_askokcancel.called)
        root.destroy()

    @patch('tkinter.messagebox.askokcancel', return_value=False)
    def test_on_closing_exit_false(self, mock_askokcancel):
        root = Tk()
        root.withdraw()  # Hide the root window
        on_closing()
        self.assertTrue(mock_askokcancel.called)
        root.destroy()

if __name__ == '__main__':
    unittest.main()
