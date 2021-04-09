# def get_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * (i)
#     return fact


# def main():
#     print(f"2! = {get_fact(2)}")
#     print(f"3! = {get_fact(3)}")
#     print(f"5! = {get_fact(5)}")
#     print(f"7! = {get_fact(7)}")
#     print(f"8! = {get_fact(8)}")

# main()


# or we can write code like this as well

def get_fact(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * (i)
    return fact


def main():
    print(f"2! = {get_fact(2)}")
    print(f"3! = {get_fact(3)}")
    print(f"5! = {get_fact(5)}")
    print(f"7! = {get_fact(7)}")
    print(f"8! = {get_fact(8)}")

main()