from ase.build import molecule
from batoms.butils import removeAll
from batoms import Batoms

removeAll()
co = Batoms(label = 'co', atoms = molecule('CO'))
co.bondsetting[('C', 'O')].style = '0'
co.model_type = 1
co.render.viewport = [1, 0, 0]
co.render.resolution = [500, 500]
co.get_image(output = 'bondsetting_style_0.png')
#
co.bondsetting[('C', 'O')].style = '1'
co.model_type = 1
co.get_image(output = 'bondsetting_style_1.png')
#
co.bondsetting[('C', 'O')].style = '2'
co.bondsetting[('C', 'O')].width = 0.01
co.model_type = 1
co.get_image(output = 'bondsetting_style_2.png')
#
co.bondsetting[('C', 'O')].style = '3'
co.bondsetting[('C', 'O')].width = 0.01
co.model_type = 1
co.get_image(output = 'bondsetting_style_3.png')
