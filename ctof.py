import re

type = input("Quel est le type de votre temperature  ? Celsius/Fahrenheit ")
type = type.lower()

regex_pattern = r'^\d+$'
match type:
    case "celsius":
        print("Conversion en Fahrenheit")
        EnCelsius = input("Entrer la temperature en Celsius : ")
        if re.match(regex_pattern, EnCelsius) : 
            EnCelsius_convert = float(EnCelsius)
            EnFahrenheit = (EnCelsius_convert * 9/5) + 32
            print("La temperature en Fahrenheit est " + str(EnFahrenheit) + " °F")
        else :
            print("Erreur de saisie") 


    case "fahrenheit":
        print("Conversion en Celsius")
        EnFahrenheit = input("Entrer la temperature en Fahrenheit : ")
        if re.match(regex_pattern, EnFahrenheit) : 
            EnFahrenheit_convert = float(EnFahrenheit)
            EnCelsius = (EnFahrenheit_convert - 32) * 5/9
            print("La temperature en Celsius est " + str(EnCelsius) + " °C")
        else :
            print("Erreur de saisie") 


    case _:
        print("Cas d erreur")

    