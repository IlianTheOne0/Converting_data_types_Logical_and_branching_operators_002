a, b = map(float, input('Enter the numbers to be compared separated by commas: ').split(','))

if a == b:
    print(f'Number {a} and number {b} are equal')
else:
    if a > b:
        print('Numbers in ascending order:', b, a)
    else:
        print('Numbers in ascending order:', a, b)