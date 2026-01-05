# Taking the input
n = int(input())

# inititalizing the variable X
X = 0

# Applying loop to iterate over each statements
for i in range(n):
    statement_with_operation = input()
    
    # Checking what in the statment, depending on that applying increasing or decreasing logic
    if statement_with_operation == "++X" or statement_with_operation == "X++":
        X += 1
        
    else:
        X -= 1
       
# printing final value of the X variable  
print(X)
    
    