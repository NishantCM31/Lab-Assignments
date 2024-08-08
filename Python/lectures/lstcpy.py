olist=[1,2,3,[4,5]]
clist=olist.copy()
clist[0]=10
olist[3][0]=40

print('Original',olist)
print("copied",clist)