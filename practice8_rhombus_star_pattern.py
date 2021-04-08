
def space(n):
    for i in range(n):
        print(" ",end = "")


def print_star():
    for i in range(10):
        print("* ",end = "")
    print()


def main():
    for i in range(10,0,-1):
        space(i)
        print_star()

"""
earlier had used
def main():
    for i in range(10):
        space(10-i-1)
        print_star()

"""


main()

"""


         * * * * * * * * * * 
        * * * * * * * * * * 
       * * * * * * * * * * 
      * * * * * * * * * * 
     * * * * * * * * * * 
    * * * * * * * * * * 
   * * * * * * * * * * 
  * * * * * * * * * * 
 * * * * * * * * * * 
* * * * * * * * * * 

"""
