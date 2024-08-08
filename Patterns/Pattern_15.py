# https://www.naukri.com/code360/problems/reverse-letter-triangle_6581906?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION

def nLetterTriangle():
    n = int(input("Enter"))
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(chr(ord('A')+j),end=" ")    
        print()

nLetterTriangle()


# Input: ‘N’ = 3

# Output: 

# A B C
# A B
# A
