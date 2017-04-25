def tripsum(x, a):
    yes = 0
    y = len(a)
    if y < 3:
        yes = 0
    elif y == 3:
        if (a[0]+a[1]+a[2]) == x:
            yes += 1
    else:
        for first in range(0, y-2):
            first_num = a[first]
            for second in range(1, y-1):
                second_num = a[second]
                for third in range(2, y):
                    third_num = a[third]
                    if (first_num+second_num+third_num) == x:
                        yes += 1
                        break
    if yes > 0:
        return True
    else:
        return False


x = 1328
a = [75, 432, 153, 272, 269, 694, 886, 338, 312, 605, 678, 407, 769, 23, 414, 1, 543, 538, 39, 389, 356, 290, 648, 182, 94, 585, 988, 762, 494, 218, 502, 483,\
     448, 666, 754, 105, 85, 96, 526, 222, 965, 782, 873, 107, 657, 344, 594, 81, 81, 869, 412, 714, 969, 252, 217, 80, 769, 41, 532, 934, 780, 664, 260, 654, 937,\
     96, 366, 875, 721, 836, 681, 977, 456, 726, 72, 809, 560, 157, 603, 833, 906, 441, 376, 563, 886, 963, 81, 837, 798, 203, 509, 81, 341, 77, 59, 494, 741, 547,\
     475, 774, 98, 881,  336, 73, 401, 708, 956, 667, 142, 589, 482, 169, 316, 397, 226, 10, 13, 137, 456, 763, 44, 743, 22, 923, 513, 249, 19, 369, 718, 715, 651,\
     291, 336, 760, 170, 896, 304, 641, 980, 200, 106, 792, 662, 682, 653, 754, 34, 30, 988, 43, 254, 84, 421, 815, 719, 245, 64, 230, 653, 865, 770]
print(tripsum(x, a))