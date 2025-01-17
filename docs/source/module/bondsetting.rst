.. module:: batoms.bondsetting

========================
The Bondsetting object
========================

The :class:`Bondsetting` object is used to store and set all parameters related with bonds. It is a collection of :class:`BatomsBond` object. It should always bind with a :class:`Batoms` object. Possible keywords are: ``symbol1``, ``symbol2``, ``min``, ``max``, ``search``, ``polyhedra``, ``color1``, ``color2``, ``bondlinewidth``, ``style``. 


>>> from ase.build import molecule
>>> from batoms import Batoms
>>> ch4 = Batoms('ch4', atoms = molecule('CH4'))
>>> ch4.model_type = 2

.. image:: ../_static/figs/bondsetting_ch4_0.png
   :width: 5cm

You can print the default bondsetting by:

>>> ch4.bondsetting

.. image:: ../_static/figs/bondsetting_ch4_1.png
   :width: 15cm

By defaut, we use default radius (``ase.data.covalent_radii``) for every atoms, and the maximum bondlength is the sum of two radius and then scaled by a default cutoff (1.3). The minimum bondlength is 0.5.


Style
===========
One set the bond style by:

>>> ch4.bondsetting[('C', 'H')].style = '0'

Here, four polyhedra model are supported.

.. list-table::
   :widths: 25 25 25 25

   * - ``0``
     - ``1``
     - ``2``
     - ``3``
   * -  .. image:: ../_static/figs/bondsetting_style_0.png 
     -  .. image:: ../_static/figs/bondsetting_style_1.png 
     -  .. image:: ../_static/figs/bondsetting_style_2.png 
     -  .. image:: ../_static/figs/bondsetting_style_3.png 
  

Polyhedra
==================

One can change setting for a bond pair. For example, to build up coordination polyhedra, the value for ``polyhedra`` should be set to ``True``:

>>> ch4.bondsetting[('C', 'H')].polyhedra = True
>>> ch4.model_type = 2


.. image:: ../_static/figs/bondsetting_ch4_2.png
   :width: 5cm


Search bond mode
==================
 
 - ``0``  Do not search atoms beyond the boundary
 - ``1``  Search additional atoms if species1 is included in the boundary
 - ``2``  Search bonded atoms of species1 or species2 recursively. This mode is the used for searching molecules.

To change setting for ``search`` by:

>>> tio2.bondsetting[('Ti', 'O')].search = 0
>>> tio2.update_boundary()
>>> tio2.model_type = 2


.. image:: ../_static/figs/bondsetting_tio2_2.png
   :width: 8cm


Color
==================

One can print the default color by:

>>> ch4.bondsetting[('C', 'H')].color1[:]

One can change color for a bond pair. 

>>> ch4.bondsetting[('C', 'H')].color1 = [0.8, 0.1, 0.3, 0.5]
>>> ch4.bondsetting[('C', 'H')].color2 = [0.1, 0.3, 0.2, 1.0]
>>> ch4.model_type = 1


.. image:: ../_static/figs/bondsetting_ch4_3.png
   :width: 5cm


High order bond
=====================

One can change bond order by:

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> co2 = Batoms('co2', atoms = molecule('CO2'))
>>> co2.bondsetting[('C', 'O')].order = 2
>>> co2.bondsetting[('C', 'O')].width = 0.05
>>> co2.model_type = 1

.. image:: ../_static/figs/bondsetting_order.png
   :width: 5cm


List of all Methods
===================

.. autoclass:: Bondsetting
   :members: