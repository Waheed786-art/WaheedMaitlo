#MAP: The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# def cube(x):   # It is must to create function first in order to use map or filter
#     return x * x * x

# cube(5)

l = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# Difficult way of printing cube
# newl = []
# for item in l:
#     newl.append(pow(item, 3))

# print(newl)

# Easy way of printing cube

new = list(map(lambda x: x*x*x , l))   # first function name and then items. It is good to use lambda funtion instead of function with more and complicated lines.
print(new)

# FILTER: The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.

def function_filter(x):   # It is must to create function first in order to use map or filter
    return x>2

newl = list(filter(function_filter , l))  # First list/tuple/set then function name and then any item of list or whole list.
print(newl)

# Reduce: The reduce function is a higher-order function that applies a function to a sequence and returns a single value.
from functools import reduce
numbers = (1 , 2 , 3 ,4 ,5)
def mysum (x , y):
    return x+y

sum = reduce(mysum, numbers )
print(sum)

