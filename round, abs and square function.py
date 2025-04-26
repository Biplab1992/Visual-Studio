

#length = float(input("Enter the length of the rectangle:"))
#width = float(input("Enter the width of the rectangle:"))

length,width = input("Input value (length & width):").split()

length = int(length)
width = int(width)

#avg_side = (length+width)
#square_area = math.pow(avg_side,2)

# area = 
# # rounded_area = math.pow(area,2)
# print(f"Area", area)
# print("square", rounded_area)

def rectangle (length,width):
    area_rectangle= length*width
    return (area_rectangle)
rectangle(length,width)