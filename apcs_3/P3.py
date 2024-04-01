def check(st):
    sex = st[0]
    age = int(st[1::])
    return age <= 12 or age >= 65 or sex == "F" and 35 <= age <= 45

n, k = map(int, input().split())
a = input().split()
b = [i for i in range(n) if check(a[i])][:k]
print(sum([b[i]-i for i in range(k)]))