num = int(input('enter any number'))

n1 = 0
n2 = 1
#fibonacci series is calculated by attition of two numbers
sum = 0

for i in range (0,num):
    #print(sum)

    #interchange the variables
    #the second number will beconsidered as the first value
    #sum will be considered as the second number
    n1 = n2
    n2 = sum #SUM IS STORED IN N2
    sum = n1 + n2
    print(sum)

# this line of code will print the fibonac series
