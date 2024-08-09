def getStarPattern():
    n = int(input("Enter"))
    for i in range(n):
        for j in range(n):
            # Print star if we're on the first row, last row, first column, or last column
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end="")
            else:
                print(' ', end="")
        print()  # Move to the next line after each row

getStarPattern()

# ****
# *  *
# *  *
# ****
