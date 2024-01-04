#Electron lifetime equation taken from van der Laan and perola 1969, O'Dea and Owen 1987
BR=(4*(1+z)**2)*10**(-6) #in Gauss (See van der Laan and perola 1969)
def t():
    return ((2.6*10**4)*B**0.5)/((B**2+BR**2)*((1+z)*ν0)**0.5)
B=Bmin             
t=t()
print('Electron lifetime =',t,'yr')
