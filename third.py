def solve():
    s = input()
    t = input()
    k = int(input())

    good_char = {}
    for ch in t:
        good_char[ch] = good_char.get(ch, 0) + 1

    strings = []
    last = ""

    for i in range(len(s)):
        if s[i] not in good_char:
            if last:
                strings.append(last)
            last = ""
        else:
            last += s[i]

    if last:
        strings.append(last)

    for i in range(len(strings) - 1, -1, -1):
        s = strings[i]
        n = len(s)
        has = {}

        for l in range(n - 1, -1, -1):
            has[s[l]] = has.get(s[l], 0) + 1

            if l + k <= n - 1:
                has[s[l + k]] -= 1
                if has[s[l + k]] == 0:
                    del has[s[l + k]]

            if len(has) == len(good_char):
                print(s[l:min(l + k, n)])
                return

    print(-1)


if __name__ == "__main__":
    solve()
