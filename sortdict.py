import operator
d={1:2,3:4,4:3,2:1,0:0}
print('Original dictionary:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print('Dictionary is ascending order by value:',sorted_d)
sorted_d=sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('Dictionary is descending order by value:',sorted_d)
