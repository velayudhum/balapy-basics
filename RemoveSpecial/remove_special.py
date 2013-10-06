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
print caps_sentence

print "\n\n"

caps_sentence = ''
for word in clear_sentence.split():
	caps_sentence+=word.capitalize()+' '
print caps_sentence

	
