# https://www.naukri.com/code360/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION

def nBinaryTriangle():
    n = int(input("enter"))
    for i in range(1,n+1):
        if i%2==0:
            start = 0
        else:
            start = 1
        for j in range(i):
            print(start, end=" ")
            start = 1 - start
        print()

nBinaryTriangle()


