# [1,2,3,4,1,2,3,1,2]-> [[1,2,3,4],[1,2,3],[1,2]]
# [2,3,1,3,4,3,2]
'''def skip(ls):
    s = []
    a = []
    for i in ls:
        if (len(ls) == 0):
            return d
        if(i not in s):
            s.append(i)
        else:
            a.append(i)
    d.append(s)
    if(len(a) != 0):
        skip(a)
    return d
ls=list(map(int,input().split()))
a = []
d = []
skip(ls)
print(d)

a = [2, 3, 1, 3, 4, 3, 2]
m = []
c = 0
while (c != len(a)):
    r = []
    for i in range(len(a)):
        if (not str(a[i]).isalpha()):
            if (a[i] not in r):
                c = c + 1
                r.append(a[i])
                a[i] = "A"
    m.append(r)
print(m)

s = input()
ls = []
for i in s:
    if (i not in ls and i != " " and i.isalpha() and i.isalnum() and i.islower()):
        ls.append(i)
    else:
        continue
print("True") if len(ls) == 26 else print("False")
'''

s = input()
d = set()
n = 0
for i in s:
    if(i not in d):
        d.add(i)
    else:
        print(len(d))
        d = set()
    n = n + 1
print(len(d),n)
m = 0
mini = 0
maxi = 0
n = 0
i = 0
j = 0
while(i < len(s)):
    j = i + 1
    count = 1
    while(j < len(s)):
        if(s[j] == s[i]):
            i = s.index(s[j]) - 1
            print(i,j)
            break
        if (count > m):
            m = count
            count = 0
        else:
            count = count + 1
            j = j + 1
        if(count > m):
            m = count
            mini = i
            maxi = j
            count = 0
        n = n + 1
    i = i + 1
print(m + 1, mini , maxi,n)





