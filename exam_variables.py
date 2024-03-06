# Question 3
test_strings = ['random string', '0', '0.1', '0,1', '100',
                '1000', '1.000', '1,000', 'not a number']

EU_wikitext = "The European Union is a supranational political \
and economic union of 27 member states that are located primarily \
in Europe. The union has a total area of 4,233,255 km2 \
(1,634,469 sq mi) and an estimated total population of over \
448 million. Containing 5.8% of the world population in 2020, \
EU member states generated a nominal gross domestic product (GDP) \
of around US$ 16.6 trillion in 2022, constituting approximately \
one sixth of global nominal GDP."


# Question 4
annotated_sentence = "A__DET language__NOUN family__NOUN is__AUX a__DET \
group__NOUN of__ADP languages__NOUN related__VERB through__ADP \
descent__NOUN from__ADP a__DET common__ADJ ancestral__ADJ language__NOUN \
or__CCONJ parental__ADJ language__NOUN ,__PUNCT called__VERB the__DET \
proto__NOUN -__PUNCT language__NOUN of__ADP that__DET family__NOUN"

function_words_tags = ["ADP", "AUX", "CCONJ", "DET", "PRON"]


# Question 6
language_data = {
    'Albanian': {'Family': 'Indo-European',
                 'Genus': 'Albanian',
                 'Word Order': 'SVO'},
    'Amara': {'Family': 'Austronesian',
              'Genus': 'Oceanic',
              'Word Order': 'SVO'},
    'Arabic (Modern Standard)': {'Family': 'Afro-Asiatic',
                                 'Genus': 'Semitic',
                                 'Word Order': 'VSO'},
    'Basque': {'Family': 'Basque',
               'Genus': 'Basque',
               'Word Order': 'SOV'},
    'Burmese': {'Family': 'Sino-Tibetan',
                'Genus': 'Burmese-Lolo',
                'Word Order': 'SOV'},
    'Catalan': {'Family': 'Indo-European',
                'Genus': 'Romance',
                'Word Order': 'SVO'},
    'Enets': {'Family': 'Uralic',
              'Genus': 'Samoyedic',
              'Word Order': 'SOV'},
    'English': {'Family': 'Indo-European',
                'Genus': 'Germanic',
                'Word Order': 'SVO'},
    'Finnish': {'Family': 'Uralic',
                'Genus': 'Finnic',
                'Word Order': 'SVO'},
    'Hawaiian': {'Family': 'Austronesian',
                 'Genus': 'Oceanic',
                 'Word Order': 'VSO'},
    'Hindi': {'Family': 'Indo-European',
              'Genus': 'Indic',
              'Word Order': 'SOV'},
    'Igbo': {'Family': 'Niger-Congo',
             'Genus': 'Igboid',
             'Word Order': 'SVO'},
    'Irish': {'Family': 'Indo-European',
              'Genus': 'Celtic',
              'Word Order': 'VSO'},
    'Macedonian': {'Family': 'Indo-European',
                   'Genus': 'Slavic',
                   'Word Order': 'SVO'},
    'Mandarin': {'Family': 'Sino-Tibetan',
              'Genus': 'Chinese',
              'Word Order': 'SVO'},
    'Persian': {'Family': 'Indo-European',
             'Genus': 'Iranian',
             'Word Order': 'SOV'},
    'Tamil': {'Family': 'Dravidian',
              'Genus': 'Dravidian',
              'Word Order': 'SOV'},
    'Tolai': {'Family': 'Austronesian',
              'Genus': 'Oceanic',
              'Word Order': 'SVO'},
    'Turkish': {'Family': 'Altaic',
                'Genus': 'Turkic',
                'Word Order': 'SOV'},
    'Yucatek': {'Family': 'Mayan',
                'Genus': 'Mayan',
                'Word Order': 'SOV'}}


# Question 7
class Recipe:

    def __init__(self, name, ingredients, instructions=""):
        self.name = name
        self.ingredients = set(ingredients)
        self.instructions = instructions

    def has_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        return False

    def display_allergens(self, additional_allergens=None):
        common_allergens = {"wheat", "shellfish", "peanuts", "eggs"}

        if additional_allergens is not None:
            common_allergens = common_allergens.union(set(additional_allergens))

        set_common_allergens = set(common_allergens)
        print(f'Contained allergens: {", ".join(set_common_allergens.intersection(self.ingredients))}')

    def print_recipe(self):
        print(f"{self.name.title()}")
        print("-" * len(self.name))
        print(f"List of ingredients: {', '.join(self.ingredients)}")
        if self.instructions != "":
            print(f"\nInstructions:\n{self.instructions}")


simple_cake = ['flour', 'sugar', 'butter', 'eggs', 'baking powder', 'milk']
instructions = "Preheat oven to 180 degrees..."
