import docx2txt
import re
my_text = docx2txt.process("/Users/suprajaraman/Desktop/sampleresume.docx")
pattern=re.compile(r'[a-zA-Z0-9_\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
matches=pattern.finditer(my_text)
for x in matches:
    print(x.group(0))

