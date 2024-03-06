fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# open file
fh = open(fname)
count = 0

# store

data = []

for line in fh:
    if line.startswith("From") and len(line.split()) > 2:
        imfor = line.split()
        data.append(imfor[1])

for address in data:
    print(address)

print("There were", len(data), "lines in the file with From as the first word")
