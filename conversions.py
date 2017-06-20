def showMenu():
    print "A: Convert celsius to fahrenheit"
    print "B: Convert fahrenheit to celsius"
    print "X: Exit"

def celsiusToFahrenheit(celsiusTemperature):
    "This function converts Celsius temps to Fahrenheit temps"
    fahrenheit = celsiusTemperature * (9.0 / 5.0) + 32.0
    return fahrenheit
    

def fahrenheitToCelsius(fahrenheitTemperature):
    "This function converts Fahrenheit temps to Celsius temps"
    celsius = (fahrenheitTemperature - 32.0) * (5.0 / 9.0)
    return celsius


    
showMenu()
option = raw_input("Option: ")


while option != "X":
    if option == "A" or option == "B":
        number = raw_input("Number to convert: ")
        if option == "A":
            print(celsiusToFahrenheit(float(number)))
        elif option == "B":
             print(fahrenheitToCelsius(float(number)))
    else:
        print "Please enter a valid option."
       

    showMenu()
    option = raw_input("Option: ")

    




        























































        



    
