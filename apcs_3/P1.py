RNA = input()
flag = True
end = ['UAA','UAG','UGA']
n = 0
m = 0
count = 0
for i in range(len(RNA)-2):
    if RNA[i:i+3] == 'AUG':
        m = i
        count += 1
        break
for i in range(m+3, len(RNA)-2, 3):
    if RNA[i:i+3] == 'AUG':
        m = i
        count += 1
    elif RNA[i:i+3] in end:
        n = i
        count -= 1
        if not(count):
            break

print(len(RNA[m:n])//3)