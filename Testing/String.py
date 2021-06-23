#string python
#https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#Some string manipulation options
#We can define a string as a chain of characters, and to manipulate and show those  there is  a variety of options

print('single quoted')

print("double quoted")


print('''Multi
    Line
    string
     ''')


##Concatenation is the way to connect multiple strings
print("Hello "+ "Wold")

str_concatenated = "Python " + " computer"

print(str_concatenated)

##Strings manipulation
str_gretting="Good Monrning "
print(str_gretting * 3 )


#Making the text in upper case.
print(str_gretting.upper)

#Find values in  string

print("\n")


#the result is a integer with the position
str_find=str_gretting.find('M')

#transforming the integer into string using the str() method
print("The Letter M is in the position " + str(str_find))
print("\n")
#Adding spaces or tabs in the string.
print("Tab\t" + str_gretting)
print("\n")
#Adding new Line in the string.
print("New Line\n" + str_gretting)

#print  quotes
print("'quotes'")
print('"Double quotes"')


