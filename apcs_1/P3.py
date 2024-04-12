#TLE
from bisect import bisect_left, bisect_right
tree = {}
n = int(input())
parent = [0 for i in range(n+1)]
for i in range(1, n+1):
    l = [int(i) for i in input().split()]
    if len(l) != 1:
        tree[i] = sorted(l[1::])
    else:
        tree[i] = [0]
    for j in l[1::]:
        parent[j] = i

root = parent[1::].index(0)+1
temp = 0
a = input()
for i in range(len(a)):
    i += temp
    if i >= len(a):
        break
    if a[i] == 'C':
        num = ''
        while i+1 != len(a) and a[i+1].isdigit():
            i += 1
            temp += 1
            num += a[i]
        num = int(num)
        if num > len(tree[root]):
            break
        root = tree[root][num-1]
    elif a[i] == 'P':
        if parent[root]:
            root = parent[root]
    elif a[i] == 'R':
        if parent[root] == 0 or bisect_right(tree[parent[root]], root) == len(tree[root]):
            break
        root = tree[parent[root]][bisect_right(tree[parent[root]], root)]
    elif a[i] == 'L':
        if parent[root] == 0 or bisect_left(tree[parent[root]], root)-1 < 0:
            break
        root = tree[parent[root]][bisect_left(tree[parent[root]], root)-1]
print(root)