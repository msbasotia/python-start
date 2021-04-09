def space(n):
    for i in range(n):
        print(" ", end = "")

def print_star_main():
    for i in range(10):
        print("* ", end = "")
    print()

def print_star_common():
    print("*", end = "")


def print_star_end():
    print("*")

def top_part():
    for i in range(4):
        print_star_common()
        space(1+2*i)
        print_star_common()
        space(15-2*(1+2*i))
        print_star_common()
        space(1+2*i)
        print_star_end()

def bottom_part():
    for i in range(4):
        print_star_common()
        space(1+2*(3-i))
        print_star_common()
        space(15-2*(1+2*(3-i)))
        print_star_common()
        space(1+2*(3-i))
        print_star_end()

def main():
    print_star_main()
    top_part()
    bottom_part()
    print_star_main()
    
main()


"""

* * * * * * * * * * 
* *             * *
*   *         *   *
*     *     *     *
*       * *       *
*       * *       *
*     *     *     *
*   *         *   *
* *             * *
* * * * * * * * * * 


"""