'''def schedule(d, n, v, i):
    if i + 1 >= len(a):
        return v
    if n >= len(a):
        if i < len(a):
            return schedule([a[i]], i + 1, v, i + 1)
    s0 = 0
    for s in range(n, len(a)):
        if not d:
            s0 = s0 + b[i]
            d.append(a[i])
        elif a[s][0] >= d[len(d) - 1][1]:
            s0 = s0 + b[s]
            d.append(a[s])
    if s == len(a) - 1:
        if s0 > v:
            v = s0
        return schedule([], n + 1, v, i)


a = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
b = [5, 6, 5, 4, 11, 2]
v = schedule([], 0, 0, 0)
print(v)'''

s1="abcd"
s2="axbd"
s=""
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s1)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])

u=len(s1)
v=len(s2)
if(s1[u-1]==s2[v-1]):
    s=s+s1[u-1]
    u=u-1
    v=v-1
else:
    if(m[u][v]):



