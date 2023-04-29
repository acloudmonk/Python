# Enter radious of a circle and prints its area, parameter, diameter


if __name__ == "__main__":
    radious = float(input("Enter radious of circle: "))
    area = 3.14 * radious * radious  # π*radious^2
    parameter = 2 * 3.14 * radious  # 2*π*radious
    diameter = 2 * radious  # 2*radious
    print("Area : ", area)
    print("Parameter : ", parameter)
    print("Diameter : ", diameter)
