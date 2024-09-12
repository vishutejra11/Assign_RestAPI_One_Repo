from bank_api import app, db
from bank_api.models import Bank, Branch
from flask import jsonify

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify([{'id': bank.id, 'name': bank.name} for bank in banks])

@app.route('/banks/<int:bank_id>/branches', methods=['GET'])
def get_branches(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    branches = Branch.query.filter_by(bank_id=bank_id).all()
    return jsonify([{'branch': branch.branch, 'ifsc': branch.ifsc} for branch in branches])

@app.route('/branches/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    branch = Branch.query.get_or_404(branch_id)
    return jsonify({
        'branch': branch.branch,
        'ifsc': branch.ifsc,
        'bank': {'id': branch.bank.id, 'name': branch.bank.name}
    })

if __name__ == '__main__':
    app.run(debug=True)
