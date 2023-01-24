#!/usr/bin/python
import optparse
import operator
import os
import sys

###WANT COLUMNS
#NAME, DATE, ROINAME

###DLBP_RAD 4 AND 50 AND 66
#FOR RAD4:  TOT_DEN, TOT_A, TRAB_A, CRTSUB_DEN, CRTSUB_A, TRAB_DEN
#FOR RAD50 AND 66: CRT_DEN, CRT_A, CRT_THK, PERI, ENDO

###DLPB_TIB TIB4,38,66
#FOR TIB4: TOT_DEN, TOT_A, TRAB_A, CRTSUB_DEN, CRTSUB_A, TRAB_DEN
#FOR TIB38 AND 66: CRT_DEN, CRT_A, CRT_THK, PERI, ENDO

###RAD_SSI RAD50 AND 66
#FOR RAD50 AND RAD66: RP_CM_W

###TIB_SSI TIB38 AND TIB66
#FOR TIB38 AND TIB66: RP_CM_W

parser = optparse.OptionParser()
parser.add_option("--dlpbrad", action="store",dest="dlpbrad") #Path to DLPB_RAD.csv
parser.add_option("--dlpbtib", action="store",dest="dlpbtib") #Path to DLPB_TIB.csv
parser.add_option("--radssi", action="store",dest="radssi") #Path to RAD_SSI.csv
parser.add_option("--tibssi", action="store",dest="tibssi") #Path to TIB_SSI.csv
parser.add_option("--dlpbbdllc", action="store",dest="dlpbbdllc") #Path to DLPB_P_E_BDLLC_V2.csv
parser.add_option("--studyid", action="store",dest="studyid") #Path to name and MRN 
parser.add_option("-o", "--outfile", action="store",dest="outfilename") #outfile name
options, args = parser.parse_args()

pqct_visit={}
name_to_studyid={}

if options.studyid != None:
	with open(options.studyid, "r") as f:
		study_IDs = [x for x in f.readlines()]
		for line1 in study_IDs:
			line=line1.rstrip().split(",")
			patient_name=(line[1])
			patient_study_ID=(line[0])
			name_to_studyid[patient_name]=[patient_study_ID]

