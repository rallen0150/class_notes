def adder(number_one, number_two, message="No Message Passed", happy=True):
    print(message)
    print(happy)
    return number_one + number_two

print(adder(9, 4, happy=False, message="DO MATH SON!",))

print(adder("Robbie", " likes programming!"))


def add(*args):
    return sum(args)

print(add(1, 2, 4, 5, 56, 90, 20, 32))

print(adder(*[9, 4]))

print(add(*range(1000)))

# Not a great idea to use *args and **kwargs
def beginners_luck(name, account_number, *args, birthday="tomorrow", **kwargs):
    print(name, "NAME")
    print(account_number, "ACCOUNT NUMBER")
    print(args)
    print(kwargs)
    return 1

print(beginners_luck("robbie", 14918938149, [1, 2, 3], 99, birthday="Today", lol="robbie"))
