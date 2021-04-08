def space(n):
    for i in range(n):
        print(" ",end = "")


def print_star1():
    for i in range(10):
        print("* ",end = "")
    print()

def print_star2():
    print("*",end = "")
    for i in range(17):
        print(" ",end = "")
    print("*")

def main():
    space(10-1)
    print_star1()
    for i in range(8):
        space(8-i)
        print_star2()
    print_star1()


main()
        

"""

         * * * * * * * * * * 
        *                 *
       *                 *
      *                 *
     *                 *
    *                 *
   *                 *
  *                 *
 *                 *
* * * * * * * * * * 

"""