# Project: Temperature Converter


def to_celsius(f_temp):
    return  (f_temp - 32) * (5/9)

def to_fahrenheit(c_temp):
    return (c_temp * (9/5)) + 32

def to_kelvin(c):
    return (c + 273.15)  

def from_kelvin(k):
    return (k - 273.15)

def show_menu():
    print('''\n\nChoose a conversion:  
          1. Celsius to Fahrenheit 
          2. Fahrenheit to Celsius
          3. Celsius to Kelvin 
          4. Kelvin to Celsius  
          5. Quit''')

while True:
    show_menu()
    try:
        choice = int(input('Enter your choice: ')) 
        possible_options = [1,2,3,4,5] 
        if choice in possible_options:
            if choice == 1:
                T_cell = float(input('Enter temperature in Celsius: '))
                result = to_fahrenheit(T_cell)
                result1 = round(result, 2)
                print(f'Result:  {T_cell}°C = {result1}°F')
    
            elif choice == 2:
                T_fah = float(input('Enter temperature in Fahrenheit: '))        
                result = to_celsius(T_fah)
                result1 = round(result, 2)
                print(f'Result:  {T_fah}°F = {result1}°C')     

            elif choice == 3:
                T_cell = float(input('Enter temperature in Celsius: '))
                result = to_kelvin(T_cell)
                result1 = round(result, 2)
                print(f'Result:  {T_cell}°C = {result1}K')

            elif choice == 4:
                T_kel = float(input('Enter temperature in kelvin: '))
                result = from_kelvin(T_kel)
                result1 = round(result, 2)
                print(f'Result:  {T_kel}K = {result1}°C')

            elif choice == 5:
                print('Good Bye!')
                break    

        elif choice not in possible_options:
            print("Invalid choice. Try again.")
     
    except ValueError:
        print('Please, Enter only numbers!') 

