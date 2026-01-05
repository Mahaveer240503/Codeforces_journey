n = int(input())
cards = list(map(int, input().split()))

left, right = 0, n-1
sereja, dima = 0, 0
turn = 0

while left <= right:
    if cards[left] > cards[right]:
        taken = cards[left]
        left = left + 1
    else:
        taken = cards[right]
        right -= 1
        
    if turn % 2 == 0:
        sereja += taken
    else:
        dima += taken
    
    turn += 1
    
print(sereja, dima)


