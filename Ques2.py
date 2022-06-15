num = int(input('Divisor:'))
range_1 = int(input('Lower limit of range:'))
range_2 = int(input('Upper limit of range:'))


i = range_1
while i < range_2:
    if i%num == 0:
        print(i)
    else:
        print()
    i+=1
    

    