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

        text = """São Paulo é a capital do estado de São Paulo. As cidades de Barueri
                  e Carapicuíba fazem parte da Grade São Paulo. O Rio de Janeiro
                  continua lindo. No carnaval eu vou para Salvador. No reveillon eu 
                  quero ir para Santos."""
        result = geotext.GeoText(text).cities
        expected = [
            'São Paulo', 'São Paulo', 'Barueri', 'Carapicuíba', 'Rio de Janeiro', 'Salvador', 'Santos'
        ]
        self.assertEqual(result, expected)

        brazillians_northeast_capitals = """As capitais do nordeste brasileiro são:
                                            Salvador na Bahia, 
                                            Recife em Pernambuco, 
                                            Natal fica no Rio Grande do Norte, 
                                            João Pessoa fica na Paraíba, 
                                            Fortaleza fica no Ceará, 
                                            Teresina no Piauí, 
                                            Aracaju em Sergipe,
                                            Maceió em Alagoas e 
                                            São Luís no Maranhão."""
        result = geotext.GeoText(brazillians_northeast_capitals).cities
        # PS: 'Rio Grande' is not a northeast city, but is a brazilian city
        expected = [
            'Salvador', 'Recife', 'Natal', 'Rio Grande', 'João Pessoa', 'Fortaleza', 'Teresina', 'Aracaju', 'Maceió', 'São Luís'
        ]
        self.assertEqual(result, expected)


        brazillians_north_capitals = """As capitais dos estados do norte brasileiro são: 
                                        Manaus no Amazonas, 
                                        Palmas em Tocantins,
                                        Belém no Pará,
                                        Acre no Rio Branco."""
        result = geotext.GeoText(brazillians_north_capitals).cities
        expected = [
            'Manaus', 'Palmas', 'Belém', 'Rio Branco'
        ]
        self.assertEqual(result, expected)

        brazillians_southeast_capitals = """As capitais da região sudeste do Brasil são:
                                            Rio de Janeiro no Rio de Janeiro,
                                            São Paulo em São Paulo,
                                            Belo Horizonte em Minas Gerais,
                                            Vitória no Espírito Santo"""
        result = geotext.GeoText(brazillians_southeast_capitals).cities
        # 'Rio de Janeiro' and 'Sao Paulo' city and state name are the same, so appears 2 times, it's ok!
        expected = [
            'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo', 'São Paulo', 'Belo Horizonte', 'Vitória'
        ]
        self.assertEqual(result, expected)

        brazillians_central_capitals = """As capitais da região centro-oeste do Brasil são: 
                                          Goiânia em Goiás, 
                                          Brasília no Distrito Federal,
                                          Campo Grande no Mato Grosso do Sul,
                                          Cuiabá no Mato Grosso."""
        result = geotext.GeoText(brazillians_central_capitals).cities
        expected = [
            'Goiânia', 'Goiás', 'Brasília', 'Campo Grande', 'Cuiabá'
        ]
        self.assertEqual(result, expected)

        brazillians_south_capitals = """As capitais da região sul são:
                                        Porto Alegre no Rio Grande do Sul,
                                        Floripa em Santa Catarina, 
                                        Curitiba no Paraná"""
        result = geotext.GeoText(brazillians_south_capitals).cities
        # PS: 'Rio Grande' is not a south city, but is a brazilian city
        expected = [
            'Porto Alegre', 'Rio Grande', 'Santa Catarina', 'Curitiba', 'Paraná'
        ]
        self.assertEqual(result, expected)

        result = geotext.GeoText('Rio de Janeiro y Havana', 'BR').cities
        expected = [
            'Rio de Janeiro'
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
