from gato import Gato
from cachorro import Cachorro
from canarinho import Canarinho

gato = Gato()
print(gato.miar())
print(gato.mover())
print("")

cachorro = Cachorro()
print(cachorro.latir())
print(cachorro.mover())
print("")

can = Canarinho(2)
print(can.cantar())
print(can.mover())
print("")

can.altura_voo = 10
print(can.mover())
