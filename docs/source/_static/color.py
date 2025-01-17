from ase.build import molecule
from batoms import Batoms
from batoms.butils import removeAll
removeAll()
ch4 = molecule('CH4')
ch4 = Batoms(label = 'ch4', atoms = ch4)
ch4.render.resolution = [200, 200]
ch4.get_image([1, 1, 4], output = 'color_ch4_0.png')

ch4['H'].color = [0, 0, 0.8, 1.0]
ch4['C'].color = [0.8, 0, 0, 1.0]
ch4.get_image([1, 1, 4], output = 'color_ch4_1.png')

ch4['H'].color[3] = 0.2
ch4.get_image([1, 1, 4], output = 'color_ch4_2.png')


removeAll()
ch4 = molecule('CH4')
ch4 = Batoms(label = 'ch4', atoms = ch4)
ch4.model_type = 1
ch4.render.resolution = [200, 200]
ch4.get_image([1, 1, 4], output = 'color_ch4_3.png')
ch4.bondsetting[('C', 'H')].color1 = [0.8, 0.1, 0.3, 0.5]
ch4.bondsetting[('C', 'H')].color2 = [0.1, 0.3, 0.2, 1.0]
ch4.model_type = 1
ch4.get_image([1, 1, 4], output = 'color_ch4_4.png')


removeAll()
ch4 = molecule('CH4')
ch4 = Batoms(label = 'ch4', atoms = ch4)
ch4.bondsetting[('C', 'H')].polyhedra = True
ch4.model_type = 2
ch4.render.resolution = [200, 200]
ch4.get_image([1, 1, 4], output = 'color_ch4_5.png')
ch4.polyhedrasetting['C'].color = [0.8, 0.1, 0.3, 0.8]
ch4.model_type = 2
ch4.get_image([1, 1, 4], output = 'color_ch4_6.png')
