calories = []
list_  = []

with open("./input", 'r') as f:
    test = []
    content = f.read()
    for i in content.split("\n"):
        if i == "":
            list_.append(test)
            test = []
        else: test.append(int(i))
    for i in list_:
        calories.append(sum(i))

# for puzzle 1:
print(max(calories))

# for puzzle 2:
calories.sort()
print(sum(calories[len(calories) - 3:]))

