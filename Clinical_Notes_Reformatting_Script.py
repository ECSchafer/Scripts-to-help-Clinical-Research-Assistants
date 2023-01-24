import os
import sys
import optparse
import operator

parser = optparse.OptionParser()
parser.add_option("-i", "--infile", action="store",dest="infilename")
parser.add_option("-o","--outfile", action="store",dest="outfilename", default="notes.txt")
options, args = parser.parse_args()
#EMPI|EPIC_PMRN|MRN_Type|MRN|LMRNote_Date|Record_Id|Status|Author|COD|Institution|Author_MRN|Subject|Comments >>>
Notes=[]
outfile=open(options.outfilename,'w')
outfile.write("MRN`EMPI`EPIC_PMRN`MRN_Type`Report_Number`Report_Date_Time`Report_Description`Report_Status`Report_Type`NOTE\n")
with open(options.infilename, "r") as f:
	current_note_list=[]
	for note_line in f:
		if note_line[0][0]=="E":
			MRN=note_line.split("|").index("MRN")
			EMPI=note_line.split("|").index("EMPI")
			EPIC_PMRN=note_line.split("|").index("EPIC_PMRN")
			MRN_TYPE=note_line.split("|").index("MRN_Type")
			REPORT_NUMBER=note_line.split("|").index("Report_Number")
			REPORT_DATE_TIME=note_line.split("|").index("Report_Date_Time")
			REPORT_DESCRIPTION=note_line.split("|").index("Report_Description")
			REPORT_STATUS=note_line.split("|").index("Report_Status")
			REPORT_TYPE=note_line.split("|").index("Report_Type")
			break


	for note_line1 in f:
		if note_line1[0][0]!="E":
			note_line=note_line1.rstrip()
			if note_line!="[report_end]":
				# print(note_line)
				current_note_list.append(note_line)
				# print(current_note_list)
			else:
				# print(current_note_list)
				current_note=None
				for line in current_note_list:
					if line!='' and current_note is None:
						current_note=str(line)
					elif line!='':
						current_note=str(current_note+'   '+str(line))
				# print(current_note)
				Notes.append(current_note)
				# print(Notes)
				current_note=None
				current_note_list=[]
				# print("Endofreport")

	for note in Notes:
		Note_split=note.split('   ')
		header=Note_split[0]
		print(header)
		mrn=header.split("|")[MRN]
		empi=header.split("|")[EMPI]
		epic_pmrn=header.split("|")[EPIC_PMRN]
		mrn_type=header.split("|")[MRN_TYPE]
		report_number=header.split("|")[REPORT_NUMBER]
		report_date_time=header.split("|")[REPORT_DATE_TIME]
		report_description=header.split("|")[REPORT_DESCRIPTION]
		report_status=header.split("|")[REPORT_STATUS]
		report_type=header.split("|")[REPORT_TYPE]
		print(mrn)
		with open(options.outfilename, 'a') as outfile:
				outfile.write(str(mrn)+'`'+str(empi)+'`'+str(epic_pmrn)+'`'+str(mrn_type)+'`'+str(report_number)+'`'+str(report_date_time)+'`'+str(report_description)+'`'+str(report_status)+'`'+str(report_type)+'`'+str(note)+'\n')
			