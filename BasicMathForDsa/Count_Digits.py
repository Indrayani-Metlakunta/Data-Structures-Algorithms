# https://www.naukri.com/code360/problems/count-digits_8416387?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM


def countDigits():
    n = int(input("Enter"))
    c = 0
    temp = n 
    while(temp>0):
        last_digit = temp%10
        if last_digit!=0 and n%last_digit==0:
            c +=1
        temp = temp//10
    return c

countDigits()


    