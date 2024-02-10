#2a
def hello():
    print("Hello!")
hello()
 
#2b
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]
print(pack(4,2,8))

empty_lunch = []
lunch_box = ["PBJ", "chips", "fruitcup"]

#2c
def eat_lunch(lunch):
    i = 0
    if len(lunch) == 0:
        print("My lunchbox is empty!")
    else:
        for food in lunch:
            if i==0:
                print("First I eat " + food)
                i += 1
            else:
                print("Next i eat " + food)

eat_lunch(empty_lunch)
eat_lunch(lunch_box)