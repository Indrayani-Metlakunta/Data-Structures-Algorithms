# https://www.naukri.com/code360/problems/increasing-letter-triangle_6581897?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC


def nLetterTriangle():
    n = int(input("Enter"))
    for i in range(1,n+1):
        for j in range(i):
            print(chr(ord('A')+j), end=" ")
        print()    
nLetterTriangle()


# op : 
# Enter3
# A
# A B
# A B C