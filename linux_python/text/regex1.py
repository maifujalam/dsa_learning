import re
s="this is a string with {{words}} embedded in\
   {{curly brackets}} to show an {{example}} of {{regular expressions}}"
pattern="{{.*?}}"
for i in re.findall(pattern, s):
    print(i)
