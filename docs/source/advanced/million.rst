==========================================
How to render million of atoms
==========================================

:class:`Batom` object has parameter ``segments``. The default value is ``[32, 16]``. Set it to ``[6, 6]`` for large system.

Here we creat a system with 1 million of gold atoms.

>>> from ase.build import bulk
>>> from batoms import Batoms
>>> au = bulk('Au', cubic = True)
>>> au = Batoms(label = 'au', atoms = au, segments = [6, 6])
>>> au.repeat([10, 10, 20])
>>> au.repeat([5, 5, 5])
>>> au.get_image(viewport = [1, 0, 0])

.. image:: ../_static/figs/million_au.png
   :width: 8cm


