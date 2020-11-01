# peak_count_estimator
## Peak count estimator for MuSCAT3

usage: python peak_count_estimator_muscat3.py [-h] --band {g,r,i,z} --mag MAG --focus {1,2,3,4,5,6} [--exp EXP]


optional arguments:

  -h, --help              : show this help message and exit

  --band {g,r,i,z}        : band name (g, r, i, or z)
  
  --mag MAG               : SDSS magnitude
  
  --focus {1,2,3,4,5,6}   : Focus offset value in mm (1,2,3,4,5,or 6)
  
  --exp EXP               : Exposure time in sec


Notes:
- This script estimates the peak count and FWHM based on images taken under a condistion of airmass=1.1 and natural seeing ~ 0.8".
  The actual peak count and FWHM may vary depending on airmass and natural seeing.
- The z-band data were taken with a tentative CCD camera, which is planned to be replaced with a new one which has a higher sensitivity.
- The estimated peak count does not include sky and bias levels. The typical bias level is 500-600 ADU.


Author: Akihiko Fukui
