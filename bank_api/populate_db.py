from bank_api import app, db
from bank_api.models import Bank, Branch

# Ensure the app context is available
with app.app_context():
    # Create all tables
    db.create_all()

    # Add sample banks
    bank1 = Bank(name="Bank A")
    bank2 = Bank(name="Bank B")
    db.session.add(bank1)
    db.session.add(bank2)
    db.session.commit()

    # Add sample branches
    branch1 = Branch(branch="Branch 1", ifsc="IFSC1234", bank=bank1)
    branch2 = Branch(branch="Branch 2", ifsc="IFSC5678", bank=bank2)
    db.session.add(branch1)
    db.session.add(branch2)
    db.session.commit()

    print("Database populated with sample data.")
