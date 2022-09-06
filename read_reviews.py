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
print ("------------")
print (list[2])

sum_len = 0
for d in list: #list里面已经加进去了所有的清单
    sum_len = sum_len + len(d) #用len可以求清单的长度/个数；这里len(清单里面的每一项)，就是求每一项的长度

print ("留言的平均长度为", sum_len/len(list))

new = []
for d in list: 
    if len(d) < 100:
        new.append(d) 
print ('一共有', len(new), "笔留言长度小于100") #这里print要定个写，因为 for in （for loop）其实还是有回旋的含义在里面，等它全部回旋（筛选）完了再印出来
