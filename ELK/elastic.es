

Get _cluster/health

#comment

GET products/_search
{
  "query": {
    "match": {
      "name": "Coffe Maker"
    }
  }
  
}


#remove  1 value
POST /products/_update/r0PMQ3oBo7FFO45vowdQ
{
    "script": {
        "source": "ctx._source.in_stock--"
    }
}

#remove  a specific value using a variable

POST /products/_update/r0PMQ3oBo7FFO45vowdQ
{
    "script": {
        "params":{"quantity": 5},
        "source": "ctx._source.in_stock -= params.quantity"
        

    }
}


#remove  a specific value using a variable and send a warning
POST /products/_update/r0PMQ3oBo7FFO45vowdQ
{
    "script": {
        "params":{"quantity": 5},
        "source": 
        """if (ctx._source.in_stock < 100) {
            ctx.op='warning less than 100 products in stock',
            ctx._source.in_stock -= params.quantity
            }
        
                ctx._source.in_stock -= params.quantity;


        """

    }
}



#asigning values
POST /products/_update/r0PMQ3oBo7FFO45vowdQ
{
    "script": {
        "source": "ctx._source.in_stock = 90"
    }
}


#asigning values
POST /products/_update/r0PMQ3oBo7FFO45vowdQ
{
    "script": {
        "params":{"quantity": 5},
        "source": "ctx._source.in_stock -= params.quantity"
        

    }
}


#----------
POST /products/_update/101
{
    "script": {
        "source": "ctx._source.in_stock++"
    },
    "upsert": {
        "name": "DVD",
        "price": 62,
        "in_stock": 12
    }
}

}

Get products/_doc/101

