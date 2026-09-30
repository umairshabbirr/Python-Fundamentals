subjects=["python","java","c++","c","javascript"]
print("original list: ",subjects)
new=input("enter new sunjects:")
subjects.append(new)
print("new list: ",subjects)
removesub=input("enter the subject to remove:")
subjects.remove(removesub)
subjects.sort()
print("sorted list: ",subjects)
