def tabs(n):
    for i in range(n):
        print(" ",end = "")


def print_line(n):
    for i in range(n):
        print(f"*",end = "")
    print()




def main():
    for i in range(10):
        tabs(10-i-1)
        print_line(i+1)


main()


""" 

         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********

"""