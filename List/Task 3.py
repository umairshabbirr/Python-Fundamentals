numbers=[22,44,53,23,20,70,100,65,23,788,2,4,6,8]
even=[]
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print("even numbers: ",even)
print("original list:",numbers) 