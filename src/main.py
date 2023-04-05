import brain


def test_set():
    langs = brain.Languages(['pl', 'a', 'en', 'es', 'b', 'd', 'fr', 'tr'])
    langs.get_langs()

    my_brain = brain.Brain(1, langs)
    print(my_brain.guess('Mariusz "Pudzian" Pudzianowski jest ambasadorem Q8Oils Polska, którą jeżdżą różnymi '
                         'samochodami, ciągnikami oraz motorem i lubię majsterkowaę w warsztacie. Doskonale jak ważną '
                         'rolę w pojazdach odgrywają środki smarne i jednocześną jesteśmy ambasadorem.'))
    print(my_brain.guess('Gabe Logan Newell (nicknamed "Gaben") is the co-founder and current managing director of '
                         'the independent game development company Valve Software. Newell was educated at Davis '
                         'Senior High School and attended Harvard University in the early 1980s before dropping out '
                         'to join Microsoft, where he helped create the Microsoft Windows operating operating '
                         'system.'))



def user_playground():
    languages = input("Please enter all languages you want to consider (all languages that brain needs to \"learn\") "
                      "(separate them with space):")
    converted_languages = languages.split()
    brain_languages = brain.Languages(converted_languages)

    # get precision
    while True:
        try:
            precision = int(input("Please enter precision (how many articles you want brain to read for each "
                                  "language): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    min_article_size = input("Provide minimum amount of letters that article needs to contain (enter nothing or "
                             "string if you are not sure, brain will take default value = 250):")

    if min_article_size is int:
        user_brain = brain.Brain(precision, brain_languages, min_article_size)
    else:
        user_brain = brain.Brain(precision, brain_languages)

    print(user_brain.guess(input("Enter text to guess:")))


#test_set()
user_playground()

