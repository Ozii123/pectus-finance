from pectus_finance import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    departments = db.Column(db.String(50))
    project_name = db.Column(db.String(255))
    amount = db.Column(db.Float, nullable = False)
    date    = db.Column(db.String(255))
    member_name = db.Column(db.String(255))

    @classmethod
    def serialize(self):
        # return {"id": self.id, "departments": self.departments,
        #     "project_name":self.project_name, "amount":self.amount,
        #     "date": self.date,"member_name": self.member_name,}
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"{self.departments} {self.date}"