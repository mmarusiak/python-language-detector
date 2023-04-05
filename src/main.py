import brain


langs = brain.Languages(['pl', 'a', 'en', 'es', 'b', 'd', 'fr', 'tr'])
langs.get_langs()

my_brain = brain.Brain(1, langs)
print(my_brain.guess('Mariusz "Pudzian" Pudzianowski jest ambasadorem Q8Oils Polska, którą jeżdżą różnymi samochodami, ciągnikami oraz motorem i lubię majsterkowaę w warsztacie. Doskonale jak ważną rolę w pojazdach odgrywają środki smarne i jednocześną jesteśmy ambasadorem.'))
print(my_brain.guess('Gabe Logan Newell (nicknamed "Gaben") is the co-founder and current managing director of the independent game development company Valve Software. Newell was educated at Davis Senior High School and attended Harvard University in the early 1980s before dropping out to join Microsoft, where he helped create the Microsoft Windows operating operating system.'))

