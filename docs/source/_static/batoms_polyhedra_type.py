from ase.build import molecule
from batoms.butils import removeAll
from batoms import Batoms

removeAll()
ch4 = Batoms(label = 'ch4', atoms = molecule('CH4'))
ch4.bondsetting[('C', 'H')].polyhedra = True
ch4['H'].color = [0, 0, 0.8, 1.0]
ch4['C'].color = [0.8, 0, 0, 1.0]
ch4.polyhedrasetting['C'].color = [0.8, 0.1, 0.3, 0.3]
ch4.model_type = 2
ch4.render.resolution = [500, 500]
for polyhedra_type in [0, 1, 2, 3]:
    ch4.polyhedra_type = polyhedra_type
    ch4.get_image(viewport = [1, 1, 4], output = 'batoms_polyhedra_type_%s.png'%polyhedra_type)
