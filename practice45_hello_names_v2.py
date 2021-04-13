names = ["Rick","Pat","Nick","Mike"]
wishes = ["Good Morning","Good Afternoon","Good Evening","Good Night"]

def wish(x):
    y = 0
    while y < 4:
        print(f"{wishes[y]} {names[x]}.")
        y = y+1


def main():
    x = 0
    while x < 4:
        wish(x)
        x = x+1

main()        

