from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint 

def calculate_total_per_invoices(products_string):
    customer_list = transform_products_to_list(products_string)
    #pprint(customer_list)
    return_dict = {}
    for item in customer_list:
        return_dict.setdefault(item[-2], {})
        return_dict[item[-2]].setdefault(item[0], 0)
        return_dict[item[-2]][item[0]] += round(int(item[3]) * float(item[-3]), 2)
    return return_dict

print(calculate_total_per_invoices(products_string))
# {
#     '17850': {  # Customer ID
#         '536365': 139.12,  # Total for Invoice ID #536365
#         '536366': 22.20,
#         '536372': 22.20,
#         '536373': 15.30,
#     },