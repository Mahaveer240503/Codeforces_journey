# taking the integer number as the input
n = int(input())

# initializing count 
count = 0

# iterating through each line which consist the value as 0 or 1 
for i in range(n): 
    
    # taking  the input in multiple variable which are friends
    petya, vasya, tonya = map(int, input().split())
    
    # applying logic whether that particular problem should be implemented or not
    if petya and vasya and tonya == 1 or petya and vasya == 1 or petya and tonya == 1 or vasya and tonya == 1:
        count += 1

# printing the number of problem for which the friends can give implementation.
print(count)
