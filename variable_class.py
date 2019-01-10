class variables:
	NTAU=0; NTEMP=0; TLOW=0.0; THIGH=0.0; NPRESSURE = 0.0; PLOW=0.0; PHIGH = 0.0; THRESHOLD = 0.0;
	RAYLEIGH = 0; TEFF=0.0; METAL = 0.0; NLAMBDA = 0; G=0.0; R_PLANET = 0; R_STAR = 0.0; T_STAR = 0.0;
class atmos:
	lamda=[]; T=[]; P=[]; mu=[]

# opacity file
class Opac: 
	name = []; NP = 0; NT = 0
	# ***kappa, **abundance;
  	P = []; Plog10 = []; T = []

# --- Chemistry structure ------------------------------------------ */

"""struct Chem {
  double **total, **C, **CH4, **CO, **CO2, **C2H2, **C2H4, **C2H6, **H, 
    **HCN, **HCl, **HF, **H2, **H2CO, **H2O, **H2S, **He, **K, **MgH, 
    **N, **N2, **NO2, **NH3, **NO, **Na, **O, **O2, **O3, **OH, **OCS, 
    **PH3, **SH, **SO2, **SiH, **SiO, **TiO, **VO, **mu;
  double *P, *T;
};"""
	
if __name__=="__main__":
	print Opac.NT
