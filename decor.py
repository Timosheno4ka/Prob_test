def simple_decore(fn):
    print("Start function")
    fn()
    print("Stop function")


@simple_decore
def first_test():
    print("Test functiom 1")

@simple_decore
def second_test():
    print("Test functiom 2")



# simple_decore(first_test)
# simple_decore(second_test)