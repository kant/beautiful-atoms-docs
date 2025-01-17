==========================================
Motion blur
==========================================

Application sences:

- Molecular dynamics simulation
- Diffusion
- Dissociation
- ...


In this tutorial we creat four water molecules and move it in different directions.

>>> from batoms import Batoms
>>> from ase import Atoms
>>> from ase.build import molecule
>>> h2o = molecule('H2O')
>>> images = []
>>> for i in range(20):
>>>     atoms = Atoms()
>>>     for j in [-1, 1]:
>>>         for k in [-1, 1]:
>>>             temp = h2o.copy()
>>>             temp.translate([i/3*j, i*i/50*k, 0])
>>>             atoms = atoms + temp
>>>     images.append(atoms)

Load trajecty to ``Batoms``:

>>> h2o = Batoms(label = 'h2o', atoms = images, movie = True)

Render the ``10th`` frame with ``eevee`` engine. Set ``use_motion_blur`` to ``True``.

>>> from batoms.butils import set_world
>>> h2o.render.use_motion_blur = True
>>> h2o.render.camera.ortho_scale = 30
>>> h2o.render.transparent = False
>>> set_world([0.1, 0.1, 0.1, 1.0])
>>> h2o.get_image(engine = 'eevee', 
>>>                frame = 10, 
>>>                canvas = [30, 30, 10])




.. image:: ../_static/figs/motion_blur_h2o.png
   :width: 8cm


