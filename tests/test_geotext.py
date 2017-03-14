#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_geotext
----------------------------------

Tests for `geotext` module.
"""

import unittest
import geotext


class TestGeotext(unittest.TestCase):
    def setUp(self):
        pass

    def test_cities(self):

        text = """São Paulo é a capital do estado de São Paulo. As cidades de Baruerí
                  e Carapicuíba fazem parte da Grade São Paulo. O Rio de Janeiro
                  continua lindo. No carnaval eu vou para Salvador. No reveillon eu 
                  quero ir para Santos."""
        result = geotext.GeoText(text).cities
        expected = [
            'São Paulo', 'São Paulo', 'Carapicuíba', 'Salvador', 'Santos'
        ]
        self.assertEqual(result, expected)

    def test_nationalities(self):

        text = 'Japanese people like anime. French people often drink wine. Chinese people enjoy fireworks.'
        result = geotext.GeoText(text).nationalities
        expected = ['Japanese', 'French', 'Chinese']
        self.assertEqual(result, expected)

    def test_countries(self):

        text = """That was fertile ground for the emergence of various forms of
                  totalitarian governments such as Japan, Italy,
                  and Germany, as well as other countries"""
        result = geotext.GeoText(text).countries
        expected = ['Japan', 'Italy', 'Germany']
        self.assertEqual(result, expected)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
