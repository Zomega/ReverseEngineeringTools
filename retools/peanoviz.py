import spacefillingcurve

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'

def colored( string, color ):
	return color + string + WHITE

def render( image, max_val = 2**8 ):
	def convert( byte ):
		number = int( ( 5 * byte ) / max_val )
		if number == 0:
			return PURPLE
		if number == 1:
			return BLUE
		if number == 2:
			return GREEN
		if number == 3:
			return YELLOW
		if number == 4:
			return RED
		return WHITE
	for row in image:
		data = ''
		for entry in row:
			data = data + colored( u"\u2588", convert( entry ) )
		print data

def file_to_bytes( f ):
	bytes = []
	while True:
		byte_s = f.read(1)
		if not byte_s:
			break
		bytes.append( ord( byte_s ) )
	return bytes

#TODO: Not really sure this is needed... RM?
from path import mirror_y
def peano_array( order ):
	p = mirror_y( spacefillingcurve.peano_curve( order ) )
	#Initialize a array to hold the data...
	arr = [[0 for i in range(p.width())] for j in range(p.height())]
	min_x = p.min_x()
	min_y = p.min_y()
	for i in range( len( p ) ):
		arr[p[i][0] - min_x][p[i][1] - min_y] = i
	return arr

def peanoify( data, order ):
	curve = peano_array( order )
	chunksize = len( curve ) * len( curve[0] )
	data = data + [0]*(chunksize - ( len(data) % chunksize ))
	offset = 0
	result = []
	print ( len(data) / chunksize )
	while offset < ( len(data) / chunksize ):
		result.extend( [[ data[ curve[i][j] + offset * chunksize ] for j in range( len( curve[0] ) ) ] for i in range( len(curve) ) ] )
		offset += 1
	return result
	
render( peanoify( file_to_bytes( open('path.pyc', 'rb') ), 4 ), 2**8 )
