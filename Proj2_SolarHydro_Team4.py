# this program is designed to calculate and output the surface area of the resevoir, the maximum system efficiency and system efficiency, the input energy, the times to 
# fill/empty, and the energy out after twelve hours.
import math

# constants
energyOut = 120
gravity = 9.81
waterDensity = 1000
radiusRes = 112.5

# user-input variables
pE = input('Pump Efficiency value (unitless): ')
fRP = input('Pump Flow Volume (m^3/s): ')
pD = input('Pipe Diameter (m): ')
pL = input('Pipe Length (m): ')
pF = input('Pipe Friction Factor (unitless): ')
rD = input('Depth of Reservoir (m): ')
eBR = input('Elevation of Reservoir (m): ')
bCO = input('Bend Coefficient 1 (K1, unitless): ')
bCT = input('Bend Coefficient 2 (K2, unitless): ')
tE = input('Turbine Efficiency value (unitless): ')
fRT = input('Turbine Flow Volume (m^3/s): ')

# set user-inputs to decimal values.
pumpEfficiency = float(pE)
flowRatePump = float(fRP)
pipeDiameter = float(pD)
pipeLength = float(pL)
pipeFriction = float(pF)
reservoirDepth = float(rD)
elevationOfBottomRes = float(eBR)
bendCoefficientOne = float(bCO)
bendCoefficientTwo = float(bCT)
turbineEfficiency = float(tE)
flowRateTurbine = float(fRT)

# calculations
resSurfArea = 2*(math.pi * math.pow(radiusRes, 2)) + 2*(math.pi*radiusRes*reservoirDepth)
energyOutJ = energyOut * (3.6 * math.pow(10, 9))
resSurfArea = 2*(math.pi * math.pow(radiusRes, 2)) + 2*(math.pi*radiusRes*reservoirDepth)
usableWaterVolume = math.pi * math.pow(radiusRes, 2) * (reservoirDepth - pipeDiameter)
usableWaterMass = usableWaterVolume * waterDensity
turbineOneLoss = energyOutJ / (1 - ((1/.89)-1))
velocityOneDown = (energyOutJ + turbineOneLoss - (usableWaterMass * (gravity * (elevationOfBottomRes + reservoirDepth - 2)))/(-(((pipeFriction * pipeLength) /4 ) + bendCoefficientTwo + (bendCoefficientOne / 2))
if velocityOneDown <= 0:
    print("Not enough energy stored for given energy losses.")
else:
    volumetricFlowDownOne = velocityOneDown * ((pipeDiameter/2)^2) * math.pi
    timeDownOne = (((usableWaterVolume / volumetricFlowDownOne) / 60) / 60)
    if timeDownOne > 12:
        print("To long.")
    elif timeDownOne <= 12 and timeDownOne > 10:
        fillTime = (((usableWaterVolume / flowRatePump) / 60) / 60)
        velocityUp = flowRatePump / (((pipeDiameter/2)^2) * math.pi)
        energyInJ = (usableWaterMass((gravity * (elevationOfBottomRes + reservoirDepth - 2)) - (pipeFriction * pipeLength * ((velocityUp^2)/2)) - (bendCoefficientTwo * velocityUp^2) - ((bendCoefficientOne * velocityUp^2)/2))) / (1 - (1 - pumpEfficiency))
        energyIn = energyInJ / (3.6 * math.pow(10, 9))
        systemEfficiency = energyOut / energyIn
        print("Reservoir Surface Area: ", resSurfArea)
        print("Input Energy: ", energyIn)
        print("System Efficiency: ", systemEfficiency)
        print("Time to fill: ", fillTime)
        print("Time to empty: ", timeDownOne)
    elif timeDownOne <= 10:
        volumetricFlowDownTwo = usableWaterVolume / (12 * 60 * 60)
        velocityTwoDown = volumetricFlowDownTwo / (((pipeDiameter/2)^2) * math.pi)
        energyOutTwelveHourJ = (usableWaterMass((gravity * (elevationOfBottomRes + reservoirDepth - 2)) - (pipeFriction * pipeLength * ((velocityTwoDown^2)/2)) - (bendCoefficientTwo * velocityTwoDown^2) - ((bendCoefficientOne * velocityTwoDown^2)/2))) / (1 + ((1/turbineEfficiency)-1))
        energyoutTwelveHour = energyOutTwelveHourJ / (3.6 * math.pow(10, 9))
        fillTime = (((usableWaterVolume / flowRatePump) / 60) / 60)
        velocityUp = flowRatePump / (((pipeDiameter/2)^2) * math.pi)
        energyInJ = (usableWaterMass((gravity * (elevationOfBottomRes + reservoirDepth - 2)) - (pipeFriction * pipeLength * ((velocityUp^2)/2)) - (bendCoefficientTwo * velocityUp^2) - ((bendCoefficientOne * velocityUp^2)/2))) / (1 - (1 - pumpEfficiency))
        energyIn = energyInJ / (3.6 * math.pow(10, 9))
        systemEfficiency = energyOut / energyIn
        maxSystemEfficiency = energyoutTwelveHour / energyIn
    
       # outputs                                                                                                                       
        print("Reservoir Surface Area: ", resSurfArea)
        print("Input Energy: ", energyIn)
        print("System Efficiency: ", systemEfficiency)
        print("Max System Efficiency: ", maxSystemEfficiency)
        print("Time to fill: ", fillTime)
        print("Time to empty: ", timeDownOne)
        print("Energy out if emptied over 12 hours: ", energyoutTwelveHour)
