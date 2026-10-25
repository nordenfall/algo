#алгоритм кнута морриса прата - поиск подстроки в строке 

g = "LSDFCVLILIALLISDFDSFDBLILILA"
s = "LILILA"

p = [0] * len(s)

j = 0
i = 1

while i < len(s):
    if s[i] == s[j]:
        p[i] = j + 1
        i += 1
        j += 1 
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1] 

print(p)

a = 0
b = 0
done = False

while a < len(g):
    if g[a] == s[b]:
        a += 1
        b += 1
        if b == len(s):
            print("нашли")
            done = True
            break
    else:
        if b > 0:
            b = p[b-1]
        else: 
            a += 1

if not done:
    print("не нашли")