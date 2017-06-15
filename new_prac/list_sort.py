# Simple way to find MAX and MIN
def simple_list(x):
    list_min = min(x)
    list_max = max(x)
    return "The max value from the list is: {}\nThe min value from the list is: {}\n".format(list_max, list_min)

###############################################################
# Sort by my own algorithm to find MAX and MIN
def max_min_sort(x):
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
##############################################################
# Sort the whole list and print it
def simple_sort(x):
    x.sort()

##############################################################
def sort_list(x):
    new = []
    for i in range(len(x)):
        first = x[i]
        small = first
        for y in range(1, len(x)):
            second = x[y]
            big = second
            if first > second:
                small = second
            else:
                continue
        new.append(small)
    return new


x = [34, 54, 2, .99, 8.93, 20, 65, 22, 30, 47, 64.98, -100, 34, 65, 76.44, -88]

print(simple_list(x))
print(max_min_sort(x))
print(simple_sort(x))
print(sort_list(x))