if options.dlpbrad != None:
	with open(options.dlpbrad, "r") as f:
		DLPB_RAD_lines = [x for x in f.readlines()]
		for DLPB_line1 in DLPB_RAD_lines:
			if "ROINAME" in DLPB_line1:
				NAME=DLPB_line1.split(",").index("NAME")
				DATE=DLPB_line1.split(",").index("DATE")
				ROI_TYPE=DLPB_line1.split(",").index("ROINAME")
				TOT_DEN=DLPB_line1.split(",").index("TOT_DEN")
				TOT_A=DLPB_line1.split(",").index("TOT_A")
				TRAB_A=DLPB_line1.split(",").index("TRAB_A")
				CRTSUB_DEN=DLPB_line1.split(",").index("CRTSUB_DEN")
				CRTSUB_A=DLPB_line1.split(",").index("CRTSUB_A")
				TRAB_DEN=DLPB_line1.split(",").index("TRAB_DEN")
				CRT_DEN=DLPB_line1.split(",").index("CRT_DEN")
				CRT_A=DLPB_line1.split(",").index("CRT_A")
				CRT_THK_C=DLPB_line1.split(",").index("CRT_THK_C")
				PERI=DLPB_line1.split(",").index("PERI")
				ENDO=DLPB_line1.split(",").index("ENDO")
				PATNO=DLPB_line1.split(",").index("PATNO")

			elif "ROINAME" not in DLPB_line1:
				name=DLPB_line1.split(",")[NAME]
				date=DLPB_line1.split(",")[DATE]
				roi_type=DLPB_line1.split(",")[ROI_TYPE]
				tot_den=DLPB_line1.split(",")[TOT_DEN]
				tot_a=DLPB_line1.split(",")[TOT_A]
				trab_a=DLPB_line1.split(",")[TRAB_A]
				crtsub_den=DLPB_line1.split(",")[CRTSUB_DEN]
				crtsub_a=DLPB_line1.split(",")[CRTSUB_A]
				trab_den=DLPB_line1.split(",")[TRAB_DEN]
				crt_den=DLPB_line1.split(",")[CRT_DEN]
				crt_a=DLPB_line1.split(",")[CRT_A]
				crt_thk=DLPB_line1.split(",")[CRT_THK_C]
				peri=DLPB_line1.split(",")[PERI]
				endo=DLPB_line1.split(",")[ENDO]		
				patno=DLPB_line1.split(",")[PATNO]


				if name in name_to_studyid:
					study_id=name_to_studyid[name][0]
				else:
					study_id=None

				visit_id=str(patno+','+date)
				if visit_id not in pqct_visit:
					pqct_visit[visit_id]={'name':name,
					'date':date,
					'study_id':study_id,
					'patno':patno,
					'endo_area_tib38':None,
					'endo_den_tib38':None,
					'endo_area_tib66':None,
					'endo_den_tib66':None,
					'tot_a_rad4':None,
					'tot_den_rad4':None,
					'trab_a_rad4':None,
					'crtsub_den_rad4':None,
					'crtsub_a_rad4':None,
					'trab_den_rad4':None,
					'crt_den_rad50':None,
					'crt_a_rad50':None,
					'mean_cort_thk_c_rad50':None,
					'peri_c_rad50':None,
					'endo_c_rad50':None,
					'ssi_polar_rad50':None,
					'crt_den_rad66':None,
					'crt_a_rad66':None,
					'mean_cort_thk_rad66':None,
					'peri_c_rad66':None,
					'endo_c_rad66':None,
					'ssi_polar_rad66':None,
					'tot_den_tib4':None,
					'tot_a_tib4':None,
					'trab_a_tib4':None,
					'crtsub_den_tib4':None,
					'crtsub_a_tib4':None,
					'trab_den_tib4':None,
					'crt_den_tib38':None,
					'crt_a_tib38':None,
					'mean_cort_thk_c_tib38':None,
					'peri_c_tib38':None,
					'endo_tib38':None,
					'ssi_polar_tib38':None,
					'crt_den_tib66':None,
					'crt_a_tib66':None,
					'cort_thk_c_tib66':None,
					'peri_c_tib66':None,
					'endo_c_tib66':None,
					'rp_cm_w_tib66':None,
					'form_19_pqct_results_revised_complete':None}
				else:
					print("already exists - no new entry")
				
				if roi_type=="RAD4":
					pqct_visit[visit_id].update({'tot_a_rad4':tot_a,'tot_den_rad4':tot_den,'trab_a_rad4':trab_a,'crtsub_den_rad4':crtsub_den,'crtsub_a_rad4':crtsub_a,'trab_den_rad4':trab_den})
				elif roi_type=="RAD50":
					pqct_visit[visit_id].update({'crt_den_rad50':crt_den,'crt_a_rad50':crt_a,'mean_cort_thk_c_rad50':crt_thk,'peri_c_rad50':peri,'endo_c_rad50':endo})
				elif roi_type=="RAD66":
					pqct_visit[visit_id].update({'crt_den_rad66':crt_den,'crt_a_rad66':crt_a,'mean_cort_thk_rad66':crt_thk,'peri_c_rad66':peri,'endo_c_rad66':endo})

