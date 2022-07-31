#imports 
import json
from flask import jsonify, request
from flask_restful import Resource
from pectus_finance.utils.query_parser import query_parser
from pectus_finance import router, db
from pectus_finance.expense.models import Expense
from sqlalchemy.sql import func
from sqlalchemy import desc


class ExpenseList(Resource):
  
    def get(self):
        
        query_dict = request.args.to_dict()
        try:
                
            if "aggregates_by" in query_dict.keys():
                agg = db.session.query(eval(f"Expense.{query_dict.get('aggregates_by')}"), func.sum(Expense.amount).label('total')).\
                group_by(eval(f"Expense.{query_dict.get('aggregates_by')}")).all()
                data = json.loads(json.dumps([row._asdict() for row in agg ]))
                return jsonify({'data': data})    
            
            queryset= query_parser("Expense",query_dict)
            if "sort" in query_dict.keys():
                queryset = db.session.query(*queryset).order_by(desc(eval(f"Expense.{query_dict.get('sort')}")))
                print(queryset)
                data = json.loads(json.dumps([row._asdict() for row in queryset ]))
                return jsonify({'data': data}) 

            queryset = db.session.query(*queryset)
            data = json.loads(json.dumps([row._asdict() for row in queryset ]))
            
        except Exception as e:
            return jsonify({"error": str(e)})
        return jsonify({'data': data})

router.add_resource(ExpenseList, '/expense')
