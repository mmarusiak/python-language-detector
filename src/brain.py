import numpy as np
import wikipedia

class Languages:
    def_langs = []
    langs = []

    def __init__(self, input_lang):
        self.def_langs = self.load_default_langs()
        self.raw_langs = input_lang
        self.fix_langs()

    def load_default_langs(self):
        return [[a.split('-')[1], a.split('-')[0]] for a in open('languages.txt').read().split()]

    def fix_langs(self):
        # fix given languages to get languages that are on list of langs
        raw_def = np.array(self.def_langs).flatten()
        for lang in self.raw_langs:
            lower = lang.lower()
            # if language is ambiguous then pass this language
            if lower not in raw_def:
                continue
            for target in self.def_langs:
                if lower in target:
                    self.langs.append(target)
                    break
        pass
    def get_langs(self):
        return self.langs

class Brain:
    data_set = []

    def __init__(self, precision, languages):
        self.precision = precision
        self.languages = languages
        self.load_data_set()
        print(self.data_set)

    def load_data(self, language):
        wikipedia.set_lang(language)
        page = wikipedia.random()
        try:
            text = wikipedia.page(page).content
        except wikipedia.exceptions.DisambiguationError as e:
            # If the page name is ambiguous, try again
            return self.load_data(language)
        return text
    def load_data_set(self):
        for language in self.languages.langs:
            new_set = [language, []]
            i = 0
            while i < self.precision:
                article = self.load_data(language[0]).replace("\n", " ")
                new_set[1].append(article)
                i += 1
            self.data_set.append(new_set)