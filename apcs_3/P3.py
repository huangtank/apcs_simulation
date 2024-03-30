n, k = map(int, input().split())
people = input().split()
R = len(people)-1
L = 0
count = 0
while k:
    while R != L:
        if int(people[R][1::]) >=65 or int(people[R][1::]) <= 12:
            break
        elif 35 <= int(people[R][1::]) <= 45 and people[R][0] == 'F':
            break
        else:
            R -= 1
    while R != L:
        if int(people[L][1::]) >=65 or int(people[L][1::]) <= 12:
            L += 1
        elif 35 <= int(people[R][1::]) <= 45 and people[R][0] == 'F':
            L += 1
        else:
            break
    if R == L:
        break
    people[L], people[R] = people[R], people[L]
    count += 1
    k -= 1
print(count)