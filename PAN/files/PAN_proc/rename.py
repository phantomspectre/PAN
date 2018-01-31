import xlrd
import sys
from collections import Counter
import re
from datetime import datetime
import os


in_file = sys.argv[1]
out_folder = sys.argv[2]

def return_token_value(str,number):
 vec=str.split(',')
 if str.count('/')>1:
  vec=str.split('/')
 output= vec[number]
 return output.upper()


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
imo=int(worksheet.cell(14,5).value)
time_of_report_1=worksheet.cell(4,5).value
time_of_report=extract_time(time_of_report_1)
tor=time_of_report.strftime('%d%m%Y%H%M-')
cmd = "mv \"%s\" %s/%s%d.xlsx"%(in_file,out_folder,tor,imo)
#print cmd
os.system(cmd)











