# https://www.geeksforgeeks.org/problems/right-triangle/1

def pattern_2():
    N = int(input("Enter: "))
    for i in range(N):
        for j in range(i):
            print("*", end = " ")
        print()
pattern_2()    
# o/p:
# *
# * *
# * * *
# * * * *