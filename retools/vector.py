###### BEGIN VECTOR PRIMITIVES ######
# Any higher level function should try to rely on these functions to provide
# support for new representations of vectors for compatibility reasons. Do not
# internally manipulate the representations in higher level functions. Remain
# representation agnostic, etc., etc.

# Returns the Euclidean Length of A, the square root of the sum of the squares
# of it's ( presumed orthonormal ) components.
def euclidian_length( A ):
	from math import sqrt
	if isinstance(A, list):
		return sqrt( sum( a**2 for a in A ) )
	if isinstance(A, dict):
		return sqrt( sum( A[key] ** 2 for key in A ) )
	raise ValueError( "euclidian_length( A ) supports only lists and dictionaries." )

# Returns kA, a component-wise scaling of A.
def scale( A, k ):
	if isinstance(A, list):
		return [ k * a for a in A ]
	if isinstance(A, dict):
		return { key: k * A[key] for key in A }
	raise ValueError( "scale( A, k ) supports only lists and dictionaries for A." )

# Returns the dot product of A with B, i.e. the sum of component-wise products.
# It is required that the representations of A and B are compatible.
def dot_product( A, B ):
	# If lists...
	if isinstance(A, list) and isinstance(B, list):
		if not len( A ) == len( B ):
			raise ValueError( "Cannot compute the dot product of two vectors of differing lengths." )
		return sum( A[i] * B[i] for i in range( len( A ) ) )
	if isinstance(A, dict) and isinstance(B, dict):
		s = 0
		for key in A:
			if key in B:
				s += A[key] * B[key]
		return s
	raise ValueError( "dot_product( A, B ) supports only lists and dictionaries." )

# Adds two vectors A and B component-wise. It is required that the
# representations of A and B are compatible.
def vector_add( A, B ):
	if isinstance(A, list) and isinstance(B, list):
		if not len(A) == len(B):
			raise ValueError( "Tried to add vectors of differing length." )
		return [ A[i] + B[i] for i in range( len(A) ) ]
	if isinstance(A, dict) and isinstance(B, dict):
		keyspace = set()
		keyspace = keyspace.union(A)
		keyspace = keyspace.union(B)
		# Add the values in A and B corresponding to key, but do not
		# complain if these values do not exist. Sloppy but functional.
		def safe_add( key ):
			r = 0
			if key in A:
				r += A[ key ]
			if key in B:
				r += B[ key ]
			return r
		return { key: safe_add(key) for key in keyspace }
	raise ValueError( "vector_add( A, B ) supports only lists and dictionaries." )

###### END VECTOR PRIMITIVES ######

###### BEGIN VECTOR NON-PRIMITIVES ######
# All following functions are defined in terms of the primitives and are
# representation agnostic. It is generally assumed that all arguments for
# these functions are passed in some common supported representation so that
# the primitives can act on them unless otherwise noted.

### Basics ###

# Returns the unit vector corresponding to A, i.e. the scaling of A such that
# the length is one, but the vector points in the original direction.
def unit_vector( A ):
	length_A = euclidian_length(A)
	return scale( A, 1.0 / length_A )

# Subtract B from A. Returns A - B. Note that the order of arguments is important.
def vector_subtract( A, B ):
	return vector_add( A, scale( B, -1 ) )

### Projection ###

# Returns the projection of A onto B, AKA the component of A parallel B.
def projection( A, B ):
	unit_B = unit_vector( B )
	return scale( unit_B, dot_product( A, unit_B ) )

# Returns the component of A orthogonal to B.
def residual( A, B ):
	return vector_subtract( A, projection( A, B ) )

### High Dimension Vector distance measures ###

# Cosine distance, i.e. The cosine of the angle between two vectors at the origin.
# Based off the dot product. Not a proper distance metric, but a good proxy.
def cosine_distance( A, B ):
	return dot_product( A, B ) / ( euclidian_length(A) * euclidian_length(B) )

# Angular distance, based off the cosine distance. This is a proper distance metric.
def angular_distance( A, B ):
	from math import acos
	return acos( cosine_distance( A, B ) )

###### Unit Test ######
if __name__ == '__main__':
	x,y,z,w='x','y','z','w'
	A_dict = {x:1,y:2,z:3}
	B_dict = {x:2,y:3,z:1}
	A_list = [1,2,3]
	B_list = [2,3,1]

	# Primitives tests
	print vector_subtract( A_list, B_list )
	print vector_subtract( A_dict, B_dict )
	print unit_vector( A_list )
	print unit_vector( A_dict )
	print projection( A_dict, B_dict )
	print residual( A_dict, B_dict )
	print vector_add( projection( A_dict, B_dict ), residual( A_dict, B_dict ) ), dot_product( projection( A_dict, B_dict ), residual( A_dict, B_dict ) )
