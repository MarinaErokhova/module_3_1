from itertools import filterfalse
from operator import truediv

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    tuple_1 = (len(string), string.upper(), string.lower())
    count_calls()
    print(tuple_1)

def is_contains(string, list_to_search):
    string = string.casefold()
    list_to_search = [s.casefold() for s in list_to_search]
    if string in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()

print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)