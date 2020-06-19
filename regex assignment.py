import re

hand = open("C:\\Users\\arssharm\\Desktop\\data.txt")

act_lst = list()

for line in hand:
    line = line.rstrip()
    lst = re.findall("[0-9]+", line)
    act_lst.extend(lst)

sum = 0

for num in act_lst:
    sum = sum + int(num)


print(sum)