if options.dlpbtib != None:
	with open(options.dlpbtib, "r") as f:
		DLPB_TIB_lines = [x for x in f.readlines()]
		for DLPB_line1 in DLPB_TIB_lines:
			if "ROINAME" in DLPB_line1:
				NAME=DLPB_line1.split(",").index("NAME")
				DATE=DLPB_line1.split(",").index("DATE")
				ROI_TYPE=DLPB_line1.split(",").index("ROINAME")
				TOT_DEN=DLPB_line1.split(",").index("TOT_DEN")
				TOT_A=DLPB_line1.split(",").index("TOT_A")
				TRAB_A=DLPB_line1.split(",").index("TRAB_A")
				CRTSUB_DEN=DLPB_line1.split(",").index("CRTSUB_DEN")
				CRTSUB_A=DLPB_line1.split(",").index("CRTSUB_A")
				TRAB_DEN=DLPB_line1.split(",").index("TRAB_DEN")
				CRT_DEN=DLPB_line1.split(",").index("CRT_DEN")
				CRT_A=DLPB_line1.split(",").index("CRT_A")
				CRT_THK_C=DLPB_line1.split(",").index("CRT_THK_C")
				PERI=DLPB_line1.split(",").index("PERI")
				ENDO=DLPB_line1.split(",").index("ENDO")
				PATNO=DLPB_line1.split(",").index("PATNO")

			elif "ROINAME" not in DLPB_line1:
				name=DLPB_line1.split(",")[NAME]
				date=DLPB_line1.split(",")[DATE]
				roi_type=DLPB_line1.split(",")[ROI_TYPE]
				tot_den=DLPB_line1.split(",")[TOT_DEN]
				tot_a=DLPB_line1.split(",")[TOT_A]
				trab_a=DLPB_line1.split(",")[TRAB_A]
				crtsub_den=DLPB_line1.split(",")[CRTSUB_DEN]
				crtsub_a=DLPB_line1.split(",")[CRTSUB_A]
				trab_den=DLPB_line1.split(",")[TRAB_DEN]
				crt_den=DLPB_line1.split(",")[CRT_DEN]
				crt_a=DLPB_line1.split(",")[CRT_A]
				crt_thk=DLPB_line1.split(",")[CRT_THK_C]
				peri=DLPB_line1.split(",")[PERI]
				endo=DLPB_line1.split(",")[ENDO]		
				patno=DLPB_line1.split(",")[PATNO]
				
				if name in name_to_studyid:
					study_id=name_to_studyid[name][0]
				else:
					study_id=None

				visit_id=str(patno+','+date)
				if visit_id not in pqct_visit:
					pqct_visit[visit_id]={'name':name,
					'date':date,
					'study_id':study_id,
					'patno':patno,
					'endo_area_tib38':None,
					'endo_den_tib38':None,
					'endo_area_tib66':None,
					'endo_den_tib66':None,
					'tot_a_rad4':None,
					'tot_den_rad4':None,
					'trab_a_rad4':None,
					'crtsub_den_rad4':None,
					'crtsub_a_rad4':None,
					'trab_den_rad4':None,
					'crt_den_rad50':None,
					'crt_a_rad50':None,
					'mean_cort_thk_c_rad50':None,
					'peri_c_rad50':None,
					'endo_c_rad50':None,
					'ssi_polar_rad50':None,
					'crt_den_rad66':None,
					'crt_a_rad66':None,
					'mean_cort_thk_rad66':None,
					'peri_c_rad66':None,
					'endo_c_rad66':None,
					'ssi_polar_rad66':None,
					'tot_den_tib4':None,
					'tot_a_tib4':None,
					'trab_a_tib4':None,
					'crtsub_den_tib4':None,
					'crtsub_a_tib4':None,
					'trab_den_tib4':None,
					'crt_den_tib38':None,
					'crt_a_tib38':None,
					'mean_cort_thk_c_tib38':None,
					'peri_c_tib38':None,
					'endo_tib38':None,
					'ssi_polar_tib38':None,
					'crt_den_tib66':None,
					'crt_a_tib66':None,
					'cort_thk_c_tib66':None,
					'peri_c_tib66':None,
					'endo_c_tib66':None,
					'rp_cm_w_tib66':None,
					'form_19_pqct_results_revised_complete':None}
				else:
					print("already exists - no new entry")
				
				if roi_type=="TIB4":
					pqct_visit[visit_id].update({'tot_a_tib4':tot_a,'tot_den_tib4':tot_den,'trab_a_tib4':trab_a,'crtsub_den_tib4':crtsub_den,'crtsub_a_tib4':crtsub_a,'trab_den_tib4':trab_den})
				elif roi_type=="TIB38":
					pqct_visit[visit_id].update({'crt_den_tib38':crt_den,'crt_a_tib38':crt_a,'mean_cort_thk_c_tib38':crt_thk,'peri_c_tib38':peri,'endo_tib38':endo})
				elif roi_type=="TIB66":
					pqct_visit[visit_id].update({'crt_den_tib66':crt_den,'crt_a_tib66':crt_a,'cort_thk_c_tib66':crt_thk,'peri_c_tib66':peri,'endo_c_tib66':endo})

