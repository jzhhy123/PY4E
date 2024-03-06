fname = input("Enter file name: ")
fh = open(fname)
lst = list()
answer = []

for line in fh:
    words = line.split()
    for word in words:
        if word not in answer:
            answer.append(word)

print(sorted(answer))
