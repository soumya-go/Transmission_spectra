#--------- Reading userInput.in file --------#
import numpy as np,sys,os

#----------- constants definition ---------#
# Everything is in SI units
c_light = 2.99792458e+08	# speed of light (m/s^2)
h_planck = 6.6260755e-34	# Planck constant (Js)
K_botz = 1.38e-23		# Boltzmann constant (J/K)
m_electron = 9.1093e-31		# mass of electron (kg)
q_electron = 1.602177e-19	# charge of electron (C)
amu = 1.6605402e-27  		# Atomic mass unit [kg]           
m_Hatom = 1.673725e-27   	# H atom mass [kg]                
N_avogadro = 6.0221420e+23	# Avogadro's number [1/mol]   
R_gas = 8.314472e+00   		# Ideal gas const. [J/mol/K]      
Sigma = 5.6704e-08     		# Stef.-Boltz. const. [W/m^2/K^4] */
NL = 2.6867774e+25  		# Loschmidt constant in [m^-3]    */

#---- Unit conversions --------------------------------------------- */

NM_TO_M = 1.0e-09
CM_TO_M = 1.0e-02
KM_TO_M = 1.0e+03
MICRON_TO_NM = 1.0e+03 
ERG_TO_JOULE = 1.0e-07
CAL_TO_JOULE = 4.1840
G_TO_KG = 1.0e-03
ATM_TO_PA = 1.01325e+05


#----------- End -------------#
def ReadInput():
	fl1=open("userInput.in","r")
	A1=fl1.readlines()
	for a in A1:
		B=a.split()
		if B[0]!="#":
			if B[0]=="pwd":
				pwd=B[2]
			if B[0]=="TP":
				TP=B[2]
			if B[0]=="EOS":
				EOS=B[2]
			if B[0]=="output":
				output_file=B[2]
			if B[0]=="grav":
				grav=float(B[2])
			if B[0]=="R_pl":
				R_pl=float(B[2])
			if B[0]=="R_st":
				R_st=float(B[2])
			if B[0]=="P_cloud":
				P_cloud=float(B[2])
			if B[0]=="R_scat":
				R_scat=float(B[2])
			if B[0]=="T_irr":
				T_irr=float(B[2])
			if B[0]=="met":
				met=float(B[2])

	#-------- Reading selectInput.in -----------#

	fl2=open("selectChem.in","r")
	A2=fl2.readlines()
	C1=["CH4","CO2","CO","H2O","NH3","O2","O3","C2H2","C2H4","C2H6","H2CO","H2S","HCl","HCN","HF","MgH","N2","NO","NO2","OCS","OH","PH3","SH","SiH","SiO","SO2","TiO","VO","Na","K","Scattering,Collision Induced Absorption"]
	Chem_comp=[]#np.zeros_like(C1)

	for a in A2:
		B=a.split()
		if B[0]!="#":
			for j in range(len(C1)):
				if B[0]==C1[j]:
					Chem_comp.append(int(B[2]))
		#------- Reading otherInput.in file --------@		
	fl3=open("otherInput.in","r")
	A3=fl3.readlines()
	opac_list=[]
	for a in A3:
		B=a.split()
		if B[0]!="#":
			if B[0]=="T_lines":
				T_lines=float(B[2])
			if B[0]=="T_min":
				T_min=float(B[2])
			if B[0]=="T_max":
				T_max=float(B[2])
			if B[0]=="P_lines":
				P_lines=float(B[2])
			if B[0]=="P_min":
				P_min=float(B[2])
			if B[0]=="P_max":
				P_max=float(B[2])
			if B[0]=="wave_lines":
				wave_lines=int(B[2])
			if B[0]=="layer":
				layer=int(B[2])
		D=a.split("/")		
		if D[0]=="":
			opac_list.append(a)
	parameters=[grav,R_pl,R_st,P_cloud,R_scat,T_irr,met,T_lines,T_min,T_max,P_lines,P_min,P_max,wave_lines,layer]
	return pwd,TP,EOS,output_file,parameters,Chem_comp,opac_list
	
if __name__=="__main__":
	pwd,TP,EOS,output_file,parameters,Chem_comp,opac_list=ReadInput()
