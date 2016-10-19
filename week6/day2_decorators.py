
def function_caller(func):
    print("IM IN YOUR DECORATOR HAXING YOUR FUNC LOL")
    return func


@function_caller
def remote_control():
    print("I love lamp")
    return 0

remote_control()

# function_caller(remote_control)
