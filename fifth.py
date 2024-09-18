def time_difference(start, current):
    start_secs = (int(start[6]) * 10 + int(start[7])) + ((int(start[3]) * 10 + int(start[4])) * 60) + ((int(start[0]) * 10 + int(start[1])) * 60 * 60)
    current_secs = (int(current[6]) * 10 + int(current[7])) + ((int(current[3]) * 10 + int(current[4])) * 60) + ((int(current[0]) * 10 + int(current[1])) * 60 * 60)

    if current_secs >= start_secs:
        return (current_secs - start_secs) // 60
    return (24 * 60 * 60 + current_secs - start_secs) // 60


def main():
    start_time = input().strip()

    num_records = int(input().strip())

    penalties = {}
    scores = {}

    for _ in range(num_records):
        user, submission, problem, status = input().split()

        if user not in scores:
            scores[user] = [0, 0]  # First is count of "ACCESSED", second is total time

        if status == "DENIED" or status == "FORBIDEN":
            penalties[(user, problem)] = penalties.get((user, problem), 0) + 1
        elif status == "ACCESSED":
            scores[user][0] += 1
            time_penalty = time_difference(start_time, submission) + 20 * penalties.get((user, problem), 0)
            scores[user][1] += time_penalty

    leaderboard = []
    for user, (accessed_count, total_time) in scores.items():
        leaderboard.append([(-accessed_count, total_time), user])

    leaderboard.sort()

    position = 1
    next_pos = 1
    for i in range(len(leaderboard)):
        if i > 0 and (leaderboard[i - 1][0] != leaderboard[i][0]):
            position = next_pos
        print(position, leaderboard[i][1], -leaderboard[i][0][0], leaderboard[i][0][1])
        next_pos += 1


if __name__ == "__main__":
    main()
