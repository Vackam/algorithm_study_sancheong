def GCD(a : int, b : int) :
    c = a%b 
    if (c == 0) :
        return b 
    else:
        return GCD(b, c)

N , M = map(int, input().split())

a = GCD(N, M)
print(a)