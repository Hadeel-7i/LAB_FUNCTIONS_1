def number(num: int):
    ''' print pattern from the number 7 to 1 '''
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(i, end=" ")
        print()


number(7)
print(number.__doc__)
