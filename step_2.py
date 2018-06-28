from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint 
def group_products_by_customer(products_string):
    list_items = transform_products_to_list(products_string)
    step_2_dict = {}
    for item in list_items:
        step_2_dict.setdefault(item[-2], [])
        step_2_dict[item[-2]].append(item)
    return step_2_dict

pprint(group_products_by_customer(products_string))
