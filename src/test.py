import requests


data = {"orderId": "unique_order_id",
 "items": [
    {"sku": "0c2b963238207ed10db93fe5281381af", "count": 1, "size1": "5.1", "size2": "2.2", "size3": "5.3",
     "weight": "7.34", "type": ["2"]},
    {"sku": "aa15f9ac3ee5540e0fc8ddb7d97ec835", "count": 3, "size1": "4", "size2": "5.23", "size3": "6.2",
     "weight": "7.45", "type": ["8", "9", "10"]},
    {"sku": "9cc11c010b6d370b332cc178620f6e6e", "count": 2, "size1": "11", "size2": "12.5", "size3": "13.3",
     "weight": "14.2", "type": ["15", "16"]}
   ]
}

r = requests.get("http://localhost:8000/pack", json=data)

print(r.json())

