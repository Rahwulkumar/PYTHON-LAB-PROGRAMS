import math

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    print("Enter the sides of the first triangle:")
    a1 = float(input("a1: "))
    b1 = float(input("b1: "))
    c1 = float(input("c1: "))

    print("Enter the sides of the second triangle:")
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    c2 = float(input("c2: "))

    area1 = area_of_triangle(a1, b1, c1)
    area2 = area_of_triangle(a2, b2, c2)
    total_area = area1 + area2

    contribution1 = (area1 / total_area) * 100
    contribution2 = (area2 / total_area) * 100

    print(f"Area of the first triangle: {area1:.2f}")
    print(f"Area of the second triangle: {area2:.2f}")
    print(f"Total area enclosed by both triangles: {total_area:.2f}")
    print(f"Contribution of the first triangle: {contribution1:.2f}%")
    print(f"Contribution of the second triangle: {contribution2:.2f}%")

if __name__ == "__main__":
    main()
