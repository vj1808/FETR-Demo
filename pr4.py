#Calculator
print("----------------------------------------")
print("Calculator")
print("----------------------------------------")
a=input('Enter value 1 : ') # variable 1
b=input('Enter value 2 : ') # variable 2


add_a=float(a)+float(b) # addition of two numbers
sub_a=float(a)-float(b) # substraction of two numbers
mul_a=float(a)*float(b) # multiplication of two numbers
div_a=float(a)/float(b) # division of two numbers using type conversion


# Printing of result using command line print function
print ('addition of two number {0} and {1} is {2}'.format(a,b,add_a)) 
print ('sub of two number {0} and {1} is {2}'.format(a,b,sub_a))
print ('mul of two number {0} and {1} is {2}'.format(a,b,mul_a))
print ('Div of two number {0} and {1} is {2}'.format(a,b,div_a))

# Store answer in list
ans=[add_a,sub_a,mul_a,div_a]
print "List contents are"
print ans

# Display result using List
print ('addition of two number {0} and {1} is {2}'.format(a,b,ans[0])) 
print ('sub of two number {0} and {1} is {2}'.format(a,b,ans[1]))
print ('mul of two number {0} and {1} is {2}'.format(a,b,ans[2]))
print ('Div of two number {0} and {1} is {2}'.format(a,b,ans[3]))

