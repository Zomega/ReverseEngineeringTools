from ngrams import *

def megadump_parser( f ):
	for line in f:
		for chunk in line.split():
			yield chunk

def fifty_shades_of_grey( n ):
	assert n >= 1	# Make sure n is tightly bound.
	assert n <= 50
	s = str( hex( 4095 * n / 50 ) )[2:]
	while len( s ) < 3:
		s = '0' + s
	return '#' + s

import pydot
		
names = [ '1388714212', '1388717228', '1388725781', '1388732850', '1388735678', '1388807221', '1389315179']

vtot = {}

for name in names:
	print "Running for megadump", name
	f = open('../../.galileo/53A0ED39B4DB/dump-'+name+'.txt', 'rb')
	
	v = ngrams_vector( list( megadump_parser( f ) ), 2 )
	vtot = vector_add( v, vtot )

	graph = pydot.Dot(graph_type='digraph')

	for a,b in v:
		if a == "00" or b == "00":
			continue
		if v[a,b] > 2:
			e = pydot.Edge( a, b, label=str( v[a,b] ) )
			graph.add_edge( e )

	# ok, we are set, let's save our graph into a file
	graph.write_png('2gram-vis-'+name+'.png')

print "Running for all."

graph = pydot.Dot(graph_type='digraph')

for a,b in vtot:
	if a == "00" or b == "00":
		continue
	if vtot[a,b] > 6:
		e = pydot.Edge( a, b, label=str( vtot[a,b] ) )
		graph.add_edge( e )

# ok, we are set, let's save our graph into a file
graph.write_png('2gram-vis-all.png')


