import json
import urllib.request
import random
import xmlrpc.client

url = 'http://localhost:8017'
username = 'admin.localhost.com'
password = 'admin'
db = 'odoo17'


def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000)
    }
    headers = {
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers=headers)

    response = json.loads(urllib.request.urlopen(req).read().decode("UTF-8"))

    if response.get('error'):
        raise Exception(response["error"])
    return response["result"]

def call(url, service, method, *args):
    return json_rpc(f"{url}/jsonrpc", "call", {"service": service, "method": method, "args": args})


user_id = call(url, "common", "login", db, username, password)

print(user_id)

vals = {
    "name": "Property from JSON",
    "sales_id": 2
}

#create_property = call(url, "object", "execute", db, user_id, password, 'estate.property', 'create', vals)
#print(create_property)

read_property = call(url, "object", "execute", db, user_id, password, 'estate.property', 'read', [9])
print(read_property)

#python3.12 custom-addons/json_rpc.py     TO RUN IN TERMINAL