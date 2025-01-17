from ase import atoms
from ase.build import surface
from ase.io import read
from batoms import Batoms
from batoms.bdraw import draw_plane
import numpy as np
from batoms.butils import removeAll
from ase.cluster import wulff_construction
removeAll()
surfaces = [(1, 1, 1), (1, 0, 0)]
energies = [1.28, 1.69]
nano = wulff_construction('Au', surfaces, energies, 30, 'fcc')
del nano[nano.positions[:, 2] < 0]
nano = Batoms('nano', atoms = nano)
bulk = read('docs/source/_static/datas/ceo2.cif')
slab111 = surface(bulk, (1, 1, 1), 4, vacuum = 0, periodic=True)
slab111 = slab111*[20, 10, 1]
slab111 = Batoms('CeO2-111', atoms = slab111)
slab111['Ce'].color = [0.1, 0.6, 0.3, 1.0]
com = slab111.get_center_of_mass()
nano.translate([com[0], com[1]-25, max(slab111.positions[:, 2]) + 2.0])
nano1 = nano.copy()
nano1.translate([-15, 15, 0])
draw_plane(size = 1000, location = (0, 0, min(slab111.positions[:, 2]) - slab111['O'].size[0]),  
        color = [0.9, 0.9, 0.9, 1.0])
com = nano.get_center_of_mass()
slab111.render.lights['Default'].type = 'POINT'
slab111.render.lights['Default'].lock_light_to_camera = False
slab111.render.lights['Default'].energy = 500000
slab111.render.lights['Default'].location = [com[0], com[1]-15, max(nano.positions[:, 2]) + 15]
slab111.render.camera.location = [com[0], com[1]-15, max(nano.positions[:, 2]) + 10]
slab111.render.engine = 'cycles'
slab111.render.camera.type = 'PERSP'
slab111.get_image(center = com, output = 'gallery_oxide_surface.png')