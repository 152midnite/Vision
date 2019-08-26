import re

reg = '(.*(?=\\dcar))(\\d(?=car)).*([str]?)'
reg = r'(.*?)(\d)car(?:.*(str))?'
string = 'wts-lg-000191_0car_lp_str'
string2 = 'wts-lg-000191_0car_lp'

print(re.findall(reg,string))
print(re.findall(reg,string2))
