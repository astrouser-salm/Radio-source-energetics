###############################################################################################################
#####Input parameter from NASA NED
###############################################################################################################
a=XXXX  #scale in kpc/arcsec 

###############################################################################################################
#####Input parameters from AIPS imastat/tvstat or CASA viewer region statistics
###############################################################################################################
larc=XXXX    #length of the emission in arcsec
rarc=XXXX  #radius of the emission in arcsec

###############################################################################################################
#These are projected lengths
l=ufloat(a*larc,a*1)   #length of the emission in kpc
r=ufloat(a*rarc,a*0.5) #radius of the emission in kpc
V=np.pi*r**2*l         #Volume considering the source as a cylinder
print('Volume of the source =',V, 'kpc\u00b3') #in kpc^3

def kpctocm(V):     #conversion to cgs  
    return V*(3.086e21)**3
Vcm=kpctocm(V)
print('Volume of the source =',Vcm,'cm\u00b3') #in cm^3

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

#Equipartition magnetic field, minimum energy equations taken from O'Dea and Owen 1987
def Bmin():
    return (((2*np.pi)*(1+k)*c12*(phi**(-1))*lrad)**(2/7))*(Vcm**(-2/7))
def Emin():
    return ((c12*(1+k)*lrad)**(4/7))*((Vcm*phi)**(3/7))*((2*np.pi)**(-3/7))

#Finding out the suitable values of c12 and c13 functions 
def find_closest(val_obs, val_theory):
    return min(val_theory, key=lambda x: abs(x - val_obs))
ν_lim=[1e10,1e11]
#c12, c13 values taken from Pacholczyk 1970  #considering S=ν^α
α_theory=[-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,-1.0,-1.1,-1.2]
c12_theory_ν10=[2.5e7,2.8e7,3.2e7,3.7e7,4.5e7,5.4e7,6.5e7,7.8e7,9.3e7,1.1e8,1.3e8]
c12_ν10=interp1d(α_theory,c12_theory_ν10,kind='linear', fill_value='extrapolate')
c13_theory_ν10=[1.6e4,1.7e4,1.8e4,2.0e4,2.2e4,2.5e4,2.7e4,3.0e4,3.3e4,3.6e4,4.0e4]   #c13 ~ c12^(4/7)
c13_ν10=interp1d(α_theory,c13_theory_ν10,kind='linear', fill_value='extrapolate')
c12_theory_ν11=[8.3e6,9.8e6,1.2e7,1.6e7,2.0e7,2.8e7,3.9e7,5.4e7,7.1e7,9.3e7,1.1e8]
c12_ν11=interp1d(α_theory,c12_theory_ν11,kind='linear', fill_value='extrapolate')
c13_theory_ν11=[8.3e3,9.1e3,1.0e4,1.2e4,1.4e4,1.7e4,2.0e4,2.4e4,2.8e4,3.3e4,3.7e4]
c13_ν11=interp1d(α_theory,c13_theory_ν11,kind='linear', fill_value='extrapolate')
#plt.plot(α_theory,c12_theory)

###############################################################################################################
#####Input parameters from AIPS imastat/tvstat or CASA viewer region statistics
###############################################################################################################
α_abs=XXXX #Value of spectral index without error
###############################################################################################################

if find_closest(νu,ν_lim)==1e10:
    c12=c12_ν10(α_abs)
    c13=c13_ν10(α_abs)
else:
    c12=c12_ν11(α_abs)
    c13=c13_ν11(α_abs)
    
###############################################################################################################
#####Assumptions. See O'Dea and Owen 1987 for details
###############################################################################################################    
k=1
phi=1
###############################################################################################################

print('c12 value used =',c12)
print('c13 value used =',c13)
Bmin=Bmin()
print('Equipartition magnetic field value =', Bmin*10**6,'μG')
Emin=Emin()
print('Particle energy at minimum pressure =', Emin,'erg')
print('Total energy of the galaxy (particles+fields) =',1.25*Emin) #see O'Dea and Owen 1987


