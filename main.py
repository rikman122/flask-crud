from flask import Flask, request
from flask import jsonify
from config import config
from models import db
from models import Bill
from dotenv import load_dotenv
load_dotenv()                 

import os

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['production']
app = create_app(enviroment)

@app.route('/api/billing', methods=['POST'])
def create_bill():
    json = request.get_json(force=True)

    if json.get('type') is None or json.get('amount') is None or json.get('bill_date') is None:
        return jsonify({'message': 'Bad request'}), 400

    bill = Bill.create(json['type'], json['amount'], json['bill_date'])

    if bill is None:
        return jsonify({'message': 'Error creating bill'}), 500

    return jsonify({'bill': bill.json() })

@app.route('/api/billing', methods=['GET'])
def get_bills():
    bills = [ bill.json() for bill in Bill.query.all() ] 
    return jsonify({'bills': bills })

@app.route('/api/billing', methods=['DELETE'])
def delete_bill():
    json = request.get_json(force=True)

    if json.get('type') is None or json.get('bill_date') is None:
        return jsonify({'message': 'Bad request'}), 400

    bill = Bill.query.filter_by(type=json.get('type'), bill_date=json.get('bill_date')).first()
    if bill is None:
        return jsonify({'message': 'Bill does not exists'}), 404

    bill.delete()

    return jsonify({'bill': bill.json() })

if __name__ == '__main__':
    app.run(debug=False)