if options.radssi != None:
	with open(options.radssi, "r") as f:
		RAD_SSI_lines = [x for x in f.readlines()]
		for SSI_line1 in RAD_SSI_lines:
			if "ROINAME" in SSI_line1:
				NAME=SSI_line1.split(",").index("NAME")
				DATE=SSI_line1.split(",").index("DATE")
				ROI_TYPE=SSI_line1.split(",").index("ROINAME")
				RP_CM_W=SSI_line1.split(",").index("RP_CM_W")
				PATNO=SSI_line1.split(",").index("PATNO")

			elif "ROINAME" not in SSI_line1:
				name=SSI_line1.split(",")[NAME]
				date=SSI_line1.split(",")[DATE]
				roi_type=SSI_line1.split(",")[ROI_TYPE]
				rp_cm_w=SSI_line1.split(",")[RP_CM_W]	
				patno=SSI_line1.split(",")[PATNO]
				
				
				visit_id=str(patno+','+date)
				# print(visit_id)
				if name in name_to_studyid:
					study_id=name_to_studyid[name][0]
				else:
					study_id=None

				if visit_id not in pqct_visit:
					pqct_visit[visit_id]={'name':name,
					'date':date,
					'study_id':study_id,
					'patno':patno,
					'endo_area_tib38':None,
					'endo_den_tib38':None,
					'endo_area_tib66':None,
					'endo_den_tib66':None,
					'tot_a_rad4':None,
					'tot_den_rad4':None,
					'trab_a_rad4':None,
					'crtsub_den_rad4':None,
					'crtsub_a_rad4':None,
					'trab_den_rad4':None,
					'crt_den_rad50':None,
					'crt_a_rad50':None,
					'mean_cort_thk_c_rad50':None,
					'peri_c_rad50':None,
					'endo_c_rad50':None,
					'ssi_polar_rad50':None,
					'crt_den_rad66':None,
					'crt_a_rad66':None,
					'mean_cort_thk_rad66':None,
					'peri_c_rad66':None,
					'endo_c_rad66':None,
					'ssi_polar_rad66':None,
					'tot_den_tib4':None,
					'tot_a_tib4':None,
					'trab_a_tib4':None,
					'crtsub_den_tib4':None,
					'crtsub_a_tib4':None,
					'trab_den_tib4':None,
					'crt_den_tib38':None,
					'crt_a_tib38':None,
					'mean_cort_thk_c_tib38':None,
					'peri_c_tib38':None,
					'endo_tib38':None,
					'ssi_polar_tib38':None,
					'crt_den_tib66':None,
					'crt_a_tib66':None,
					'cort_thk_c_tib66':None,
					'peri_c_tib66':None,
					'endo_c_tib66':None,
					'rp_cm_w_tib66':None,
					'form_19_pqct_results_revised_complete':None}
				else:
					print("already exists - no new entry")
				# print(pqct_visit[visit_id]['name'])	

				if roi_type=="RAD50":
					#FOR RAD50 AND RAD66: RP_CM_W
					pqct_visit[visit_id].update({'ssi_polar_rad50':rp_cm_w})
				elif roi_type=="RAD66":
					#FOR RAD50 AND RAD66: RP_CM_W
					pqct_visit[visit_id].update({'ssi_polar_rad66':rp_cm_w})

if options.tibssi != None:
	with open(options.tibssi, "r") as f:
		TIB_SSI_lines = [x for x in f.readlines()]
		for SSI_line1 in TIB_SSI_lines:
			if "ROINAME" in SSI_line1:
				NAME=SSI_line1.split(",").index("NAME")
				DATE=SSI_line1.split(",").index("DATE")
				ROI_TYPE=SSI_line1.split(",").index("ROINAME")
				RP_CM_W=SSI_line1.split(",").index("RP_CM_W")
				PATNO=SSI_line1.split(",").index("PATNO")
			
			elif "ROINAME" not in SSI_line1:
				name=SSI_line1.split(",")[NAME]
				date=SSI_line1.split(",")[DATE]
				roi_type=SSI_line1.split(",")[ROI_TYPE]
				rp_cm_w=SSI_line1.split(",")[RP_CM_W]	
				patno=SSI_line1.split(",")[PATNO]
				
				visit_id=str(patno+','+date)
				
				# print(visit_id)
				if name in name_to_studyid:
					study_id=name_to_studyid[name][0]
				else:
					study_id=None

				if visit_id not in pqct_visit:
					pqct_visit[visit_id]={'name':name,
					'date':date,
					'study_id':study_id,
					'patno':patno,
					'endo_area_tib38':None,
					'endo_den_tib38':None,
					'endo_area_tib66':None,
					'endo_den_tib66':None,
					'tot_a_rad4':None,
					'tot_den_rad4':None,
					'trab_a_rad4':None,
					'crtsub_den_rad4':None,
					'crtsub_a_rad4':None,
					'trab_den_rad4':None,
					'crt_den_rad50':None,
					'crt_a_rad50':None,
					'mean_cort_thk_c_rad50':None,
					'peri_c_rad50':None,
					'endo_c_rad50':None,
					'ssi_polar_rad50':None,
					'crt_den_rad66':None,
					'crt_a_rad66':None,
					'mean_cort_thk_rad66':None,
					'peri_c_rad66':None,
					'endo_c_rad66':None,
					'ssi_polar_rad66':None,
					'tot_den_tib4':None,
					'tot_a_tib4':None,
					'trab_a_tib4':None,
					'crtsub_den_tib4':None,
					'crtsub_a_tib4':None,
					'trab_den_tib4':None,
					'crt_den_tib38':None,
					'crt_a_tib38':None,
					'mean_cort_thk_c_tib38':None,
					'peri_c_tib38':None,
					'endo_tib38':None,
					'ssi_polar_tib38':None,
					'crt_den_tib66':None,
					'crt_a_tib66':None,
					'cort_thk_c_tib66':None,
					'peri_c_tib66':None,
					'endo_c_tib66':None,
					'rp_cm_w_tib66':None,
					'form_19_pqct_results_revised_complete':None}
				else:
					print("already exists - no new entry")
				if roi_type=="TIB38":
					#FOR TIB38 AND TIB66: RP_CM_W
					pqct_visit[visit_id].update({'ssi_polar_tib38':rp_cm_w})
				elif roi_type=="TIB66":
					#FOR TIB38 AND TIB66: RP_CM_W
					pqct_visit[visit_id].update({'rp_cm_w_tib66':rp_cm_w})


