# Taking the input, of how many words are there
n = int(input())

# iterating through each word
for i in range(n):
    words = input()
    
    # checking the length of the word
    if len(words) > 10:
        
        # Checking the length of the word between first and last character
        between_first_and_last = words[1:-1]
        
        # converting length to string
        converting_to_string = str(len(between_first_and_last))
        
        # forming the abbreviated word
        words_abbreviation = words[0] + converting_to_string + words[-1]
        
        # printing the abbreviated word
        print(words_abbreviation)
    
    else:
        
        # printing the word as it is
        print(words)