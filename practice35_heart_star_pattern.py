def space(n):
    for i in range(n+1):
        print(" ",end = "")


def print_star1(n):
    for i in range(n+1):
        print("* ",end = "")

def print_star2(n):
    for i in range(n+1):
        print("* ",end = "")
    print()
    

def top():
    for i in range(0,6,2):
        space(4-i)
        print_star1(i+5)
        space(9-2*i)
        print_star2(i+5)

def bottom():
    i = 2
    while i <= 22:
        space(i-2)
        print_star2(22-i)
        i = i+2

def main():
    top()
    bottom()

main()    


"""

     * * * * * *           * * * * * * 
   * * * * * * * *       * * * * * * * * 
 * * * * * * * * * *   * * * * * * * * * * 
 * * * * * * * * * * * * * * * * * * * * * 
   * * * * * * * * * * * * * * * * * * * 
     * * * * * * * * * * * * * * * * * 
       * * * * * * * * * * * * * * * 
         * * * * * * * * * * * * * 
           * * * * * * * * * * * 
             * * * * * * * * * 
               * * * * * * * 
                 * * * * * 
                   * * * 
                     * 

"""


# source of inspiration - https://codeforwin.org/2015/07/star-patterns-program-in-c.html