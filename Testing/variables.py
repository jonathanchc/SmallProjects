# Basics

#
str_string="Hello "
str_int= 100

print(str_string)

print(str_int)

print(str_int , str_string)

#lists = order list of items.
number_list=[1,2,3,4]
print(type(number_list))
print(number_list)
print("list items ", len(number_list))
print(number_list[0]) ##index item

print("")

char_list=["a","b","c","d","e","f"]
print(char_list)
print("list items ", len(char_list))
print(char_list[2]) ##index item.

print("---------------------------------------")
##Addin
char_list.insert(len(char_list),"g")
print(char_list)
print("list items ", len(char_list))
print(char_list[2]) ##index item.


print("---------------------------------------")
#removing last element
print("Extracting Last element Pop",char_list.pop())
print(char_list)
print("list items ", len(char_list))


print("---------------------------------------")
#removing first element
print("Extracting First element Pop",char_list.pop(0))
print(char_list)
print("list items ", len(char_list))



print("---------------------------------------")
char_list=("a","b","c","d","e","f")
print(type(char_list))
print(char_list)
print("list items ", len(char_list))
print(char_list[2]) ##index item.

