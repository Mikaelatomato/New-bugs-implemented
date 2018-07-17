import random
def randomlist():
    listr = list(random.sample(range(1,100), random.randint(10, 25))) #randomlist
    print("the list that will be used is: ", listr)
    return listr
def first_last(listr):
    new = [listr[0], listr[-1]]
    return new
listnewr = first_last(randomlist())
print ("the first and the last item of the list above are:", listnewr)
