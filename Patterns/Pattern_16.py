# https://www.naukri.com/code360/problems/alpha-ramp_6581888?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC

def alphaRamp():
    n = int(input("Enter"))
    for i in range(1,n+1):
        for j in range(i):
            print(chr(ord('A')+i-1), end = " ")
        print()     


alphaRamp()


# Input: ‘N’ = 3

# Output: 
# A
# B B
# C C C
