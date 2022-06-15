#since herons formula uses square root we import math module
import math

side_1 = int(input('1st side:'))
side_2 = int(input('2nd side:'))
side_3 = int(input('3rd side:'))
#here we first confirm if the values input by the user make a triange

a = side_1
b = side_2
c = side_3
semi_peri = (a+b+c)/2

x = semi_peri-a
y = semi_peri-b
z = semi_peri-c
#then we use the herons formula to find the area

area_of_triangle = math.sqrt(semi_peri*x*y*z)

condition_1 = a+b>c
condition_2 = b+c>a
condition_3 = a+c>b

if condition_1 == True & condition_2 == True & condition_3 == True:
    print(area_of_triangle)
    
else:
    print('Enter valid values')
    