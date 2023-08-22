import math
import numpy as np

###############################################################################
# Definition of the input
###############################################################################

# Geometry
# Plate width in [m]
B = 0.2
# Plate spacing in [m]
S = 2
        
#Soil properties
# Young modulus in [kPa]
E = 8*1000
#Poisson's ratio [dimensionless]
nu = 0.3
#Cohesion in [kPa]
c   = 1
# Friction angle in [rad]
phi = 40*math.pi/180
# Dilatancy angle in [rad]
psi = 12*math.pi/180
# Unit weight in [kN/m3]
gam = 17
        
#Wire mesh properties
# Axial stiffness in [kN/m]
J   = 2*1000  
# Axial strength in [kN/m]
ty  = 105     

#number of calculation steps
Nmax = 1000


###############################################################################
# calculation of additional parameters 
# necessary for the meta-model integration
###############################################################################

# Simple shear failure parameters
c_ss   = c*(math.cos(phi)*math.cos(psi)/(1-math.sin(phi)*math.sin(psi)))
phiss  = math.atan(math.sin(phi)*math.cos(psi)/(1-math.sin(phi)*math.sin(psi)))

# Parameters for the evolution of B*
b1 = 4.9-(0.9)*(1-math.exp(-1.8*(c_ss/gam/B)/(0.9)))
b2 = 0.85185*(J/B)/E + 0.3804
b3 = 45

# Initial slope of load-displacement curve
R0  = E*B/((1-nu**2)*0.85)

# Bearing capacity coefficients
Nq  = (1+math.sin(phiss))/(1-math.sin(phiss))*math.exp(math.pi*math.tan(phiss))
Nc  = (Nq-1)/math.tan(phiss)
Ng  = 2*(Nq+1)*math.tan(phiss) 
sq  = 1 + 0.1*(1+math.sin(phiss))/(1-math.sin(phiss))
sg  = 1 + 0.1*(1+math.sin(phiss))/(1-math.sin(phiss))
sc  = 1 + 0.2*(1+math.sin(phiss))/(1-math.sin(phiss))

# Parameters for the evolution of tensile force in the wire mesh
t1 = 0.2176
t2 = 1/3
t3 = 3/2

# Definition of wire mesh yield point
Ty  = ty*B
uy = B*(Ty/(t1*J*B*(E*B/J)**t2))**(1/t3)



###############################################################################       
# Initialization  of the calculation variable
###############################################################################

# Displacement increment
du  = uy/Nmax
# Displacements
u   = np.zeros((Nmax+1,1))
# Retaining force
F   = np.zeros((Nmax+1,1))
# Wire mesh tensile force
T   = np.zeros((Nmax+1,1))
# Deformable foundation dimension 
Bst = np.zeros((Nmax+1,1))
Bst[0] = B

###############################################################################       
# Calculation
###############################################################################

for i in range(1,Nmax+1):
    
    # Updating the displacement
    u[i] = u[i-1] + du
    

    # Updating the coefficients for adjacent plate
    ac =  ( 2.44/(S/Bst[i-1]-1)**2.5-math.exp(-0.32*(S/Bst[i-1]-1))+1) 
    aq =  ( 2.44/(S/Bst[i-1]-1)**2.5-math.exp(-0.32*(S/Bst[i-1]-1))+1)
    ag =  ( 0.98/(S/Bst[i-1]-1)**2.5-math.exp(-0.8*(S/Bst[i-1]-1))+1)
    
    # Calculating the bearing capacity
    qlim = c_ss*Nc*ac*sc + 1/2*Bst[i-1]*gam*Ng*ag*sg+sq*Nq*aq*u[i]*gam
    # Calculating the limit load
    Vlim = qlim*Bst[i-1]*Bst[i-1]
    
    # Calculating the increment in retaining force
    dF = R0*(1-F[i-1]/Vlim)*du
    # Updating the retaining force
    F[i]  = F[i-1]  + dF   

    # Updating the deformable foundation dimension
    Bst[i] = B+(b1*u[i]+b2*B)*(1-math.exp(-b3*u[i]/(b1*u[i]+b2*B)));

    # Calculating the wire mesh tensile force
    T[i]=t1*J*B*(E/J*B)**(t2)*(u[i]/B)**t3
            


###############################################################################       
# Output
###############################################################################

# Maximum retaining force in [kN]
Fmax  = np.round( F[Nmax])

# Maximum retaining force per unit area in [kPa]
pmax  = np.round( F[Nmax]/(S**2))

print('')
print('**********************************************************')
print('Output')
print('**********************************************************')
print('')
print('The maximum retaining force is equal to', str(Fmax).replace(' [', '').replace('[', '').replace(']', '') , 'kN')
print('The maximum retaining force per unit area is equal to', str(pmax).replace(' [', '').replace('[', '').replace(']', '') , 'kPa')
print('')
print('**********************************************************')
