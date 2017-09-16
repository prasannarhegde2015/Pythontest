import re
file = open("e:\getOTP.txt", "r") 
alltxt = file.read()
print (alltxt)
line0 = alltxt
print(line0)
line00 = line0.replace('\n',"")
print (line00)
#line = "The One Time Password for your servicing request is 213411. The code is valid for 15 minutes only and is usable only once";
line = line00
searchObj = re.search( r' request is (.*)The code is valid', line, re.M|re.I)
abc=""
print (abc)
for  mt in searchObj.group():
	abc=abc + mt
print (abc)
line2 = abc
searchObj = re.search( r'\d+', line2, re.M|re.I)
abc=""
for  mt in searchObj.group():
	abc=abc + mt
print (abc)
