name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hourcount = dict()
hourlist = []

for line in handle:
    words = line.split()
    if  len(words) > 2 and words[0] == 'From':
        hour = words[5].split(':')
        hourcount[hour[0]] = hourcount.get(hour[0], 0) + 1
    else:
        continue

for k,v in hourcount.items():
    hourlist.append((k,v))
hourlist.sort()

for k,v in hourlist:
    print(k,v)