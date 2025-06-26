s1 = {2,3,1}
s2 = {4,6,2}
s3 = set(zip(s1,s2))
print(s3,'\n')

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x,y in zip(list1, list2[::-1]):
    print(x,y) #prints pairs one by one but second list elements in pairs are reversed


#Zip for dicts
stocks = ['reliance', 'tcs', 'infosys']
prices = [3452,2345,2250]

new_dict = {stocks: prices for stocks,prices in zip(stocks, prices)} #dictionary comphrehension
print('\n{}'.format(new_dict))