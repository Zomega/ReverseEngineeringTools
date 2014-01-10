# Class to serve as a stand in for the DistanceMetric class in cases where it is more effient simply to calculate relative distances.
# This class has the same interface as DistanceMetric.
class NaiveDistanceMetric:
	def __init__( self, metric ):
		self.metric = metric
	# Returns the distance from x1 to x2
	def distance( x1, x2 ):
		return self.metric( x1, x2 )
	# Returns True iff d( x1, x2 ) < C
	def distance_le( x1, x2, C ):
		return self.distance( x1, x2 ) <= C
	# Returns True iff sum( d( x_i x_j ) ) < C
	def sum_distance_le( pairs, C ):
		s = 0
		for x1, x2 in pairs:
			s += self.distance( x1, x2 )
		return s <= C

class CachedDistanceMetric:
	def __init__( self, metric ):
		self.metric = metric
		self.cache = {}
		self.cache_le = {}
	def __force_calculation__( self, x1, x2 ):
		print "Distance Calculation"
		d = self.metric( x1, x2 )
		self.cache[ x1, x2 ] = d
		return d
	# Returns the distance from x1 to x2
	def distance( self, x1, x2 ):
		if ( x1, x2 ) in self.cache:
			return self.cache[ x1, x2 ]
		if ( x2, x1 ) in self.cache:
			return self.cache[ x2, x1 ]
		return self.__force_calculation__( x1, x2 )
	# Returns True iff d( x1, x2 ) < C
	def distance_le( x1, x2, C ):
		return self.distance( x1, x2 ) <= C
	# Returns True iff sum( d( x_i x_j ) ) < C
	def sum_distance_le( pairs, C ):
		s = 0
		for x1, x2 in pairs:
			s += self.distance( x1, x2 )
		return s <= C

# Tool to try and cache / amortise distance calculation times where
# calculating distances is *very* expensive.
#
# In order to use more complex methods effectivly, a UC-Search must
# be cheaper than simply calculating the distance.
#
# First, all distances are cached in object dictionaries (ensure
# robust hashing on the objects of interest). Secondly, tools are
# provided to allow for checking of statements such as
#
#			d( x1, x2 ) <= C
#
# without explicit calculations of d( x1, x2 ) in some cases. This
# is achived by use of the triangle inequality. For instance, if we
# wish to check if d( x1, x2 ) <= d( x1, x3 ), we may be able to
# simply calculate d( x1, x3 ) alone.
class DistanceMetric:
	def __init__( self, metric ):
		self.metric = metric
		self.cache = {}
	def __force_calculation__( self, x1, x2 ):
		print "Distance Calculation"
		d = self.metric( x1, x2 )
		self.cache[ x1, x2 ] = d
		return d
	# This function may return none if the underlying
	# graph is not connected.
	def __le_estimate__( x1, x2 ):
		return self.__force_calculation__( x1, x2 )
	def distance( self, x1, x2 ):
		if ( x1, x2 ) in self.cache:
			return self.cache[ x1, x2 ]
		if ( x2, x1 ) in self.cache:
			return self.cache[ x2, x1 ]
		return self.__force_calculation__( x1, x2 )

if __name__ == '__main__':
	import math
	euc_metric = lambda x1, x2: math.sqrt( ( x1[0] - x2[0] ) ** 2 + ( x1[1] - x2[1] ) ** 2 )
	a = (0,1)
	b = (1,0)
	c = (1,1)
	d = DistanceMetric( euc_metric )
	print d.distance( a, b )
	print d.distance( a, b )
