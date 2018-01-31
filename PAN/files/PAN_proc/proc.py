import xlrd
import sys
from collections import Counter
import re
from datetime import datetime




in_file = sys.argv[1]
out_file = sys.argv[2]



file_out = open(out_file,"a") 

def return_token_value(str,number):
 vec=str.split(',')
 if str.count('/')>1:
  vec=str.split('/')
 output= vec[number]
 return output.upper()

def return_token_value2(str,number):
 vec=str.split(',')
 #vec=re.split(token,str)
 output= vec[number]
 return output

def hasNumbers(inputString):
 return any(char.isdigit() for char in inputString)

def extract_time(time_string):
 now = datetime.now()
 digits = re.findall('\d+', time_string)
 mon = "xx"
 if "jan" in time_string.lower():
  mon="Jan"
 if "feb" in time_string.lower():
  mon="Feb"
 if "mar" in time_string.lower():
  mon="Mar"
 if "apr" in time_string.lower():
  mon="Apr"
 if "may" in time_string.lower():
  mon="May"
 if "jun" in time_string.lower():
  mon="Jun"
 if "jul" in time_string.lower():
  mon="Jul"
 if "aug" in time_string.lower():
  mon="Aug"
 if "sep" in time_string.lower():
  mon="Sep"
 if "oct" in time_string.lower():
  mon="Oct"
 if "nov" in time_string.lower():
  mon="Nov"
 if "dec" in time_string.lower():
  mon="Dec"
 time_str = "%s %s %s"%(digits[0],mon,now.year)
 report_date = datetime.strptime(time_str,'%d%H%M %b %Y')
 return report_date

workbook = xlrd.open_workbook(in_file)
worksheet = workbook.sheet_by_name('Col A to U, Z explanation')
vessel_name= return_token_value(worksheet.cell(2,5).value,0)
time_of_report_1=worksheet.cell(4,5).value
time_of_report=extract_time(time_of_report_1)
tor=time_of_report.strftime('%d-%m %H:%M')



#port call , ETA and followup ports
port_and_followup=worksheet.cell(20,5).value
port_call_t= return_token_value(worksheet.cell(20,5).value,0)
port_call = ''.join([i for i in port_call_t if not i.isdigit()])
ETA_t=re.search(r'\d+',port_and_followup).group()
now = datetime.now()

td = 0

if len(ETA_t) == 6:
 if int(ETA_t[0:2]) >= time_of_report.day:
  time_str = "%s %d %s"%(ETA_t,time_of_report.month,now.year)
  ETA_datetime = datetime.strptime(time_str,'%d%H%M %m %Y')
  ETA=ETA_datetime.strftime('%d-%m %H:%M')
  time_diff = ETA_datetime - time_of_report
  td = float(time_diff.total_seconds())/(60*60)

 if int(ETA_t[0:2]) < time_of_report.day:
  time_str = "%s %d %s"%(ETA_t,time_of_report.month+1,now.year)
  ETA_datetime = datetime.strptime(time_str,'%d%H%M %m %Y')
  ETA=ETA_datetime.strftime('%d-%m %H:%M')
  time_diff = ETA_datetime - time_of_report
  td = float(time_diff.total_seconds())/(60*60)
else:
 ETA = "invalid date format"

#if td < 96:
# td_flag = 1
#else:
# td_flag = 0

previous_1 = return_token_value2(worksheet.cell(22,5).value,0)
previous_2 = return_token_value2(worksheet.cell(24,5).value,0)
previous_3 = return_token_value2(worksheet.cell(26,5).value,0)
previous_4 = return_token_value2(worksheet.cell(28,5).value,0)
previous_5 = return_token_value2(worksheet.cell(30,5).value,0)
previous_6 = return_token_value2(worksheet.cell(32,5).value,0)
previous_7 = return_token_value2(worksheet.cell(34,5).value,0)
previous_8 = return_token_value2(worksheet.cell(36,5).value,0)
previous_9 =  return_token_value2(worksheet.cell(38,5).value,0)
previous_10 =  return_token_value2(worksheet.cell(40,5).value,0)

str_previous_ports = "%s-%s-%s-%s-%s-%s-%s-%s-%s-%s"%(previous_1.upper(),previous_2.upper(),previous_3.upper(),previous_4.upper(),previous_5.upper(),previous_6.upper(),previous_7.upper(),previous_8.upper(),previous_9.upper(),previous_10.upper())

