def foo():
    print("foo")

def bar():
    print("bar")

def main():
    print("I am in main")


def main2():
    foo()
    main()
    bar()

# Start print message

print("Hello")    
main() #invoking main function
print("Bye")
main2()