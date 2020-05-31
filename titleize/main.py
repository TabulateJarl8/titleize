import nltk
import re

def reconstruct_sentance(startsentance, sentancelist):
	spaces = [(m.start(0), m.end(0)) for m in re.finditer(" ", startsentance)]
	newsentance = "".join(sentancelist)
	for i in range(len(spaces)):
		newsentance = newsentance[:spaces[i][0]] + " " + newsentance[spaces[i][0]:]
	return newsentance

def titleize(str):	
	words = nltk.pos_tag(nltk.word_tokenize(str))
	newwords = []
	for i in range(len(words)):
		if i == 0:
			newwords.append(words[i][0].capitalize())
		elif i >= len(words) - 1:
			newwords.append(words[i][0].capitalize())
		elif re.search("\.|\?|\!", words[i+1][0]) != None:
			newwords.append(words[i][0].capitalize())
		elif re.search("\.|\?|\!", words[i-1][0]) != None:
			newwords.append(words[i][0].capitalize())
		elif re.search(".*(NN|PRP|VB|RB|JJ|IN|WDT|WP|WRB).*", words[i][1]) != None:
			newwords.append(words[i][0].capitalize())
		else:
			newwords.append(words[i][0])
	return reconstruct_sentance(str, newwords)