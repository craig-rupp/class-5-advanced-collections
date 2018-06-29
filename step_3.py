from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint 
def group_products_by_customer_and_invoice(products_string):
    doub_lists = transform_products_to_list(products_string)
    customer_invoice = {}
    for item in doub_lists:
        customer_invoice.setdefault(item[-2], {})
        customer_invoice[item[-2]].setdefault(item[0], [])
        customer_invoice[item[-2]][item[0]].append(item)
    return customer_invoice
pprint(group_products_by_customer_and_invoice(products_string))
