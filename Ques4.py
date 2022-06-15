n = 5
#this part is for the increasing lines till 5
#here we have used a nested for loop
#end= has been used to make the stars print in the same line istead of in the same line
for i in range(n):
    for j in range(i):
        print('* ',end='')
    print('')    
#this part is for the decresing lines from 5 to 1        
for i in range(n,0,-1):
    for j in range(i):
        print('* ',end='')
    print('')
    
          