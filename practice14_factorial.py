def get_fact(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    print(f"{n}! = {fact}")

def main():
    get_fact(2)
    get_fact(3)
    get_fact(5)
    get_fact(10)
    get_fact(22)

main()