if options.dlpbbdllc != None:
	with open(options.dlpbbdllc, "r") as f:
		BDLLC_lines = [x for x in f.readlines()]
		for BDLLC_line1 in BDLLC_lines:
			if "ROINAME" in BDLLC_line1:
				DATE=BDLLC_line1.split(",").index("DATE")
				ROI_TYPE=BDLLC_line1.split(",").index("ROINAME")
				PATNO=BDLLC_line1.split(",").index("PATNO")
				ENDO_AREA=BDLLC_line1.split(",").index("Endo_Area")
				ENDO_DEN=BDLLC_line1.split(",").index("Endo_Den")

			elif "ROINAME" not in BDLLC_line1:
				date=BDLLC_line1.split(",")[DATE]
				roi_type=BDLLC_line1.split(",")[ROI_TYPE]
				patno=BDLLC_line1.split(",")[PATNO]
				endo_area=BDLLC_line1.split(",")[ENDO_AREA]
				endo_den=BDLLC_line1.split(",")[ENDO_DEN]
				
				visit_id=str(patno+','+date)

				if name in name_to_studyid:
					study_id=name_to_studyid[name][0]
				else:
					study_id=None

				if visit_id not in pqct_visit:
					pqct_visit[visit_id]={'name':None,
					'date':date,
					'study_id':study_id,
					'patno':patno,
					'endo_area_tib38':None,
					'endo_den_tib38':None,
					'endo_area_tib66':None,
					'endo_den_tib66':None,
					'tot_a_rad4':None,
					'tot_den_rad4':None,
					'trab_a_rad4':None,
					'crtsub_den_rad4':None,
					'crtsub_a_rad4':None,
					'trab_den_rad4':None,
					'crt_den_rad50':None,
					'crt_a_rad50':None,
					'mean_cort_thk_c_rad50':None,
					'peri_c_rad50':None,
					'endo_c_rad50':None,
					'ssi_polar_rad50':None,
					'crt_den_rad66':None,
					'crt_a_rad66':None,
					'mean_cort_thk_rad66':None,
					'peri_c_rad66':None,
					'endo_c_rad66':None,
					'ssi_polar_rad66':None,
					'tot_den_tib4':None,
					'tot_a_tib4':None,
					'trab_a_tib4':None,
					'crtsub_den_tib4':None,
					'crtsub_a_tib4':None,
					'trab_den_tib4':None,
					'crt_den_tib38':None,
					'crt_a_tib38':None,
					'mean_cort_thk_c_tib38':None,
					'peri_c_tib38':None,
					'endo_tib38':None,
					'ssi_polar_tib38':None,
					'crt_den_tib66':None,
					'crt_a_tib66':None,
					'cort_thk_c_tib66':None,
					'peri_c_tib66':None,
					'endo_c_tib66':None,
					'rp_cm_w_tib66':None,
					'form_19_pqct_results_revised_complete':None}
				else:
					print("already exists - no new entry")
				# print(pqct_visit[visit_id]['name'])	

				print(endo_area,endo_den)	

				if roi_type=="TIB38" and endo_area!="":
					#FOR TIB38 AND TIB66: ENDO_AREA, ENDO_DENSITY
					pqct_visit[visit_id].update({'endo_area_tib38':endo_area,'endo_den_tib38':endo_den})
				elif roi_type=="TIB66" and endo_area!="":
					#FOR RAD50 AND RAD66: RP_CM_W
					pqct_visit[visit_id].update({'endo_area_tib66':endo_area,'endo_den_tib66':endo_den})


