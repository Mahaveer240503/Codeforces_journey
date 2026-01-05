# this code counts how many participants advance to the next round

# Taking input for number of participants and the k-th position
n, k = map(int, input().split())

# Taking input for scores of n participants
*scores_of_n_participants, = map(int, input().split())

# Ensuring we only have scores for n participants
scores_of_n_participants = scores_of_n_participants[:n]

# Sorting the scores in descending order
scores_of_n_participants.sort(reverse=True)

# Finding the k-th score
kth_score = scores_of_n_participants[k-1]

# Counting how many participants have scores >= k-th score and > 0
count = 0

# Iterating through each participant's score
for i in scores_of_n_participants:
    
    # Checking if the score is greater than or equal to k-th score and greater than 0
    if i >= kth_score and i > 0:
        count += 1

# Printing the count of participants advancing to the next round
print(count)




