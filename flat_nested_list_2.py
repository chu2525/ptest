def flatten(nested_list):
    if len(nested_list) == 0:
        return nested_list
    if isinstance(nested_list[0], list):
        return flatten(nested_list[0] + flatten(nested_list[1:]))
    return nested_list[:1] + flatten(nested_list[1:])

print(flatten([[1,2],3,[4,[5,6,[7,8]]],9]))
