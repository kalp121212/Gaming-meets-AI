def Insert(ans_list,i,j):
    temp=j
    flag=True

    for x in ans_list:
        if temp>x[1]:
            ans_list.insert(ans_list.index(x),[i,temp])
            flag=False
            return

    if flag:
        ans_list.append([i,temp])


t=int(input())

ans_dic={}
ans_list=[]

for i in range(t):
    temp=input().split(':')
    match=temp[0]
    temp_dic={}
    temp=temp[1].split(',')

    for i in temp:
        for j in range(len(i)):
            if i[j]=='-':
                temp_dic[i[:j]]=int(i[j+1:])
                flag=True  
                for k in ans_list:
                    if k[0]==i[:j]:
                        ans_list.remove(k)
                        Insert(ans_list,i[:j],int(i[j+1:])+k[1])
                        flag=False
                        break
                if flag:
                    Insert(ans_list,i[:j],int(i[j+1:]))
    ans_dic[match]=temp_dic

ans_list=[(x[0],x[1]) for x in ans_list]

print(ans_dic)
print(ans_list)