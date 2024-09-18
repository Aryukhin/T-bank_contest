def f(s: str) -> list[int]:
    res = []

    for value in s.split(','):
        if '-' in value:
            a, b = map(int, value.split('-'))
            res.extend(range(a, b + 1))
        else:
            res.append(int(value))

    return res

s = input()
result = f(s)
print(*result)
