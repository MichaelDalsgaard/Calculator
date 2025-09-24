def calculate_square_side(area):
    side = area ** 0.5
    return side

def calculate_triangle_area(base, height):
        area = (base * height) / 2
        return area

def main():
    while True:

        print("\nWhat would you like to do?")
        print("1. Calculate square side length from area")
        print("2. Calculate triangle area from base and height")
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

        elif choice == "x" or choice == "X":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


