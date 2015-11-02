import unittest
from main import *


class TestSuperheroMethods(unittest.TestCase):

    # Should successfully create a superhero
    def test_create(self):
        hero = Superhero()
        self.assertIsNotNone(hero)

    # Should only allow suffix or prefix, not both
    # Should have at least 1 adjective
    def test_name_format(self):
        f = Superhero().choose_name_format()
        if f['prefix']:
            self.assertFalse(f['suffix'])
        if f['suffix']:
            self.assertFalse(f['prefix'])
        self.assertGreater(f['adjective_count'], 0)

    # Should successfully get the hero's name
    def test_battlecry(self):
        hero = Superhero()
        self.assertEqual(hero.battlecry(), hero.name + ' is ready to fight evil!')


class TestNameGenMethods(unittest.TestCase):

    # Should read from a file and strip new lines
    def test_read_files(self):
        array = []
        generator = NameGenerator()
        with open('data/adjectives.txt', 'r') as file:
            for line in file:
                array.append(line.strip('\n'))

        self.assertEqual(len(array), len(generator.adjectives))
        for adjective in generator.adjectives:
            self.assertNotIn('\n', adjective)

    # Should get an attribute correctly from each list
    def test_get_attributes(self):
        generator = NameGenerator()

        self.assertIn(generator.get_adjective(), generator.adjectives)
        self.assertIn(generator.get_prefix(), generator.prefixes)
        self.assertIn(generator.get_suffix(), generator.suffixes)
        self.assertIn(generator.get_verb(), generator.verbs)
