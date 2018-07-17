def number():
    num = int(input("How many numbers of fibonnaci do you want to display?: "))
    return num
def fibonnaci(num):
    fibo = list
    if num == 0:
        fibo = []
    if num == 1:
        fibo = [1]
    if num >= 2:
        fibo = [1, 1]
        while len(fibo) < num:
            fibo.append(fibo[-1] + fibo[-2])
    return fibo
print (fibonnaci(number()))
# based on a sequence that starts from 1 1 2 3 5 ...
#did two functions because the exercise asked for it.
