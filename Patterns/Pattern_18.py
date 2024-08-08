# https://www.naukri.com/code360/problems/alpha-triangle_6581429?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION

def alphaTriangle():
    n = int(input("Enter"))
    for i in range(n):
    # Print letters starting from 'A' + (n-i-1) up to 'E'
        for j in range(i + 1):
            print(chr(ord('A') + n - 1 - j), end=" ")
        print()
alphaTriangle()
        
# op : 
# Input: ‘N’ = 3

# Output: 
# C
# C B 
# C B A