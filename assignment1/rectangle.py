# to find area of a rectangle and perimeter of the rectangle 

length = int(input("enter the length of the rectangle : "))
print("length is : ",length)
breadth = int(input("enter the breadth of the rectangle : "))
print("breadth is : ",breadth)
area = length * breadth
perimeter  = 2 * (length + breadth)
print("the area is = ", area,"\nperimeter is = ",perimeter)

# using functions -
def rectangle(length,breadth):
    return length * breadth

def perimeter (length,breadth):
    return 2*(length + breadth)

length = int(input("enter the length of the rectangle : "))
print("length is : ",length)

breadth = int(input("enter the breadth of the rectangle : "))
print("breadth is : ",breadth)

area = rectangle(length, breadth)
perimeter = perimeter(length, breadth)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)



