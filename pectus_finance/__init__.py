from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from pectus_finance.expense.view import ExpenseList, ExpenDetails 
# from pectus_finance.expense.models import Expense

app = Flask(__name__, instance_relative_config=True)
marshmallow = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pectusFinance.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) 
router = Api(app) 

from pectus_finance.expense import view, models


