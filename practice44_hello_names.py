names = ["Rick","Pat","Nick","Mike"]
wishes = ["Good Morning","Good Afternoon","Good Evening","Good Night"]



x = 0
y = 0
while x < 4:
    while y < 4:
        print(f"{wishes[y]} {names[x]}.")
        y = y+1
    y = 0 # this is a must step
    x = x+1 