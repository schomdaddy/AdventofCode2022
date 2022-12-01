total = 0
elves = []
for line in open("input.txt"):
    if line == "\n":
        elves.append(total)
        total = 0
    else:
        total += int(line)
elves.sort(reverse=True)
print(elves[0])
print(elves[0]+elves[1]+elves[2])