elfList, sumOfElfCal = [], 0
for line in open("input.txt", "r"):
    if line == "\n":
        elfList.append(sumOfElfCal)
        sumOfElfCal = 0
    else:
        sumOfElfCal += int(line)
elfList.sort(reverse=True)
print(str(elfList[0])+"   "+str(sum(elfList[:3])))
