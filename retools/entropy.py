# Optimized Shannon Entropy calculation over collection X.
from math import log
def entropy( X ):
	count = {}
	total = 0
	for x in X:
		if x not in count:
			count[x] = 0
		count[x] += 1
		total += 1
	print count, total

	# At this point, we could compute the frequencies, but some quick algebra
	# reveals that we can do a lot better just by rearranging when dealing with
	# finite samples.
	return log( total, 2 ) - sum( count[x] * log( count[x], 2 ) for x in count ) / total

# Routine optimized for computing the entropy of multiple sequential and overlapping blocks of data formatted as a generator to allow continous data flow.
def window_entropy( X, window_size, jump_size = 1):
	
	# Any time we return a value, we'll have sum( count[x] for x in count ) = window_size
	# by structural induction.

	def current_entropy():
		return log( window_size, 2 ) - sum( count[x] * log( count[x], 2 ) for x in count ) / window_size
	
	# Initialize data structures...
	count = {}

	elems = []
	k = 1
	while True:
		try:
			elem = next( X )
		except StopIteration:
			break
		elems.append( elem )
		if elem not in count:
			count[ elem ] = 0
		count[ elem ] += 1
		if len( elems ) < window_size:
			continue
		if len( elems ) == window_size:
			yield current_entropy()
			continue
		# At this point, we need to remove an element.
		rm_elem = elems.pop(0)
		k += 1
		count[ rm_elem ] -= 1
		if count[ rm_elem ] == 0:
			del count[ rm_elem ]
		if k == jump_size:
			k = 0
			yield current_entropy()


print entropy( [ 1, 2, 1, 2, 1, 3, 3, 1, 1, 1 ] )
print entropy( [1,0,1,0,1,0] )
print entropy( [1,1,1,1,1,1] )
print entropy( ['A','B','C','D','E','F'] )

l = [ x for x in window_entropy( (c for c in 'Language is the human capacity for acquiring and using complex systems of communication, and a language is any specific example of such a system. The scientific study of language is called linguistics. Estimates of the number of languages in the world vary between 6,000 and 7,000. However, any precise estimate depends on a partly arbitrary distinction between languages and dialects. Natural languages are spoken or signed, but any language can be encoded into secondary media using auditory, visual, or tactile stimuli, for example, in graphic writing, braille, or whistling. This is because human language is modality-independent. When used as a general concept, "language" may refer to the cognitive ability to learn and use systems of complex communication, or to describe the set of rules that makes up these systems, or the set of utterances that can be produced from those rules. All languages rely on the process of semiosis to relate signs with particular meanings. Oral and sign languages contain a phonological system that governs how symbols are used to form sequences known as words or morphemes, and a syntactic system that governs how words and morphemes are combined to form phrases and utterances. Human language is unique because it has the properties of productivity, recursivity, and displacement, and because it relies entirely on social convention and learning. Its complex structure therefore affords a much wider range of possible expressions and uses than any known system of animal communication. Language is thought to have originated when early hominins started gradually changing their primate communication systems, acquiring the ability to form a theory of other minds and a shared intentionality. This development is sometimes thought to have coincided with an increase in brain volume, and many linguists see the structures of language as having evolved to serve specific communicative and social functions. Language is processed in many different locations in the human brain, but especially in Broca\'s and Wernicke\'s areas. Humans acquire language through social interaction in early childhood, and children generally speak fluently when they are approximately three years old. The use of language is deeply entrenched in human culture. Therefore, in addition to its strictly communicative uses, language also has many social and cultural uses, such as signifying group identity, social stratification, as well as for social grooming and entertainment. Languages evolve and diversify over time, and the history of their evolution can be reconstructed by comparing modern languages to determine which traits their ancestral languages must have had in order for the later stages to have occurred. A group of languages that descend from a common ancestor is known as a language family. The languages that are most spoken in the world today belong to the Indo-European family, which includes languages such as English, Spanish, Portuguese, Russian, and Hindi; the Sino-Tibetan languages, which include Mandarin Chinese, Cantonese, and many others; the Afro-Asiatic family, which include Arabic, Amharic, Somali, and Hebrew; and the Bantu languages, which include Swahili, Zulu, Shona, and hundreds of other languages spoken throughout Africa. The consensus is that between 50 and 90% of languages spoken at the beginning of the twenty-first century will probably have become extinct by the year 2100.'), 350 ) ]

def file_to_bytes( f ):
	while True:
		byte_s = f.read(1)
		if not byte_s:
			break
		yield hex(ord( byte_s ))
l = []
k=0
for x in window_entropy( file_to_bytes( open('0001.dmp', 'rb') ), 5000, 500 ):
	k += 1
	if k % 10**2 == 0:
		print x
	l.append( ( k, x ) )

from path import *
render( Path( l ) )

