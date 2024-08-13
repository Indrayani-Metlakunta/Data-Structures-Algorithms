def palindrome():
    n = int(input("Enter:"))
    reverse_num = 0
    temp = n
    while n > 0:
        last_digit = n % 10
        reverse_num = (10 * reverse_num) + last_digit
        n = n // 10
    if(reverse_num == temp):
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome()