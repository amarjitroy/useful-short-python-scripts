import re, pyperclip

text = pyperclip.paste()
#Extracting Register Numbers
extractedCSEReg= re.compile(r'36\d\d\d\d\d\d') #36110009 for first year CSE
extractedITReg= re.compile(r'36\d\d\d\d\d') #3610001 for others

#Saving the extracted register numbers in variables
CSEreg= extractedCSEReg.findall(text)
ITreg= extractedITReg.findall(text)

#Storing the register numbers on the clipboard
result= '\n'.join(CSEreg)+ '\n'+ '\n'.join(ITreg)
pyperclip.copy(result)


