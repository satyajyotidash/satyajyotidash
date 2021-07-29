import re

data='''perl is simple and powerful programming langauge
Perl is interpreter based langauge
perl has huge library support
Perl is used for autmation, web development and data analysis
perl is portable
perl is Perl is PERL is PErl is perL is Perl'''


newdata=re.subn('[pP]erl',"python",data,count=0,flags=re.I)

print(data)
print("************************************")
print(newdata[0])
print("Number of substitutes :: ",newdata[1])
