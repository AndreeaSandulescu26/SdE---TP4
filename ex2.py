def nombresPrimes(n):
    ok = True

    if n<=1:
        ok = False

    for d in range(2,n):
        if n%d == 0:
            ok = False
            return ok

    return ok       

print("Il est prime") if nombresPrimes(11) else print("Il n'est pas prime")
