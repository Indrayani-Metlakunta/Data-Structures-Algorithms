# https://www.naukri.com/code360/problems/increasing-number-triangle_6581893?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION

def nNumberTriangle():
    num = 1
    for i in range(1,n+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

nNumberTriangle()

# op:
# Input: ‘N’ = 3

# Output: 

# 1
# 2 3
# 4 5 6
