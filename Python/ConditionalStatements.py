#
#print(2<3)

print("-----equal ?--------")
print(3==3)

print("-----equal >< --------")
print(2>3) 

print("-----not equal  --------")
print("a"!= "b" )

print("-----Value in  --------")
print(2 in [1,2,3])
#control Flow

#firstname= input("Enter your name ")
#lastname= input("Enter your lastname ")
#print("Hello   ",firstname, lastname )

print("-----Reviewing Values  --------")
if (1 > 2):
    print("fist value is greather")
else:
    print("Second value is greather ")


print("-----Length  Values  --------")
job="Engineer"
a=len(job)
if (a >= 6):
    print("Job name is long")
elif (a ==5 ):
    print("Job name is 5 Characters")
else:
    print("Job name is short ")
