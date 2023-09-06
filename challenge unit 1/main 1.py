
print ("*******************")
print ("FACTORIAL OF THE NUMBER")
print ("********************")
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num=int(input ("Enter the value ="))

if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
