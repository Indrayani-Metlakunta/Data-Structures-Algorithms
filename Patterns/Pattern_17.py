# https://www.naukri.com/code360/problems/alpha-hill_6581921?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION

def alphaHill():
    n = int(input("Enter:"))
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end=" ")
        
        # Print ascending part of the letters
        for j in range(i + 1):
            print(chr(ord('A') + j), end=" ")
        
        # Print descending part of the letters
        for j in range(i - 1, -1, -1):
            print(chr(ord('A') + j), end=" ")
        
        print()

alphaHill()

# op:
# Input: ‘N’ = 3

# Output: 
#     A
#   A B A
# A B C B A


