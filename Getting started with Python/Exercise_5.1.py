total = 0
count = 0
while True:
    answer = input("Enter a number: ")
    if answer == "done":
        break
    try:
        answer == int(answer)
    except:
        print("Enter a number: bad data")
        print("Invalid")
        continue
    count = count + 1
    total = total + int(answer)
print(total,count,total/count)