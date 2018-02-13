#Enthalpy Changes
#This program calculates the amount of energy and cost to melt some snow.
#Water c 4.187 kJ/kgK, Ice C 2.108 kJ/kgK
#Enthalpy of Vaporization 2.030 mJ/kg
#Enthalpy of Fusion 334 kJ/kg

print ("This program calculates the amount of energy and cost to melt some snow in a rectangular area.");
print ("<Enter> after every input.")
print ("First the dimensions of the area you want to clear, in metres (m): ")
length = int(input ("Length: "))
width = int(input ("Width: "))
depth = float(input ("Depth: "))
vol = length*width*depth
print ("You have %f cubic metres of snow." % (vol))
print ("How dense is the snow?\n0 for dusting\n1 : light\n2 : medium\n3 : dense\n4 : solid ice")
iRho = int(input ("Density: "))
rho = 3; #default kg m-3
if (iRho == 0):
    rho = 50
elif (iRho == 1):
    rho = 100
elif (iRho == 2):
    rho = 250
elif (iRho == 3):
    rho = 400
elif (iRho == 4):
    rho = 900
mass = rho*vol
print ("Density is approximately %i kg per cubic metre."%(rho ))
print ("There is %f kg of snow on the ground." % (mass))
temp = int(input("What's the negative temperature outside (Degrees Celcius)? Enter an integer: -"))
eMelt = ((temp+1) * mass * 2.108) + (mass*334000) #energy req to melt and fuse
eVap = (100*mass*4.187) + (mass*2030000) + eMelt
print()
print ("To melt this snow and bring it to 1 degree, it will take %f J of energy. \nThis is equivalent to %f TJ." % (eMelt, eMelt/1e12))
print ("To completely vaporize this snow, it will take %f J of energy.\nThis is equivalent to %f TJ." % (eVap, eVap/1e12))
print()
print("For reference, this is approximately %f nuclear detonations to melt." % (eMelt/1e17))
print("For reference, this is approximately %f nuclear detonations to vaporize." % (eVap/1e17))

choice = int(input ("Press 1 to melt, press 2 to vaporize. "))
time = int(input ("How long do you have? Time in minutes: "))
eChoice = 0
if choice == 1:
    eChoice = eMelt
elif choice == 2:
    eChoice = eVap
else:
    print ("Vaporize is the default. The option has been set to vaporization.")
    eChoice = eVap

powerDraw = eChoice/(time*60)
print ("This will draw %f megawatts (MW) of power..." % (powerDraw/1e6))
print()
cpW = float(input ("How much does 1 kWh (kilowatt hour) cost where you live? Cost:$ "))
cost = cpW * eChoice/3.6e6
print ("This will cost you $%f" % (cost))
