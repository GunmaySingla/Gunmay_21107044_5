#we take A as starting value 
st = 'A'
#here we use a nested for loop to print the triangle pattern
for i in range(int(input("Enter number of rows: "))):
    for j in range(i+1):
        
        print(st, end="")
        if st == 'Z':
            st = 'A'
        else:
            st = chr(ord(st) + 1)
    print()
