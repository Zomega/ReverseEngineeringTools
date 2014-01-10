# Represents a familiy of strings that are constructed by repeatedly applying
# simple replacement rules. This sort of thing is especially useful when working
# with space-filling curves and other iterative fractals, as these fractals usually
# have corresponding Lindenmayer Representations.
#
# Alphabet - Set of characters that are used internally. Pass in as a string, one to a character. There should be one rule per member of the Alphabet.
# Constants - External members.
# Axiom - The starting string ( i.e. order 0 member representation ).
# Rules - Replacement rules.
#
# Example: Hilbert curve turtle path generator.

class LindenmayerSystem:
	def __init__( self, alphabet, constants, axiom, rules ):
		# TODO: Abstract to string to list fxn.
		# TODO: Evaluate actual use cases here.
		# Many should be sets. Alphabet may be totally redundant with rules, or should at least be verified against it.
		self.alphabet = [ char for char in alphabet ]
		self.constants = [ char for char in constants ]
		self.axiom = [ char for char in axiom ]
		self.rules = { seed:[ char for char in rules[seed] ] for seed in rules }
		self.representation_cache = { 0: axiom } # Would a list be faster here? It's not any more difficult in this case.
	def representation( self, order ):
		if order < 0:
			raise ValueError( "Order must be non-negative." )
		if order not in self.representation_cache:
			
			# We have not yet generated the representation for this order.
			r = []
			for char in self.representation( order - 1 ):
				if char in self.rules:
					r.extend( self.rules[ char ] )
				else:
					r.append( char )
			self.representation_cache[ order ] = r
			
		return self.representation_cache[ order ]

	# Return the nth order lindenmayer pattern.
	# Note that this returns only those symbols labeled as constants.
	def __call__( self, order ):

		# TODO: Use filter, sum....
		result = ''
		for char in self.representation( order ):
			if char in self.constants:
				result = result + char
		return result
