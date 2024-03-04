# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        total = total + float(line[20:])
        count = count + 1

print("Average spam confidence:", total / count)