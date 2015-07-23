"""
Def
F
U
N
C
T
I
O
N
"""
"""
Calling Function
"""
def PrintFunc( str ):
   print str;
   return;

#PrintFunc
PrintFunc("Yo! Function ");
PrintFunc("Print!!!!");

"""
Pass by Value
"""
#square Function Here!
def square(Val):
   SquareRel=Val*Val
   print "Got Value and Square equal=", SquareRel
   return SquareRel

# Throw Value to square Function
three=3
REL = square(three);
print "Values After Square = ", REL
