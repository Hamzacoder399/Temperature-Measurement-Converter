#Making a temperature/measurement converter
#TEMPRATURE CONVERTER

print("Welcome to the temprature/measurement converter!")
u = input(
    "\nDo you want to go to Temprature Converter or Measurement Converter?(enter T or M)  "
)
T = "T"
M = "M"

if (u == T):
   q = input(
       "\nWhich Temprature scale do you need to convert to?(enter F , C or K)  "
   )
   F = "F"
   C = "C"
   K = "K"

   if (q == F):
      fahrenheit = float(input("\nEnter Fahrenheit: "))
      celcius = (fahrenheit - 32) / 1.8
      print("\n" + str(fahrenheit) + " degree Fahrenheit is equal to " +
            str(celcius) + " degree Celcius.")
      kelvin = celcius + 273.15
      print("\n" + str(celcius) + " degree Fahrenheit to Kelvin is" +
            str(kelvin) + " degree Kelvin.")
      print("\n")

   if (q == C):
      celcius = float(input("\nEnter Celcius: "))
      fahrenheit = (celcius * 1.8) + 32
      kelvin = celcius + 273
      print("\n" + str(celcius) + " degree Celcius is equal to " +
            str(fahrenheit) + " degree Fahrenheit.")
      print("\n" + str(celcius) + " degree Celcius to Kelvin is " +
            str(kelvin) + " degree Kelvin.")
   if (q == K):
      kelvin = float(input("\nEnter Kelvin: "))
      celcius = 273 - kelvin
      fahrenheit = (celcius * 9 / 5) + 32
      print("\n" + str(kelvin) + " degree Kelvin is equal to " +
            str(fahrenheit) + " degree Fahrenheit.")
      print("\n" + str(kelvin) + " degree Kelvin to is equal to" +
            str(celcius) + " degree celcius.")

#MEASUREMENT CONVERTER
elif (u == M):
   p = input(
       "\nWhich length quantity do you need to convert to other units?(for millimeters=mm,centimeters=cm,meters=m and inches=i.): "
   )
   mm = "mm"
   cm = "cm"
   mtr = "m"
   inch = "i"

   if (p == mm):
      millimeters = float(input("\nEnter millimeters: "))
      centimeters = millimeters / 10
      print("\n" + str(millimeters) + " millimeters is equal to " +
            str(centimeters) + " centimeters.")
      meters = centimeters / 100
      inches = centimeters / 2.54
      print("\n" + str(mm) + " millimeters to meters is " + str(meters) +
            " meters.")
      print("\n", str(mm), "millimeters to inches is", str(inches), "inches.")

   if (p == cm):
      centimeters = float(input("\nEnter centimeters: "))
      millimeters = centimeters * 10
      meters = centimeters / 100
      inches = centimeters / 2.54
      print("\n" + str(centimeters) + " centimeters is equal to " +
            str(millimeters) + " millimeters.")
      print("\n" + str(centimeters) + " centimeters is equal to " +
            str(meters) + " meters.")
      print("\n" + str(centimeters) + " centimeters is equal to " +
            str(inches) + " inches.")

   if (p == mtr):
      meters = float(input("\nEnter meters: "))
      millimeters = meters * 1000
      centimeters = meters * 100
      inches = meters * 39.37
      print("\n" + str(meters) + " meters is equal to " + str(millimeters) +
            " millimeters.")
      print("\n" + str(meters) + " meters is equal to " + str(centimeters) +
            " centimeters.")
      print("\n" + str(meters) + " meters is equal to " + str(inches) +
            " inches.")

   if (p == inch):
      inches = float(input("\nEnter inches: "))
      millimeters = inches * 25.4
      centimeters = inches * 2.54
      meters = inches / 39.37
      print("\n" + str(inches) + " inches is equal to " + str(millimeters) +
            " millimeters.")
      print("\n" + str(inches) + " inches is equal to " + str(centimeters) +
            " centimeters.")
      print("\n" + str(inches) + " inches is equal to " + str(meters) +
            " meters.")
else:
   e = input(
       "\nDo you want to go to Temprature Converter or Measurement Converter?(enter Temprature or Measurement)  "
   )

