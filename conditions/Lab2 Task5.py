x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("Point lies in Quadrant 1")

elif x < 0 and y > 0:
    print("Point lies in Quadrant 2")

elif x < 0 and y < 0:
    print("Point lies in Quadrant 3")

elif x > 0 and y < 0:
    print("Point lies in Quadrant 4")

elif x == 0 and y == 0:
    print("Point lies at the Origin")

elif y == 0:
    print("Point lies on the X-axis")

else:
    print("Point lies on the Y-axis")