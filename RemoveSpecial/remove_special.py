#!/usr/bin/python


sentence = """A pyt#hon i!s a co%nstri^cting s\nake belong@ing to the 
P*ython (genus), or, more gene[]rally, any sna+ke in the fa-mily #$%
Py/thoni%dae (cont/aining the Pyt<>?hon g"en\tus)."""

clear_sentence = ''

for letter in sentence:
	if letter.isalpha() or letter ==' ' or letter ==',' or letter =='.' or letter== ',':
		clear_sentence+=letter
print clear_sentence
