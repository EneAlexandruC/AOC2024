from collections import defaultdict

# Part 1
# input = open("day1/input.txt", "r")

# leftID = []
# rightID = []
# diff = 0

# for line in input:
#     numbers = line.split()
#     leftID.append(int(numbers[0]))
#     rightID.append(int(numbers[1]))

# leftID.sort()
# rightID.sort()

# for i in range(len(leftID)):
#     if leftID[i] - rightID[i] < 0:
#         diff += rightID[i] - leftID[i]
#     else:
#         diff += leftID[i] - rightID[i]
    
# print(diff)

# input.close()

# Part 2

input = open("day1/input.txt", "r")

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
input.close()