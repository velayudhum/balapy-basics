#!/usr/bin/python


sentence = """A pyt#hon i!s a co%nstri^cting s\nake belong@ing to the 
P*ython (genus), or, more gene[]rally, any sna+ke in the fa-mily #$%
Py/thoni%dae (cont/aining the Pyt<>?hon g"en\tus)."""

clear_sentence = ''

for letter in sentence:
	if letter.isalpha() or letter ==' ' or letter ==',' or letter =='.' or letter== ',':
		clear_sentence+=letter
print clear_sentence

print "\n\n"

caps_sentence = ''
word = ''
for letter in clear_sentence:
	if not letter.isspace():
		word+=letter
	else:
		word=word.capitalize()+' '
		caps_sentence+=word
		word=''
if word:
	caps_sentence+=word
#print caps_sentence

print "\n\n"

caps_sentence = ''
for word in clear_sentence.split():
	caps_sentence+=word.capitalize()+' '
print caps_sentence

print "\n\n"

caracter_counts={}
for letter in clear_sentence:
	caracter_counts[letter]=caracter_counts.setdefault(letter,0)+1
	
for letter in clear_sentence:
	if not caracter_counts.has_key(letter):
		caracter_counts[letter]=0
	caracter_counts[letter]+=1
	

for key in caracter_counts:
	print key, '-',caracter_counts[key]

	


	
