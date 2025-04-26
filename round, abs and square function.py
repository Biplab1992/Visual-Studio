import math

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

length = abs(length)
width = abs(width)

#avg_side = (length+width)
#square_area = math.pow(avg_side,2)#

area = length*width
rounded_area = math.pow(area,2)
print(f"Area", area)
print("square", rounded_area)