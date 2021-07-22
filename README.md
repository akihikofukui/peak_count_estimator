# peak_count_estimator
## Peak count estimator for MuSCAT3

usage: python peak_count_estimator_muscat3.py [-h] --band {g,r,i,z} --mag MAG --focus {0,1,2,3,4,5,6} [--exp EXP]


optional arguments:

  -h, --help              : show this help message and exit

  --band {g,r,i,z}        : band name (g, r, i, or z)
  
  --mag MAG               : SDSS magnitude
  
  --focus {0,1,2,3,4,5,6} : Focus offset value in mm (0,1,2,3,4,5,or 6)
  
  --exp EXP               : Exposure time in sec


Notes:
- This script estimates the peak count and FWHM based on images taken under the condistion that airmass was 1.1 and natural seeing was ~0.8".
  The actual values may vary depending on airmass, sky transparency, and natural seeing.
- Although this script accepts only integers between 0 and 6 as a focus value, decimal numbers are also acceptable to the actual observations.
- The estimated peak count does not include sky and bias levels. The typical bias level is 500-600 ADU.


Author: Akihiko Fukui (The University of Tokyo)
(Email: afukui @ g.ecc.u-tokyo.ac.jp)

Last update: July 22, 2021
