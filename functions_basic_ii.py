#1
num = 5
def countdown():
    # new = []
    for i in range(num, -1, -1):
        # new.append(i)
        print(i)
        # new.append(i)

print(countdown())


#2
list = [1,2]
def print_and_return():
    print(list[0])
    return(list[1])

print(print_and_return())


#3
list = [1,2,3,4,5]
def first_plus_length():
    sum = list[0] + len(list)
    return(sum)

print(first_plus_length())

#4
list = [5,2,3,2,1,4]
def values_greater_than_second():
    new = []
    for i in range(len(list)):
        if list[i] >= list[2]:
            new.append(list[i])
            print(new)

print(values_greater_than_second())

#5
def length_and_value(value = '', repeat=4):
    print(f"{value}" * repeat)

length_and_value(value="7", repeat=4)