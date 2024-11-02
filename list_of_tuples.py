def convert_to_dict(tuple_list):
    result={}
    for items in tuple_list:
        if len(items)==2:
            key,value=items
            result[key]=value
    return result
tuple_list=[("a",1),("b",2),("c",3),("d",2,1)]
print(convert_to_dict(tuple_list))