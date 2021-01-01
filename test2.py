file1 = open("input.txt","r+")


## input from file

input1 = file1.readlines()
list1= []
for i in input1:
    if "\n" in i:
        # print(i[0:-1])
        list1.append(i[0:-1])
    else:
        list1.append(i)
print("input: ", list1)

## count collision

size  = 10
# print(size)

list2 = []
for i in range(size):
    list2.append("x")
# print(list2)

collision = []

for j in list1:
    if j not in list2:
        data = int(j)
        print("++++++++++++++++++++")
        print("data",data)
        # print("size", size)
        key  = data%size
        # print("key",key)
        if list2[key] == "x":
            list2[key] = data
        else:
            for k in range(size):
                print("-----------")
                print("i=",k)
                key2 = (key+k)%size
                print("key=", key2)
                if list2[key2] != "x":
                    collision.append("1")
                    print("!! colision !!")
                
                if list2[key2] == "x":
                    list2[key2]=data
                    print("!! get place !!")
                    break
                print("-----------")
        print("++++++++++++++++++++")


print("output: ",list2)
print("Total collision: ", len(collision))










