def space(n):
    for i in  range(n):
        print(" ",end = "")


def print_star():
    print("*")

def print_star1():
    print("*",end = "")

def print_star2():
    print("*")

def print_star3():
    for i in range(12):
        print("* ",end = "")
    print()


def main():
    print_star()
    for i in range(10):
        print_star1()
        space(1+2*i)
        print_star2()
    print_star3()

main()


""" 

*
* *
*   *
*     *
*       *
*         *
*           *
*             *
*               *
*                 *
*                   *
* * * * * * * * * * * * 

"""