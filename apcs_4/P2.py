#模擬
arr = [["A", "B", "C", "D", "E", "F", "G", "H"],
       ["I", "J", "K", "L", "M", "N", "O", "P"],
       ["Q", "R", "S", "T", "U", "V", "W", "X"],
       ["Y", "Z", "a", "b", "c", "d", "e", "f"],
       ["g", "h", "i", "j", "k", "l", "m", "n"],
       ["o", "p", "q", "r", "s", "t", "u", "v"],
       ["w", "x", "y", "z", "0", "1", "2", "3"],
       ["4", "5", "6", "7", "8", "9", "+", "/"]]
dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

for _ in range(int(input())):
    s, t, n = input().split()
    t, n = int(t), int(n)
    for i in range(8):
        if s in arr[i]:
            x, y = i, arr[i].index(s)
    D = 1
    for _ in range(n):
        add_x, add_y = dir[t%8]; t = (t%8)+1
        x = (x+(add_x*D))%8
        y = (y+(add_y*D))%8
        D += 1
    print(arr[x][y])