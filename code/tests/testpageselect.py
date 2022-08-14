import sys
import unittest
sys.path.append('.')
from pagepicker.picker import page_picker
from pagepicker.abcpage import IPage

class TestPicker(unittest.TestCase):
    def test_selection(self):
        page = page_picker()
        self.assertIsInstance(page, IPage)
