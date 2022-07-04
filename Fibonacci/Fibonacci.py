
num1 = int(input())
num2 = int(input())
next = num1 + num2
print(next)

###############

Fibonacci_list = []
# first two numbers
num1 = 0
num2 = 1
#add first two numbers to Fibonacci_list
Fibonacci_list.append(num1)
Fibonacci_list.append(num2)

num3 = int(input())
for i in range(num3-2):
    res = num1 + num2
    Fibonacci_list.append(res)
    num1 = num2
    num2 = res

print(Fibonacci_list)

#####################

Fibonacci_list = []
# first two numbers
num1 = 0
num2 = 1
num3 = int(input())

def Fibonacci(num1,num2,num3):
    #add first two numbers to Fibonacci_list
    Fibonacci_list.append(num1)
    Fibonacci_list.append(num2)
    
    for i in range(num3-2):
        res = num1 + num2
        Fibonacci_list.append(res)
        num1 = num2
        num2 = res

Fibonacci(num1,num2,num3)
print(Fibonacci_list)

###########################

# first two numbers
num1 = int(input())
num2 = int(input())

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    if not(num1> 987):
        print(num1, end="  ")
        # add last two numbers to get next number
        res = num1 + num2
    
        # update values
        num1 = num2
        num2 = res
