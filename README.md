# pectus-finance

### install all the dependencises 
``` pip install -r requirements.txt ```

### Run the flask server
``` python app.py ```

### Endpoint
``` http://127.0.0.1:5000/expense ```

#### Query Params
```
# aggregates
 .../expense?aggregates_by=<any_field_name>
   #sort
   .../expense?sort=departments&order=desc
   # fields/attributes
   .../expanses?amount[gte]=1400&member_name=Sam
   # return a sparse fieldset 
   /expanses?fields=departments,member_name,amount)
```
