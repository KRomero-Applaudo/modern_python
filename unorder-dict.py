from collections import ChainMap

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print('%s: %s' % (key, value))

print('-'*20)

my_dict.update({
    'd': 4,
    'e': 5
})

for key, value in my_dict.items():
    print('%s: %s' % (key, value))

# Union operator beteen dicts
print('-'*20)

first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'d': 4, 'e': 5, 'c': 4}
third_dict = {'f': 6}

third_dict.update(second_dict)
chain_result = ChainMap(first_dict, second_dict)

print(third_dict)
print(chain_result['a'])

union_result = first_dict | second_dict

print(union_result)

print('-'*20)

a = 1
b = 3

match a, b:
    case 1:
        print("I'm a int")
    case (c, d):
        print("i'm a tuple")
    case _:
        print("I'm a defualt")
