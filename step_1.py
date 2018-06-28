from data import products_string
from pprint import pprint 
def transform_products_to_list(products_string):
    string_list = products_string.split('\n')
    new_string_list = [x for x in string_list if x != '']
    final_list = []
    for i in range(len(new_string_list)):
        final_list.append(new_string_list[i].split(','))
    return final_list
pprint(transform_products_to_list(products_string))
