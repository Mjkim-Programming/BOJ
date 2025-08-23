def custom_round(n):
    if round(n) > n:
        return round(n) - 1
    else:
        return round(n)
    
N = float(input())
print(custom_round(N))