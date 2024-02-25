list = [2 , 45 , 23, 56, 12, 1, 4,9,2]
list.append(8) # Adds 8 in list
print(list)
list.sort()  # Ascending Order 
list.sort(reverse=True) # Descending Order
list.reverse() # Reverses our original list
print(list)
print(list.index(45)) # tells us where the certain number is according to index
print(list.count(2))

m = list.copy()  # list will be same but 0 will be added in m only
m[0] = 0  # add 0 in the list at index 0
print(m)
print(list)

list.insert(1, 23)  # add 23 in the list at index 1
print(list)

n = [100 , 200 , 300]  # it add the value of n in list
k = list+n  # Works same as extend
list.extend(n) # extend opens the n and adds it into list
print(list)