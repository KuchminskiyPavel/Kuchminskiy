import re
# =====1=====
# def find_cat(string):
#     substrings = re.findall(r'(?=(cat))', string)
#     return substrings
#
# input_string = "jdgdh catdjhg fsfsfcatffff dcat"
# substrings = find_cat(input_string)
# for substring in substrings:
#     print(substring)
# =====2=====
# pattern = r'(z.{3}z)'
# text = "dgdgdfgzdfgzereezzzewefdfz"
# print(re.findall(pattern, text))
# =====3=====
# patern = r'[8-9]{1}[0-9]{9}\s'
# numbers = "8527548237 7546596025 9236749204235 "
# print(re.findall(patern,numbers))
# ====4=====
# text = "впвава авукг Оаукамв"
# print(re.findall(r'\b[аеёиоуыэюяАЕЁИОУЫЭЮЯ]\w+\b',text, re.UNICODE))
# ====5=====
# numbers = "43fsddf35dsfs-33-24234"
# print(re.findall(r'-?\d',numbers))
#=====6=====
# text = "human humanitary humani ty ex-human"
# print(re.sub(r'(human)','computer',text))
#=====7=====
# numbers = "23-11-2035 12.02.2123 34-345-2394"
# print(re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}',numbers))
#====8====
# text = ("dhhjyrt bdsfsg gjfbsfisf geufsub")
# print(re.findall(r'\b\w*b\w*\b',text))
