opponant = {
        "A": 1,
        "B": 2,
        "C": 3
    }
you = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

with open("input", 'r') as f:
    input_ = f.read().split("\n")
    input_ = input_[:-1]
    scores = []
    for i in input_:
        o = i[0] # opponant
        y = i[2] # you
        if (o == "A" and y == "Y") or (o == "B" and y == "Z") or (o == "C" and y == "X"): # winning condition
            scores.append(you[y] + 6)
        elif opponant[o] == you[y]:
            scores.append(you[y] + 3)
        else:
            scores.append(you[y])

print(sum(scores))
