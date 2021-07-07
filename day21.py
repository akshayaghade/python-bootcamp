#Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
def merge(list1,list2):
    merged_list = tuple(zip(list1,list2))
    return merged_list
list1 =[1,2,3]
list2 = ["a","b","c"]
print(merge(list1,list2))
#Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
merging = tuple(zip(range(8),range(8)))
print(merging)
#Using sorted() function, sort the list in ascending order.
list3 = [2,5,3,7,1]
print(sorted(list3))
#Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
import functools
list4 = [3,66,4,8,47,23]
odd_nums = list(filter(lambda x:x%2!=0,list4))
print(odd_nums)
