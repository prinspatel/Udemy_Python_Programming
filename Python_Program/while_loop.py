#wile loop use to check a conditio. if the condition is true the loop will continue.
it = 4
while it>1:
    print(it)
    it = it -1   #without this loop will not stop. it will print 4,3,2
print("While Execution is done")
print("--------------- New One --------------------")

print("skip number 3")
skip =  4
while skip>1:
    if skip != 3:
        print(skip)
    skip = skip - 1
print("While Execution is done")
print("--------------- New One --------------------")

print("Brackpoint in loop")
brack =0
while brack<10:
    print(brack)
    if brack == 5:
        break
    brack = brack + 1

print("While Execution is done")
