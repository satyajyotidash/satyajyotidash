import re

data="asada432sdfsdf3223sdfsdf213324sdfsdfs23234sfsdfsdf23234wefwefw3124234324sgwgwgwrg"

res=re.split("\d+",data,maxsplit=3)

print(res)

