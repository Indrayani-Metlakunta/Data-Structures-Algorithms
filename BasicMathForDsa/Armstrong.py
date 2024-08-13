# https://www.naukri.com/code360/problems/check-armstrong_589?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM


def checkArmstrong():
    n = int(input("Enter : "))
    num_digits = len(str(n))
    temp = n
    sum = 0
    while (n>0):
        last_digit = n%10
        sum = sum +  last_digit**num_digits
        n = n//10
    if(temp == sum):
        print("True") 

checkArmstrong()



# For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.
    