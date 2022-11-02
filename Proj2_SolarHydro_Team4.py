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

