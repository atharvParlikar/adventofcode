opponent_options = ['A', 'B', 'C']
your_options = ['X', 'Y', 'Z']

scores = []

with open("./input", 'r') as f:
    todo = f.read().split("\n")
    todo = todo[:-1]
    for i in todo:
        o = i[0]
        y = i[2]
        if y == "X":
            scores.append(your_options.index(your_options[opponent_options.index(o) - 1]) + 1)
        elif y == "Y":
            scores.append(opponent_options.index(o) + 4)
        else:
            scores.append(((opponent_options.index(o) + 1) % 3) + 7)

print(sum(scores))
