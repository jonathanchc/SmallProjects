#structures

print("----------------Dictionaries-------------------")
ages= {"David":32 , "Alexandra": 25 , "Ken":42}
print(ages)
print(ages["Ken"]) # printing one value
# add additional key value pair
print("----------------add values-------------------")

ages= {"David":32 , "Alexandra": 25 , "Ken":42 , "Lissa": 53}

#Updating Alexanda Age
ages["Alexandra"]=26

print(ages)

print("----------------Remove values-------------------")
#Remove values 
ages.pop("Ken")
print(ages)


print("----------------Get values-------------------")
print(ages.get("David"))

print("----------------show  values-------------------")
ages.keys
ages.values

