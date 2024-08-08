mylist=[]
print(mylist)

names=['jeff','bill','steve']
print(names)

item=[1,'jeff','computer',75.5,True]
print(item)

print(type(mylist))
print(type(names))
print(type(item))


nums=[1,2,3,[4,5,6,[7,8,[9]]],10]
print(nums[0])
print(nums[1])
print(nums[3])
print(nums[4])
print(nums[3][0])
print(nums[3][3])
print(nums[3][3][0])
print(nums[3][3][2])

print('For Loop')
for i in nums:
    print(i)


nums.append(5)
print(nums)

        