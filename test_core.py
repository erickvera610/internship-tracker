import unittest
from core import connect,add
class Tests(unittest.TestCase):
    def test_persistence_and_sql_text(self):
        db=connect(':memory:'); add(db,"O'Reilly",'Software Intern')
        self.assertEqual(db.execute('SELECT company FROM applications').fetchone()[0],"O'Reilly")
    def test_invalid_status(self):
        with self.assertRaises(ValueError): add(connect(':memory:'),'A','B','unknown')
    def test_empty_company(self):
        with self.assertRaises(ValueError): add(connect(':memory:'),' ','B')
    def test_invalid_date(self):
        with self.assertRaises(ValueError): add(connect(':memory:'),'A','B',deadline='2027-02-30')
