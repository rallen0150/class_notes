# Simple way
def sort_list(x):
    list_min = min(x)
    list_max = max(x)
    return "The max value from the list is: {}\nThe min value from the list is: {}\n".format(list_max, list_min)

###############################################################
# Sort by my own algorithm
def list_sort(x):
    list_min = 100
    list_max = 0
    for i in range(len(x)):
        first = x[i]
        for y in range(1, len(x)):
            second = x[y]
            if second > first:
                if second > list_max:
                    list_max = second
            elif second < first:
                if second < list_min:
                    list_min = second
            else:
                continue
    return list_max, list_min


x = [34, 54, 2, .99, 8.93, 20, 65, 22, 30, 47, 64.98, -100, 34, 65, 76.44, -88]

print(sort_list(x))
print(list_sort(x))