worksheet2 = workbook.sheet_by_name('Col W_Crew')
list_crew = list()
i=5
while 1:
 try:
  str_temp=worksheet2.cell(i,6).value
  str_temp = str_temp.upper()
  list_crew.append(str_temp.strip(' '))    
  i=i+1
 except IndexError:
  break
counts = Counter(list_crew)
dist = counts.most_common(5)
#print dist[0][0]
str_dist = ""
for i in xrange(0,len(dist)):
 if len(dist[i][0]) > 2:
  str_dist = str_dist + dist[i][0] + " " + str(dist[i][1]) + " "  

#*******************
list_crew = list()
i=5
genderflag=0
while 1:
 try:
  str_temp=worksheet2.cell(i,4).value
  str_temp = str_temp.upper()
  #if len(str_temp.strip(' ')) > 0:
  list_crew.append(str_temp.strip(' '))    
  i=i+1
 except IndexError:
  break
counts = Counter(list_crew)
dist = counts.most_common(5)
#print dist[0][0]
str_dist2 = ""
if len(dist) > 1:
 genderflag=1
for i in xrange(0,len(dist)):
 if dist[i][0] == "M":
  str_dist2 = str_dist2 + "MALE" + " " + str(dist[i][1]) + " "  
 else:
   if dist[i][0] == "F":
    str_dist2 = str_dist2 + "FEMALE" + " " + str(dist[i][1]) + " " 
   else:
    if (len(dist[i][0]) > 0):
     str_dist2 = str_dist2 + dist[i][0] + " " + str(dist[i][1]) + " "  

#**********************


#print str_dist


worksheet3 = workbook.sheet_by_name('Col Y_Other persons')
i=8
str_others = ""
while 1:
 try:
   str_others = str_others + worksheet3.cell(i,1).value + " "
   i=i+1
 except IndexError:
  break

str_others = str_others.upper()
str_others = str_others.replace("NIL", "")
str_others = str_others.replace("NA", "")
str_others = str_others.replace("N/A", "")

worksheet4 = workbook.sheet_by_name('Col YS_Security Personnel')
i=6
str_security = ""
while 1:
 try:
   str_security = str_security + worksheet4.cell(i,1).value + " "
   i=i+1
 except IndexError:
  break
str_security = str_security.upper()
str_security = str_security.replace("NIL", "")
str_security = str_security.replace("NA", "")
str_security = str_security.replace("N/A", "")



cargo=worksheet.cell(48,5).value
cargo=cargo.upper()
weapons=worksheet.cell(51,5).value
weapons = weapons.upper()
weapons = weapons.replace("NIL", "")
weapons = weapons.replace("NA", "")
weapons = weapons.replace("N/A", "")

ship_type=worksheet.cell(8,5).value





file_out.write("<TR>")
str_out = "<TD>%s"%(ship_type)
file_out.write(str_out)
str_out = "<TD>%s"%(vessel_name)
file_out.write(str_out)

str_out = "<TD>%s"%(port_call)
file_out.write(str_out)

if td > 96:
 str_out = "<TD>%s"%(ETA)
else:
 str_out = "<TD BGCOLOR=\"#ffff00\">%s"%(ETA)
file_out.write(str_out)

#str_out = "<TD>%s"%(ETA)
#file_out.write(str_out)

str_out = "<TD>%s"%(str_previous_ports)
file_out.write(str_out)
str_out = "<TD>%s"%(str_dist)
file_out.write(str_out)

if  len(re.findall('\d+',str_dist2)) == 1:
 str_out = "<TD>%s"%(str_dist2)
else:
 str_out = "<TD BGCOLOR=\"#ffff00\">%s"%(str_dist2)
file_out.write(str_out)


if len(str_others.replace(" ", "")) < 1:
 str_out = "<TD>%s"%(str_others)
else:
 str_out = "<TD BGCOLOR=\"#ffff00\">%s"%(str_others)
file_out.write(str_out)

if len(str_security.replace(" ", "")) < 1:
 str_out = "<TD>%s"%(str_security)
else:
 str_out = "<TD BGCOLOR=\"#ffff00\">%s"%(str_security)
file_out.write(str_out)


if ("timber" in cargo.lower()) or ("waste" in cargo.lower()) :
 str_out = "<TD BGCOLOR=\"#ffff00\">%s"%(cargo)
else:
 str_out = "<TD>%s"%(cargo)
file_out.write(str_out)


if hasNumbers(weapons) :
 str_out = "<TD BGCOLOR=\"#ffff00\">%s"%(weapons)
else:
 str_out = "<TD>%s"%(weapons)
file_out.write(str_out)

file_out.write("</TR>")
file_out.close()
#print str_out
#file_out.write("<TD>")












