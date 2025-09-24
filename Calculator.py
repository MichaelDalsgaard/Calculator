def calculate_square_side(area):
    side = area ** 0.5
    return side

def calculate_triangle_area(base, height):
        area = (base * height) / 2
        return area

def calculate_slope_percent(distance, z_change):
    slope = (z_change / distance) * 100
    return slope

def calculate_slope_ratio(distance, z_change):
    ratio = distance / z_change
    return ratio

def calculate_slope_ratio_by_hypotenuse(hypotenuse, z_change):
    base = (hypotenuse**2 - z_change**2) ** 0.5
    ratio = base / z_change
    return ratio

def main():
    while True:

        print("\nWhat would you like to do?")
        print("1. Calculate square side length from area")
        print("2. Calculate triangle area from base and height")
        print("3. Calculate slope percentage from distance and vertical change")
        print("4. Calculate slope ratio from distance and vertical change")
        print("5. Calculate slope ratio from hypotenuse and vertical change")
        print("X. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                try:
                    area = float(input("Enter the area of the square: "))
                    side = calculate_square_side(area)
                    print(f"The side length is: {side}")
                    
                    cont = input("\nDo you want to calculate another area? (y/n): ")
                    if cont.lower() != 'y':
                        break
                except ValueError:
                    print("Please enter a valid number")
        
        elif choice == "2":
            while True:
                try:
                    base = float(input("Enter the base of the triangle: "))
                    height = float(input("Enter the height of the triangle: "))
                    area = calculate_triangle_area(base, height)
                    print(f"The area of the triangle is: {area}")
                    
                    cont = input("\nDo you want to calculate another area? (y/n): ")
                    if cont.lower() != 'y':
                        break
                except ValueError:
                    print("Please enter a valid number")

        elif choice == "3":
            while True:
                try:
                    distance = float(input("Enter the horizontal distance: "))
                    z_change = float(input("Enter the vertical change: "))
                    slope = calculate_slope_percent(distance, z_change)
                    print(f"The slope percentage is: {slope}%")
                    
                    cont = input("\nDo you want to calculate another slope? (y/n): ")
                    if cont.lower() != 'y':
                        break
                except ValueError:
                    print("Please enter a valid number")
        
        elif choice == "4":
            while True:
                try:
                    distance = float(input("Enter the horizontal distance: "))
                    z_change = float(input("Enter the vertical change: "))
                    ratio = calculate_slope_ratio(distance, z_change)
                    print(f"The slope ratio is 1:{ratio}")
                    
                    cont = input("\nDo you want to calculate another ratio? (y/n): ")
                    if cont.lower() != 'y':
                        break
                except ValueError:
                    print("Please enter a valid number")

        elif choice == "5":
            while True:
                try:
                    hypotenuse = float(input("Enter the hypotenuse length: "))
                    z_change = float(input("Enter the vertical change: "))
                    ratio = calculate_slope_ratio_by_hypotenuse(hypotenuse, z_change)
                    print(f"The slope ratio is 1:{ratio}")
                    
                    cont = input("\nDo you want to calculate another ratio? (y/n): ")
                    if cont.lower() != 'y':
                        break
                except ValueError:
                    print("Please enter a valid number")

        elif choice == "x" or choice == "X":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


