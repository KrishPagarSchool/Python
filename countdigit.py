number=int(input("Enter The Number : "))
count = 0
while number > 0:
    count=count+1
    number = number//10
print ("Number of digits in the given number is ", count)
