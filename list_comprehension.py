num = int(input("Enter a num:"))
odd_list = (i for i in range(1,num+1) if i%2==1)
print('All odd nums below given num:\n',list(odd_list))

fruits = ['rasberry', 'orange', 'pear', 'cherry', 'watermelon']
Cap_list = (i.capitalize() for i in fruits )
print(list(Cap_list))