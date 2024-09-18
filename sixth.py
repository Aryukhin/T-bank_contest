from collections import deque

def parse_input(s):
    numbers = []
    current_number = 0
    for char in s:
        if char == ' ':
            if current_number > 0:
                numbers.append(current_number)
                current_number = 0
        else:
            current_number = current_number * 10 + int(char)
    if current_number > 0:
        numbers.append(current_number)
    return numbers

def process_dependencies():
    num_nodes = int(input())
    times = [0] * num_nodes
    in_degrees = [0] * num_nodes
    adjacency_list = [[] for _ in range(num_nodes)]

    for i in range(num_nodes):
        line = input().strip()
        values = parse_input(line)
        times[i] = values[0]
        for j in range(1, len(values)):
            adjacency_list[values[j] - 1].append(i)
            in_degrees[i] += 1

    max_time = [0] * num_nodes
    queue = deque()

    for node in range(num_nodes):
        if in_degrees[node] == 0:
            queue.append(node)

    while queue:
        current = queue.popleft()
        max_time[current] += times[current]

        for neighbor in adjacency_list[current]:
            in_degrees[neighbor] -= 1
            max_time[neighbor] = max(max_time[neighbor], max_time[current])
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    result = max(max_time)
    print(result)

if __name__ == "__main__":
    process_dependencies()
