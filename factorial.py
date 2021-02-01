import math

x = int(input("Please Enter a Number: "))
#recursion
def factorial (x):
    if x < 2:
        return 1
    else:
        return (x * factorial(x-1))

#iteration

def fact(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n

def factorial(p):
	if p == 0:
		return 1
	else:
		return p * factorial(p-1)

x = dict ()
def cachedfactorial(num):
	#if the number is in key we return to the value
	if num in x:
		return x[num]


	elif num == 0 or num == 1:
		#i assume that the number >=1 but just in case the number is zero
		return 1



	else:
		x[num] = num*cachedfactorial(num -1)
		return x[num]



print(factorial(x))
