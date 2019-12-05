0.3.2
=====

* Preferring to_dict() to dataclasses.asdict().
  This is because objects might need to be more specific about how they
  should convert themselves to a dict.

0.3.1
=====

* Fixing the serialization of objects inside tuples.

0.3.0
=====

* Supporting tuples for multi-section YAML generation.

0.2.0
=====

Supporting other types for generating dictionaries:

* Classes with a ``to_dict`` method
* Classes from the ``attr`` library
* "Flat" classes that can be serialized through ``__dict__``

0.1.2
=====

* Supporting patchesJson6902

0.1.1
=====

* Supporting patchesStrategicMerge

0.1.0
=====

* First release!
* Supporting dictionaries and dataclasses.
