def dragon_power(N):
    if N <= 4:
        return N
    power = 1
    while N > 4:
        power *= 3
        N -= 3
    power *= N
    return power

N = int(input())
print(dragon_power(N))