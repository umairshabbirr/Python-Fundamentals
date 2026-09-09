x=10 
y="25"
try:
    print(x+y)
except TypeError as e:
    print("error found",e)
 #fixing
fixed_sum=x+ int(y)
print("correct sum", fixed_sum)
#types
print(type(x))
print(type(y))