##Create output file 
outfile=open(options.outfilename, "w")
outfile.write("study_id,name,patno,date_pqct,tot_a_rad4,tot_den_rad4,trab_a_rad4,crtsub_den_rad4,crtsub_a_rad4,trab_den_rad4,crt_den_rad50,crt_a_rad50,mean_cort_thk_c_rad50,peri_c_rad50,endo_c_rad50,ssi_polar_rad50,crt_den_rad66,crt_a_rad66,mean_cort_thk_rad66,peri_c_rad66,endo_c_rad66,ssi_polar_rad66,tot_den_tib4,tot_a_tib4,trab_a_tib4,crtsub_den_tib4,crtsub_a_tib4,trab_den_tib4,crt_den_tib38,crt_a_tib38,mean_cort_thk_c_tib38,peri_c_tib38,endo_tib38,ssi_polar_tib38,crt_den_tib66,crt_a_tib66,cort_thk_c_tib66,peri_c_tib66,endo_c_tib66,rp_cm_w_tib66,endo_area,endo_density,endo_area66,endo_density66\n")

for visit in pqct_visit:
	for entry in pqct_visit[visit]:
		if pqct_visit[visit][entry] == None:
			print("updating entry because it was none")
			pqct_visit[visit][entry]=""
	outfile.write(str(pqct_visit[visit]['study_id'])+","+str(pqct_visit[visit]['name'])+","+str(pqct_visit[visit]['patno'])+","+str(pqct_visit[visit]['date'])+","+str(pqct_visit[visit]['tot_a_rad4'])+","+str(pqct_visit[visit]['tot_den_rad4'])+","+str(pqct_visit[visit]['trab_a_rad4'])+","+str(pqct_visit[visit]['crtsub_den_rad4'])+","+str(pqct_visit[visit]['crtsub_a_rad4'])+","+str(pqct_visit[visit]['trab_den_rad4'])+","+str(pqct_visit[visit]['crt_den_rad50'])+","+str(pqct_visit[visit]['crt_a_rad50'])+","+str(pqct_visit[visit]['mean_cort_thk_c_rad50'])+","+str(pqct_visit[visit]['peri_c_rad50'])+","+str(pqct_visit[visit]['endo_c_rad50'])+","+str(pqct_visit[visit]['ssi_polar_rad50'])+","+str(pqct_visit[visit]['crt_den_rad66'])+","+str(pqct_visit[visit]['crt_a_rad66'])+","+str(pqct_visit[visit]['mean_cort_thk_rad66'])+","+str(pqct_visit[visit]['peri_c_rad66'])+","+str(pqct_visit[visit]['endo_c_rad66'])+","+str(pqct_visit[visit]['ssi_polar_rad66'])+","+str(pqct_visit[visit]['tot_den_tib4'])+","+str(pqct_visit[visit]['tot_a_tib4'])+","+str(pqct_visit[visit]['trab_a_tib4'])+","+str(pqct_visit[visit]['crtsub_den_tib4'])+","+str(pqct_visit[visit]['crtsub_a_tib4'])+","+str(pqct_visit[visit]['trab_den_tib4'])+","+str(pqct_visit[visit]['crt_den_tib38'])+","+str(pqct_visit[visit]['crt_a_tib38'])+","+str(pqct_visit[visit]['mean_cort_thk_c_tib38'])+","+str(pqct_visit[visit]['peri_c_tib38'])+","+str(pqct_visit[visit]['endo_tib38'])+","+str(pqct_visit[visit]['ssi_polar_tib38'])+","+str(pqct_visit[visit]['crt_den_tib66'])+","+str(pqct_visit[visit]['crt_a_tib66'])+","+str(pqct_visit[visit]['cort_thk_c_tib66'])+","+str(pqct_visit[visit]['peri_c_tib66'])+","+str(pqct_visit[visit]['endo_c_tib66'])+","+str(pqct_visit[visit]['rp_cm_w_tib66'])+","+str(pqct_visit[visit]['endo_area_tib38'])+","+str(pqct_visit[visit]['endo_den_tib38'])+","+str(pqct_visit[visit]['endo_area_tib66'])+","+str(pqct_visit[visit]['endo_den_tib66'])+'\n')
outfile.close()