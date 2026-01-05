t = int(input())

for _ in range(t):
    start_rating, limit, change, rounds = map(int, input().split())
    contest = input().strip()

    current = start_rating
    total_rated = 0

    for c in contest:
        if c == '1':
            # div.1 contest → always rated
            total_rated += 1
            # play it safe by keeping rating as low as possible
            current = max(0, current - change)

        else:  # div.2 contest
            if current < limit:
                # rated for Vasya
                total_rated += 1
                # increase rating but stay just below the limit
                current = min(limit - 1, current + change)
            # else → unrated, so no change in rating

    print(total_rated)
