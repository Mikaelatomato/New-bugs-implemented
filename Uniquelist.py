def randomlist():
    import random
    listr = list(random.sample(range(1, 30), random.randint(10, 25)))    #  why two lists? well, random.sample will always give me a random unique item, so the second function wouldn't do anything.
    listr2 = list(random.sample(range(1, 30), random.randint(10, 25)))
    listf = listr + listr2    # so here, i merge both lists of unique random items to create a new one with duplicated items.
    sortedlist = sorted(listf)   # i sort it so it's easier to see where are those duplicated items
    print("the list that will be used is: ", sortedlist, "with a len of: ", len(sortedlist)) #but also you can see the len of the list to compare it later
    return sortedlist
def setunique(sortedlist):
    unique = set(sortedlist)
    uniquesorted = sorted(unique)
    return print("the list above without the duplicated items is: ", uniquesorted, "with a new len of: ", len(uniquesorted))
(setunique(randomlist()))
