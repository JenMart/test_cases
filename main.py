import random

#
#   Superhero Name Gen - Rom Stevens
#   A simple superhero name generating app with test cases. See tests.py for tests.
#


#
#   Reads lines from a file and stores them into arrays.
#   Provides methods for accessing a random item from each array.
#
class NameGenerator:
    def __init__(self):
        self.adjectives = []
        self.prefixes = []
        self.suffixes = []
        self.verbs = []

        self.read_files()

    def read_files(self):
        file_names = ['adjectives', 'prefixes', 'suffixes', 'verbs']
        for file_name in file_names:
            with open('data/' + file_name + '.txt', 'r') as file:
                for line in file:
                    getattr(self, file_name).append(line.strip('\n'))

    def get_adjective(self):
        return random.choice(self.adjectives)

    def get_prefix(self):
        return random.choice(self.prefixes)

    def get_suffix(self):
        return random.choice(self.suffixes)

    def get_verb(self):
        return random.choice(self.verbs)


#
#   Superhero object. Creates a name with the help of a NameGenerator object.
#   Can state its name using self.battlecry()
#
class Superhero:
    def __init__(self):
        self.name = self.make_name(self.choose_name_format())

    def battlecry(self):
        return self.name + ' is ready to fight evil!'

    def choose_name_format(self):
        adjective_count = random.randint(1,3)

        verb = bool(random.getrandbits(1))
        prefix = bool(random.getrandbits(1))
        suffix = bool(random.getrandbits(1))

        if prefix and suffix:
            choice = random.getrandbits(1)
            if choice > 0:
                prefix = False
            else:
                suffix = False

        return {
            'prefix': prefix,
            'suffix': suffix,
            'verb': verb,
            'adjective_count': adjective_count
        }

    def make_name(self, format):
        generator = NameGenerator()
        n = ''

        if format['prefix']:
            n += generator.get_prefix() + ' '
        for i in range(format['adjective_count']):
            n += generator.get_adjective()
        if format['verb']:
            n += generator.get_verb() + ' '
        else:
            n += ' '
        if format['suffix']:
            n += generator.get_suffix()

        return n


if __name__ == '__main__':
    for i in range(5):
        print Superhero().battlecry()