# https://www.naukri.com/code360/problems/symmetric-void_6581919?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC

def symmetry():
    n = int(input("Enter"))
    for i in range(n):
        for j in range(n-i):
            print('*', end=" ")
        for j in range(2*i):
            print(' ',end=" ")
        for j in range(n-i):
            print('*',end=" ")
        print()
    for i in range(n-1, -1, -1):
        for j in range(n-i):
            print('*', end=" ")
        for j in range(2*i):
            print(' ',end=" ")
        for j in range(n-i):
            print('*',end=" ")
        print()
symmetry()

# Input: ‘N’ = 3

# Output: 
# * * * * * * 
# * *     * * 
# *         * 
# *         * 
# * *     * * 
# * * * * * * 