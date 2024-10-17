#list[]:
list=[]
list.append(1)
list.append(2)
list.append('ram')
list.append(2.7)
print(list)
#use remove function to delete any element
list.remove(element)
#use pop to remove an element using index
list.pop(4)
#use extend function to add more elemnts at a time
list2=['ram','lax']
list.extend(list2)
print(list)
#append add the n elemnts into a single element
list.append(list2) #output [1,2,'ram',2.7,['ram','lax']]
#extend of a single element of string data will act as a split
list.extend('ram') #output [list,'r','a','m']
