from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False) 
    amount = db.Column(db.Float, nullable=False) 
    bill_date = db.Column(db.Date(), nullable=False)

    @classmethod
    def create(cls, type, amount, bill_date):
            bill = Bill(type=type, amount=amount, bill_date=bill_date)
            return bill.save()

    def save(self):
            try:
                    db.session.add(self)
                    db.session.commit()

                    return self
            except:
                    return None
    
    def json(self):
        return {
            'id': self.id,
            'type': self.type,
            'amount': self.amount,
            'bill_date': self.bill_date
        }
    
    def delete(self):
        try:
                db.session.delete(self)
                db.session.commit()

                return True
        except:
                return False