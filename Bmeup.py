inString = raw_input("Enter text. ")
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'
for vowel in vowels:
	inString = inString.replace(" " + vowel, " B" + vowel )

for consonant in consonants:
	inString = inString.replace(" " + consonant, " B")

bList = list(inString)

if bList[0] in vowels:
	bList[0] = "B" + bList[0]
elif bList[0] in consonants:
	bList[0] = "B"

outString = "".join(bList)

print "You mean,",outString,"?"
