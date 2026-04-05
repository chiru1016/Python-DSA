number = [1,2,2,5,7,3,9,4,4,2,6,7,]
new = []
for i in number:
    if i not in new:
        new.append(i)
new.sort()
print(new)