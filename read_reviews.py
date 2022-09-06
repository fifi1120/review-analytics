list = []
count = 0 
with open ("reviews.txt", "r") as file:
    for line in file:
        list.append(line)
        count += 1 #就是count = count + 1的简写
        if count % 1000 == 0: #%表示求余数
            print (len(list))
print (len(list))
print (list[0])
print ("-----------")
print (list[1])
print ("----------------")
print (list[2])