========
Usage
========

To use geotext in a project::

    from geotext import GeoText
    
    places = GeoText("London is a great city")
    places.cities
    # "London"
    
    GeoText('New York, Texas, and also China').country_mentions
    # OrderedDict([(u'US', 2), (u'CN', 1)])
