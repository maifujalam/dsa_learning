import re


FILE="text.txt"
REGEX=re.compile(r"https?://[\w\.,]+")   # https:\\.www.[fdd].com

def read_file(filename):
    file_object=open(filename,"r")
    data=file_object.read()
    file_object.close()
    return data

def fine_regex(data,pattern):
    result=re.findall(pattern,data)
    return result

if __name__ == '__main__':
   # print(read_file(FILE))
    print(fine_regex(read_file(FILE),REGEX))