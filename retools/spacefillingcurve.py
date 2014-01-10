from lindenmayer import *
from path import *

hilbert_curve_rep = LindenmayerSystem( 'AB', 'FRL', 'A', {'A':'LBFRAFARFBL','B':'RAFLBFBLFAR'} )
peano_curve_rep = LindenmayerSystem( 'AB', 'FRL', 'A', {'A':'AFBFALFLBFAFBRFRAFBFA','B':'BFAFBRFRAFBFALFLBFAFB'} )
moore_curve_rep = LindenmayerSystem( 'AB', 'FRL', 'AFALFLAFA', {'A':'RBFLAFALFBR', 'B':'LAFRBFBRFAL'} )

hilbert_curve = lambda order: trace( hilbert_curve_rep( order ) )
peano_curve = lambda order: trace( peano_curve_rep( order ) )
moore_curve = lambda order: trace( moore_curve_rep( order ) )

if __name__ == '__main__':
	render( hilbert_curve( 4 ) )
