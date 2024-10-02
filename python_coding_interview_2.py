
#str1 = "AC*WV12N/ :#e123we2.45oin   (fwoi6n#a98nfwb+owi"

#output = [2.45,6,12,98,123]

#method 1
import re
def extract_num_decimal1(str1):
    pattern = r'\d+\.\d+|\d+'
    res = re.findall(pattern, str1)
    return res 

str1 = "AC*WV12N/ :#e123we2.45oin   (fwoi6n#a98nfwb+owi"
print(extract_num_decimal1(str1))



    


#method 2

def extract_num_decimal2(str1):
    res2 =[]
    temp = ""
    for ch in str1:
        if ch.isdigit() or (ch=='.' and '.' not in temp):
            temp = temp + ch  
        elif len(temp)!=0:
            res2.append(eval(temp))
            temp = ""
    return res2 

         
    return res2
str1 = "AC*WV12N/ :#e123we2.45oin   (fwoi6n#a98nfwb+owi"
print(extract_num_decimal2(str1))
