# 1. Set default value
# 2. refer to the argument by name, in this case, oder of passing argument does not matter
# 3. Use list *
# 4. Use dictionary **

def arguments_demo(arg1="default1", arg2="default2", *args, **kwargs):
    print("*********************************************")
    print(arg1)
    print(arg2)
    for count, arg in enumerate(args):
        print("{0} {1}".format(count, arg))
    for name, value in kwargs.items():
        print("{0} {1}".format(name, value))


if __name__ == "__main__":
    arguments_demo(arg2="value2", arg1="value1")
    arguments_demo(arg2="value2")
    arguments_demo(arg1="value1")
    arguments_demo("value1")
    arguments_demo("value1", "value2")
    arguments_demo("value1", "value2", "value11", "value12", "value13")
    arguments_demo("arg2", "arg1", "args1", "arg2", "args3", test_arg1="test1", test_arg2="test2", test_arg3="test3")