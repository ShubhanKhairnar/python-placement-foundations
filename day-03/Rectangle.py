def calculate_area(length,width):
    return length * width

def calculate_perimeter(length,width):
    return 2 * (length + width)

Length = float(input("Enter Length:"))
width = float(input("Enter Width:"))

area = calculate_area(Length,width)
perimeter = calculate_perimeter(Length,width)

print(f"Area of rectangle is {area:.2f} and Perimeter of rectangle is {perimeter:.2f}")
