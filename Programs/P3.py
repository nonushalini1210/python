
def display_distance():
    miles=float(input("Enter distance in miles(M):"))
    conversion_factor=1.609344
    kilometers=miles*conversion_factor
    print(miles,'M = ', kilometers,'K')
    print('\n')
    
def display_temperature():
    fahrenheits=float(input("Enter temperature in Fahrenheit(F):"))
    celsius=((fahrenheits-32)*(5/9))
    print(fahrenheits, 'F = ', celsius,'C')
    print('\n')
    
def distance_weight():
    Pounds=float(input("Enter weight in Pounds(lb):"))
    conversion_factor=0.45359237
    Kilograms=Pounds*conversion_factor
    print(Pounds, 'lb = ',Kilograms, 'kg')
    print('\n')
    
def main():
    display_distance()
    display_temperature()
    distance_weight()
    return
main()
