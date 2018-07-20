def readfiles(filename):
    list = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list.append(str(line))
            line = f.readline()
    return list

list1 = readfiles('primenumbers.txt')
list2 = readfiles('happynumbers.txt')

with open('overlap.txt', 'w') as f:
        f.write(str([elem.rstrip() for elem in list1 if elem in list2]))

