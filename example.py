from doughnut import generate_doughnut

with open("text.txt", "r") as f:
    contents = f.read()

# big doughnut
print(generate_doughnut(contents))

# one doughnut for each line
for text in contents.split("\n"):
    print(generate_doughnut(text))