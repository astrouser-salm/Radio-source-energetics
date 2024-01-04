# Radio-source-energetics

The radio_luminosity.py file obtains the values of radio luminosities of galaxies/jets/diffuse radio lobe emissions. For details, see O'Dea and Owen 1987, Pacholczyk 1970, Ghosh et al. 2023, etc.

The equipartition_Bfield.py file obtains the values of the equipartition magnetic field, particle energy, and total energy. It requires the radio luminosity value, so run the radio_luminosity.py file before this. 

The electron_lifetime.py file obtains the value of electron lifetime considering synchrotron losses and inverse Compton losses off CMB. It requires the equipartition magnetic field value, so run the radio_luminosity.py, and equipartition_Bfield.py files before this.
