import brain

print ('hello world?')

langs = brain.Languages(['pl', 'a', 'en', 'es', 'b', 'd'])
langs.get_langs()

my_brain = brain.Brain(2, langs)