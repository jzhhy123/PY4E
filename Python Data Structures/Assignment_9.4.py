name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

maxauthor = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    maxauthor[words[1]] = maxauthor.get(words[1], 0) + 1

time = None
author = None

for key in maxauthor:
    if time is None:
        time = maxauthor[key]

    if time < maxauthor[key]:
        time = maxauthor[key]
        author = key

print(author, time)