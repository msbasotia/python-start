def rev(n):
    i = n
    s = 0

    while i > 0:
        x = i % 10
        s = s * 10 + x 
        i = i // 10
    return s

def main():
    print(f"The reverse of 1234 is {rev(1234)}.")
    print(f"The reverse of 10450 is {rev(10450)}.")
    print(f"The reverse of 1940236 is {rev(1940236)}.")

main()    