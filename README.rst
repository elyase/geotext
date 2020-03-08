===============================
geotext
===============================

.. image:: https://img.shields.io/pypi/v/geotext.svg
        :target: https://pypi.python.org/pypi/geotext

.. image:: https://img.shields.io/pypi/pyversions/geotext.svg
        :target: https://pypi.python.org/pypi/geotext
        
.. image:: https://travis-ci.org/elyase/geotext.png?branch=master
        :target: https://travis-ci.org/elyase/geotext


Geotext extracts country and city mentions from text

* Free software: MIT license
* Documentation: https://geotext.readthedocs.org.

Usage
-----
.. code-block:: python

        from geotext import GeoText
        
        places = GeoText("London is a great city")
        places.cities
        # "London"

        # filter by country code
        result = GeoText('I loved Rio de Janeiro and Havana', 'BR').cities
        # 'Rio de Janeiro'
        
        GeoText('New York, Texas, and also China').country_mentions
        # OrderedDict([(u'US', 2), (u'CN', 1)])

Installation
------------
.. code-block:: bash

        pip install https://github.com/elyase/geotext/archive/master.zip


Features
--------
- No external dependencies
- Fast
- Data from http://www.geonames.org licensed under the Creative Commons Attribution 3.0 License.

Similar projects
----------------
`geography
<https://github.com/ushahidi/geograpy>`_: geography is more advanced and bigger in scope compared to geotext and can do everything geotext does. On the other hand geotext is leaner: has no external dependencies, is faster (re vs nltk) and also depends on libraries and data covered with more permissive licenses.
