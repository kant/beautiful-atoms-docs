from ase.build import molecule
from ase import Atoms
from batoms.batoms import Batoms
from ase.collections import g2
atoms = Atoms()
n = 0
for name in g2.names:
    mol = molecule(name)
    i = int(n/15)
    j = n - i*15
    print(i, j)
    mol.translate([8*j, -8*i, 0])
    atoms = atoms + mol
    n+=1

batoms = Batoms(label = 'mol', atoms = atoms)
batoms.render.resolution = [1500, 1500]
batoms.get_image(output = 'mols.png')



