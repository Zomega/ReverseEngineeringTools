from vector import *

# Take a sequence and break it into it's constituent n-grams.
def ngrams( data, n ):
	g = []
	for datum in data:
		g.append( datum )
		if len( g ) < n:
			continue
		yield tuple(g)
		g.pop(0)

# Aliases for n-grams. Strictly for typing convenience.
bigrams = lambda data: ngrams( data, 2 )
trigrams = lambda data: ngrams( data, 3 )

# Encodes the data into a vector (dictionary) that has length = len( singletons ) ** n
def ngrams_vector( data, n ):
	v = {}
	for ngram in ngrams( data, n ):
		if ngram not in v:
			v[ ngram ] = 0
		v[ ngram ] += 1
	return v

# TODO: Make work with a generator like this.
def charsplit( string ):
	return ( char for char in string )

def wordsplit( string ):
	return string.split()

if __name__ == '__main__' :

	sample1 = 'Languages have capitalisation rules to determine whether upper case or lower case letters are to be used in a given context. In English, capital letters are used as the first letter of a sentence, a proper noun, or a proper adjective, and for initials or abbreviations in American English; British English only capitalises the first letter of an abbreviation. The first-person pronoun "I" and the interjection "O" are also capitalised. Lower case letters are normally used for all other purposes. There are however situations where further capitalisation may be used to give added emphasis, for example in headings and titles or to pick out certain words (often using small capitals). There are also a few pairs of words of different meanings whose only difference is capitalisation of the first letter. Other languages vary in their use of capitals. For example, in German the first letter of all nouns is capitalised, while in Romance languages the names of days of the week, months of the year, and adjectives of nationality, religion and so on generally begin with a lower case letter.'

	sample2 = 'Capitalisation is the writing of a word with its first letter in uppercase and the remaining letters in lowercase. Capitalization rules vary by language (e.g. capitalisation in English) and are often quite complex, but in most modern languages that have capitalisation, the first letter of every sentence is capitalised, as are all proper nouns. Some languages, such as German, capitalise the first letter of all nouns; this was previously common in English as well. (See the article on capitalisation for a detailed list of norms.)'

	sample3 = 'Die land is geografies, in oppervlakte en inwonertal die middelste van die Baltiese lande, en verenig elemente van beide buurlande: dit deel sy Baltiese taal, Lets, met Litaue, waar die verwante Litaus gepraat word, en dit deel sy oorwegend Lutherse geloof met Estland. Die geskiedenis van Letland vertoon groot ooreenkomste met die van Estland, en veel minder met die van Litaue. Letland het na n langdurige Sowjet-besetting in 1991 sy onafhanklikheid herwin nadat dit reeds tussen 1918 en 1940 as onafhanklike republiek bestaan het. n Erfenis van die Sowjet-tydperk is die groot aantal Russiessprekende inwoners.'

	print "First trigrams of Sample 1:"
	for x in list( trigrams( sample1 ) )[ :20 ]:
		print "'" + str( x[0] + x[1] + x[2] ) + "',",
	print "...\n"

	v1 = ngrams_vector( charsplit(sample1), 3 )
	v2 = ngrams_vector( charsplit(sample2), 3 )
	v3 = ngrams_vector( charsplit(sample3), 3 )

	print "Trigram analysis of samples to demonstrate language clusters..."
	print "( English <-> English ):",angular_distance( v1, v2 )
	print "( English <-> Other ):  ",angular_distance( v1, v3 )
	print "( English <-> Other ):  ",angular_distance( v2, v3 )
