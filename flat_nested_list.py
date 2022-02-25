import sys 
from itertools import chain

if len(sys.argv) < 1:
    print("Usage: flat_nested_link.py <nested list to be flatten")
    sys.exit(1)

nested_list = sys.argv[1]
flatted_list = []
for element in list(chain.from_iterable(nested_list)):
    if element == '[' or element == ']' or element == ',':
        list(chain.from_iterable(nested_list)).remove(element)
    else:
        flatted_list.append(element)
flatted_list = [int(i) for i in flatted_list]
print(flatted_list)


