def unique_list(list_of_items):
    x =[]
    for item in list_of_items:
        if item not in x:
            x.append(item)
    return x




lst = [1, 1, 1, 1, 2, 2, 2, 3, 2, 3, 3, 3, 5, 1, 5, 6]

print(unique_list(lst))
