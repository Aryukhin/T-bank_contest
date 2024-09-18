def recover_snow_data(length, data):
    if data[0] == -1:
        data[0] = 1

    for idx in range(1, length):
        if data[idx] == -1:
            data[idx] = data[idx - 1] + 1
        elif data[idx] <= data[idx - 1]:
            return "NO"
    for idx in range(length-1, 0, -1):
        data[idx] -= data[idx - 1]
    # print("YES")
    # print(*data)
    d = ' '.join(map(str, data))
    return (f'YES\n{d}')


length = int(input())
data = list(map(int, input().split()))

print(recover_snow_data(length, data))
