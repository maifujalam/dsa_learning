import re
import math

FILE_NAME = "text.txt"
PATTERN=re.compile(r'[\w\.-]+@[\w\.-]+')

def get_data(file):
    file_object=open(file,"r")
    data=file_object.read()
    file_object.close()
    return data

def get_regex(data,pattern):
    emails=re.findall(pattern,data)
    return emails

if __name__ == '__main__':
    data=get_data(FILE_NAME)
    print(get_regex(data,PATTERN))
