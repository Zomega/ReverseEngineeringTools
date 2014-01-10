class Path:
	def __init__( self, data ):
		self.data = data

	def min_x( self ):
		return min( p[0] for p in self.data )
	def max_x( self ):
		return max( p[0] for p in self.data )
	def min_y( self ):
		return min( p[1] for p in self.data )
	def max_y( self ):
		return max( p[1] for p in self.data )

	def width( self ):
		return 1 + self.max_x() - self.min_x()
	def height( self ):
		return 1 + self.max_y() - self.min_y()

	def __len__( self ):
		return len( self.data )

	def __getitem__( self, index ):
		return self.data[ index ]

def shift( path, x ):
	return Path( [ (p[0]+x[0], p[1]+x[1] ) for p in path.data ] )

def mirror_x( path ):
	return Path( [ ( -1 * p[0], p[1] ) for p in path.data ] )

def mirror_y( path ):
	return Path( [ ( p[0], -1 * p[1] ) for p in path.data ] )

def regularize( path ):
	return shift( path, ( -1 * path.min_x(), -1 * path.min_y() ) )

# A quick and lightweight function to convert a string of commands
# (e.g. 'FFRFLRRF') into an Path.		
def trace( path ):
	def right90( vec ):
		return ( -vec[1], vec[0] )

	# Rotate the vector left 90 degrees
	# Uses right90 for refactor purposes.
	def left90( vec ):
		return right90( right90( right90( vec ) ) )

	def add( vec1, vec2 ):
		return ( vec1[0] + vec2[0], vec1[1] + vec2[1] )

	point_path = [ (0,0) ] # Start at (0,0)
	heading = (1,0) # Facing towards (1,0)
	
	for char in path:
		if char == 'F':
			point_path.append( add( point_path[-1], heading ) )
		if char == 'R':
			heading = right90( heading )
		if char == 'L':
			heading = left90( heading )
	return Path( point_path )

# Test our an SVGFig replacement.
import svgfig
def render( p ):
	return svgfig.Fig(svgfig.Poly(p.data) ).SVG(svgfig.window(p.min_x()-1,p.max_x()+1,p.min_y()-1,p.max_y()+1)).inkview()

if __name__ == '__main__':
	# Just test some stuff out...
	p = Path( [(0,0),(1,1),(1,-1),(-1,-1),(-20, 0)] )
	print p.data
	print regularize( p ).data
	render( p )
