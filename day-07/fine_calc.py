#Speeding fine calculator

def calculate_fine(speed, speed_limit):
    over_speed = speed - speed_limit

    if over_speed <= 0:
        return 0
    elif over_speed <= 20:
        return 500
    else:
        return 2000

speed = float(input("Enter your speed (in km/h): "))
speed_limit = float(input("Enter the speed limit (in km/h): "))

fine = calculate_fine(speed, speed_limit)
print(f"Your fine is: ${fine:.2f}")
    