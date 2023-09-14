def fatorial(a):
    return 1 if a == 0 else a * fatorial(a-1)

print(fatorial(6))