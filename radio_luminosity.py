import numpy as np
from uncertainties import ufloat
import math
from decimal import Decimal

#Radio luminosity equation from O'Dea and Owen 1987
def lrad():
    return (1.2*10**27)*(D**2)*(S0)*((ν0)**(-α))*((1+z)**(-(1+α)))*((νu**(1+α))-(νl**(1+α)))*((1+α)**(-1))
#Equation of error in flux densities taken from Kale et al. 2019
def fluxerr():
    return np.sqrt((σ*np.sqrt(Nb))**2+(σabs*S0)**2)  


###############################################################################################################
#####Input parameters from AIPS imastat/tvstat or CASA viewer region statistics
###############################################################################################################

S0=XXXX    #flux density in Jy
σ=XXXX    #rms noise of the image
σabs=0.05   #calculated for uGMRT band-4 (See Kale et al. 2019)
beamarea=XXXX #in pixels  
Npts=XXXX
Nb=Npts/beamarea
ν0=XXXX  #central freq (observing) in Hz
α=ufloat(XXXX,XXXX) #Spectral index with error

###############################################################################################################
#####Input parameters from NASA NED
###############################################################################################################
#Using cosmology of H0 = XXXX km/sec/Mpc, Ωmatter = XXXX, Ωvacuum = XXXX
D=XXXX    #luminosity dist in Mpc
z=XXXX    #redshift
###############################################################################################################

νu=15e9        #upper lim from O'Dea and Owen 1987
νl=100e6       #lower lim from O'Dea and Owen 1987
###############################################################################################################

fluxerr=fluxerr()
S0=ufloat(S0,fluxerr)     #flux density with error
print('Flux density at',ν0/10**9,'GHz =',S0*1000,'mJy')
lrad=lrad()               #total radio luminosity
print('Total radio luminosity =',lrad,'erg/s')
