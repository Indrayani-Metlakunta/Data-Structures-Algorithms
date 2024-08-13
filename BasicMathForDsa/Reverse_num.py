def genReverse():
    n = int(input("Enter:"))
    reverse_num = 0
    while n > 0:
        last_digit = n % 10
        reverse_num = (10 * reverse_num) + last_digit
        n = n // 10
    print(reverse_num) 

genReverse()