Basics
------
Particle
~~~~~~~~
There are a lot of arguments, but required is only center position. So this is the minimal particle example

.. literalinclude:: basics/particle.py
   :language: python3

By running this code you won't see something nice and interesting, it is just a showcase of how to use them

Shape
~~~~~
You can subclass shape object to create your own

.. literalinclude:: basics/shape.py
   :language: python3

Now you can use this `CustomShape` as `shape_cls` argument for particle

Container
~~~~~~~~~
Container is an object which has some methods to make your work easier

.. literalinclude:: basics/container.py
   :language: python3

Random in range
~~~~~~~~~~~~~~~
Particle's speed and size can be a single number or a tuple.

.. code-block:: python3

    3 # Just 3
    3.5 # Just 3.5
    (1, 3) # A random integer value in range [1, 3]
    (1, 3.5) # A random float value in range [1, 3.5]
