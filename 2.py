nested_list = [
   ['a', 'b', 'c'],
   ['d', 'e', 'f', 'h', False],
   [1, 2, None],
]

# def recurse(nested_list, depth=1):
#     for i in nested_list:
#         #print(i)
#         if type(i) == list:
#             recurse(nested_list, depth+1)
#     print(i)
    #return i



def recurse(nested_list, depth=0):
    count = 0
    for i in nested_list:
        if isinstance(i, list):
            count += recurse(i)
        else:
            count += 1
            #recurse(nested_list, depth+1)
            print(count)
    return count
recurse(nested_list)

# for item in recurse(nested_list):
#    print(item)