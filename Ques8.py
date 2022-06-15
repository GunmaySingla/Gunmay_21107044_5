#first we take 10 integers as outputs
a= int(input('Enter 1st integer: '))
b= int(input('Enter 2nd integer: '))
c= int(input('Enter 3rd integer: '))
d= int(input('Enter 4th integer: '))
e= int(input('Enter 5th integer: '))
f= int(input('Enter 6th integer: '))
g= int(input('Enter 7th integer: '))
h= int(input('Enter 8th integer: '))
i= int(input('Enter 9th integer: '))
j= int(input('Enter 10th integer: '))
#then we define them in a list
integer_list = [a,b,c,d,e,f,g,h,i,j]
#now we apply conditions for all the parts given in the question
print("positive numbers are : ")
for positive_numbers in integer_list:
    if positive_numbers>=0:
        print(positive_numbers,"  ",end="")
print("")
        
print('negative numbers are : ')
for negative_numbers in integer_list:
    if negative_numbers<0:
        print(negative_numbers,' ',end='')
print('')
        
print("positive numbers are : ")
for odd_numbers in integer_list:
    if odd_numbers%2!=0:
        print(odd_numbers,"  ",end="")
print("")

print("even numbers are : ")
for even_numbers in integer_list:
    if even_numbers%2==0:
        print(even_numbers,"  ",end="")
print("")

