from pectus_finance.utils.constants import DB_OPREATION_MAP
from pectus_finance.expense.models import Expense
"""
This is a query parser for parsing the query params into meanigful SQL query it can be extended. Alsp we can use for different Database tables it for parsing 
"""
def query_parser(cls, query):
    fields = DB_OPREATION_MAP.get(cls)
    queryset = list()
    op = None
    if not query:
        return
    for k, v in query.items():
        if "[lte]" in k or "[gte]" in k :
            k = k.replace("[", "__").replace("]", "")
            op = k.split("__")[1]
            col = k.split("__")[0]
        if op == "lte":
            queryset.append((eval(".".join([str(cls), col])) <= v) )
        if op == "gte":
            queryset.append((eval(".".join([str(cls), col])) >= v ) )
        if k == "fields":
            fields = "".join(v).replace("(", "").replace(")","").split(",")
        if k in fields:
            queryset.append((eval(".".join([str(cls), k])) == v ) )
            

    for field in fields:
        queryset.append(eval((".".join([str(cls), field]))))
    return queryset

