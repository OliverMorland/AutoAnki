import pyperclip
import re

#Get vocab string from clip board
vocabString = pyperclip.paste()

#Create regex pattern
pattern = r'\b([가-힣]+)\b\s*:\s*(\w+)\b'

#Find all in vocab string
vocabPairs = re.findall(pattern, vocabString)
print(vocabPairs)
