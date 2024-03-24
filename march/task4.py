def luky(n):
    if len(n) % 2 != 0:
        return False
    s1 = sum(map(int, n[:len(n)//2]))
    s2 = sum(map(int, n[len(n)//2:]))
    return s1 == s2
print(luky("385926"))