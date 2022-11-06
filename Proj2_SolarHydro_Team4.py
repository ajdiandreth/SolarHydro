# this program is designed to 
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
energyPumpLoss = ((1/pumpEfficiency) - 1)
mass = waterDensity * flowRatePump * 6
velocityDown = flowRateTurbine / math.pi
velocityUp = flowRatePump / math.pi
height = mass * gravity * (elevationOfBottomRes + 2 + (elevationOfBottomRes/2))
bendCoVel = mass * (bendCoefficientOne * pow(velocityUp, 2)) / 2
bendCoVelTwo = mass * bendCoefficientTwo * pow(velocityUp, 2)
frictionLenVel = mass * (pipeFriction * pipeLength * pow(velocityUp, 2)) / (2 * pipeDiameter)
energyIn = (height + frictionLenVel + bendCoVelTwo + bendCoVel) / energyPumpLoss

