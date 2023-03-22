numOfWords = int(input())
engtotr = {}
trtoeng = {}
for i in range(numOfWords):
    a = input()
    b = a.split(":")
    engtotr.update({b[0]: b[1]})
    trtoeng.update({b[1]: b[0]})

centence = input()
list2 = centence.split(" ")
list3 = set(list2)
list4 = list(list3)
list4.sort()
count = 0
notfound = []
if "TR" in list4:
    for j in range(1, len(list4)):
        if list4[j] in engtotr.keys():
            print(list4[j] + "=" + engtotr[list4[j]])
        else:
            count += 1
            notfound.append(list4[j])
    if count != 0:
        print(count, "word not found:", " ".join(notfound), end="")

elif "EN" in list4:
    for k in range(1, len(list4)):
        if list4[k] in trtoeng.keys():
            print(list4[k] + "=" + trtoeng[list4[k]])
        else:
            count += 1
            notfound.append(list4[k])
    if count != 0:
        print(count, "word not found:", " ".join(notfound), end="")
