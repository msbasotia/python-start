import sys
numbers = [23,45,67,1,43,19,34]

print("-----print1------")    

for i in numbers: # advantage is that you don't have to declare the size of list
    print(i)

print("-----print2------")    

for i in range(len(numbers)):
    print(f"{i}. {numbers[i]}")



print("----sum_avg all-------")        

sum = 0
for i in range(len(numbers)):
    sum = sum + numbers[i]

avg = sum / len(numbers)
print(f"sum of {numbers} = {sum}")    
print(f"avg of {numbers} = {avg}")    



print("----max_min-------")        

min_n = sys.maxsize
max_n = -sys.maxsize

for i in range(len(numbers)):
    if numbers[i] > max_n:
        max_n = numbers[i]
    if numbers[i] < min_n:
        min_n = numbers[i]
print(f"Maximum of {numbers} = {max_n}")
print(f"Minimum of {numbers} = {min_n}")