from Tools import req
from Tools import dbconnect

rq = req.REQ()

def create_product():
    title = "TEST1 TITLE"
    price = 100
    input_data = {
        "name": title,
        "type": "simple",
        "regular_price": price,
        "description": "Pellentesque"}

    info = rq.post('products', input_data)
    print(info)

create_product()