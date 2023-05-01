from doughnut import generate_doughnut

# generate dougnuts for each line
with open("text.txt", "r") as f:
    contents = f.read()

for text in contents.split("\n"):
    if not text: continue # skip empty lines

    print(generate_doughnut(text))