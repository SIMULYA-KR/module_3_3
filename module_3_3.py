def print_params(a=1, b="list", c=True):
    print(a, b, c)

print_params(b=25)
print_params(c=[1,2,3])


value_list = [1, 'dog', True]
value_dict = {"a": 'cat', 'b': False, 'c': 3}
print_params(*value_list)
print_params(**value_dict)


value_list_2 = [54, 234]
print_params(*value_list_2, 42)
