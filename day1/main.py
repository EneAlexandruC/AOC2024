from collections import defaultdict

# Part 1
with open("day1/input.txt", "r") as input:

    leftID, rightID = [], []
    diff = 0

    for line in input:
        numbers = line.split()
        leftID.append(int(numbers[0]))
        rightID.append(int(numbers[1]))

    leftID.sort()
    rightID.sort()

    for i in range(len(leftID)):
        diff += abs(rightID[i] - leftID[i])
        
    print(diff)


# Part 2

with open("day1/input.txt", "r") as input:

    IDs = []
    scores = defaultdict(int)
    score = 0

    for line in input:
        numbers = line.split()
        IDs.append(int(numbers[0]))
        scores[int(numbers[1])] += 1

    for ID in IDs:
        score += ID * scores[ID]

    print(score)