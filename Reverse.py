s= "Karthik has lot of girlfriends"

k = s.split(" ")

for ele in k:
    m = ele[::-1]
    print (m, end = " ")


print ("\n***************")

for j in k:
    ele = list(j)
    for i in range(len(ele)//2):
        temp = ele[i]
        ele[i] = ele[len(j)-i-1]
        ele[len(j)-i-1] = temp
    print ("".join(ele), end ="\t")






