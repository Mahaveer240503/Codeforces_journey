t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    left, right = 0, n-1
    
    while left < right and s[left] != s[right]:
        left += 1
        right -= 1
        
    if left > right:
        print(0)
    else:
        print(right - left +1)
        
        
