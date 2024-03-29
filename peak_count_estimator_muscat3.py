import numpy as np
import argparse

parser = argparse.ArgumentParser(description=\
'## Peak count estimator for MuSCAT3 ver. 2021 Jul. 22 ##')

parser.add_argument('--band', choices=['g', 'r', 'i', 'z'],\
                     help='band name (g, r, i, or z)', required=True)
parser.add_argument('--mag', type=float, help='SDSS magnitude', required=True)
parser.add_argument('--focus', type=int, choices=[0, 1, 2, 3, 4, 5, 6], help='Focus offset value in mm (0,1,2,3,4,5,or 6)', required=True)
parser.add_argument('--exp', type=float, default=1, help='Exposure time in sec')

args = parser.parse_args()


#-----------
b=[]
nfocus=7

# coefficients for g-band
b.append(np.array((\
10.51276637, 10.2636757,  9.99203702,  9.72257331,  9.51637384,  9.44039911, 9.28810117\
)))

# coefficients for r-band
b.append(np.array((\
10.509745, 10.28773524, 10.23136096,  9.9569031 ,  9.64339266,  9.53424511, 9.35282711\
)))

# coefficients for i-band
b.append(np.array((\
10.24247762, 10.08295809,  9.88549464,  9.57156006,  9.30655855,  9.24200499, 9.05599536\
)))

# coefficients for z-band
b.append(np.array((\
9.84187978, 9.67468481, 9.55641629, 9.25645003, 8.966079  , 8.89227852, 8.70435107\
)))

#-------------
# FWHM values
fwhm=[]
fwhm.append([ 3.0, 3.95666667, 5.91166667, 9.135     ,12.93333333,15.49833333,19.60166667])
fwhm.append([ 3.0, 3.88833333, 4.19666667, 6.24833333,10.24666667,12.75666667,16.68833333])
fwhm.append([ 3.0, 3.50166667, 4.62666667, 7.545     ,11.53833333,13.89833333,17.99333333])
fwhm.append([ 3.0, 3.6       , 4.36333333, 6.81333333,10.76      ,13.35333333,17.45      ])

#-------------
# Gain [e-/ADU]
gain = np.array((1.9, 1.88, 1.8, 2.0)) # z-band for Sophia
#gain = np.array((1.9, 1.88, 1.8, 1.7))

#-------------


bandnum = {'g': 0, 'r': 1, 'i': 2, 'z': 3, 'zs': 3}

if bandnum[args.band]==3:
    logpeak = b[bandnum[args.band]][args.focus] - 0.4*(args.mag-1)
else:
    logpeak = b[bandnum[args.band]][args.focus] - 0.4*args.mag
peak = 10**logpeak * args.exp / 60.

print('\n')
print('====== INPUT ====================================\n')
print('Band: {0}-band'.format(args.band))
print('Mag: {0} (mag)'.format(args.mag))
print('Focus offset: {0} (mm)'.format(args.focus))
print('Exposure time: {0} (s)'.format(args.exp))
print('\n')
print('====== OUTPUT ===================================\n')
print('Gain: {0} (e-/ADU)'.format(gain[bandnum[args.band]]))
print('Estimated peak count: {0} (ADU) or {1} (electrons)'.format(int(peak), int(peak*gain[bandnum[args.band]]) ))
print('Estimated FWHM : {0:.1f} (pixel)\n'.format(fwhm[bandnum[args.band]][args.focus]))
print('=================================================\n')
print('Note:')
print('- The above values are estimated based on images taken under the condistion that airmass was 1.1 and natural seeing was ~0.8". The actual values may vary depending on airmass, sky transparency, and natural seeing.')
print('- Although this script accepts only integers between 0 and 6 as a focus value, decimal numbers are also acceptable to the actual observations.')
#print('- The z-band data were taken with a tentative CCD camera, which is planned to be replaced with a new one which has a higher sensitivity.')
print('- The estimated peak count does not include sky and bias levels. The typical bias level is 500-600 ADU.')
print('\n')
