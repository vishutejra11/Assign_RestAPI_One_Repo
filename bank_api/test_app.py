import unittest
from app import app, db, Bank, Branch

class BankApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        # Add test data
        self.bank = Bank(name="Test Bank")
        db.session.add(self.bank)
        db.session.commit()
        
        self.branch = Branch(branch="Test Branch", ifsc="TEST1234", bank=self.bank)
        db.session.add(self.branch)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_banks(self):
        response = self.app.get('/banks')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"id":1,"name":"Test Bank"}', response.data)

    def test_get_branches(self):
        response = self.app.get(f'/banks/{self.bank.id}/branches')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"branch":"Test Branch","ifsc":"TEST1234"}', response.data)

    def test_get_branch(self):
        response = self.app.get(f'/branches/{self.branch.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"branch":"Test Branch","ifsc":"TEST1234","bank":{"id":1,"name":"Test Bank"}}', response.data)

if __name__ == '__main__':
    unittest.main()
