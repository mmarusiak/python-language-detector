import numpy as np
import wikipedia


class Languages:
    def_langs = []
    langs = []

    def __init__(self, input_lang):
        self.def_langs = self.load_default_langs()
        self.raw_langs = input_lang
        self.fix_langs()

    @staticmethod
    def load_default_langs():
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
    min_data_size = 250

    def __init__(self, precision, languages, data_size = 250):
        self.precision = precision
        self.languages = languages
        self.min_data_size = data_size
        self.load_data_set()

    def load_data(self, language):
        # load single data from wikipedia
        wikipedia.set_lang(language)
        page = wikipedia.random()
        try:
            text = wikipedia.page(page).content
        except wikipedia.exceptions.DisambiguationError as e:
            # If the page name is ambiguous, try again
            return self.load_data(language)
        # get only articles that are long enough
        if len(text) < self.min_data_size:
            return self.load_data(language)
        return text

    def load_data_set(self):
        # load data set - load each data for language and parametrize it
        for language in self.languages.langs:
            new_set = [language, []]
            i = 0
            articles = ''
            while i < self.precision:
                article = self.load_data(language[0]).replace("\n", " ")
                articles += article
                i += 1
            new_set[1] = (self.parametrization(articles))
            self.data_set.append(new_set)

    @staticmethod
    def parametrization(text):
        text = text.lower()
        num_letters = [text.count(chr(i+97)) for i in range(ord('z') - ord('a') + 1)]
        param_letters = [num_letters[i]/sum(num_letters) * 100 for i in range(ord('z') - ord('a') + 1)]
        return param_letters

    @staticmethod
    def dist(a, b):
        dist = 0
        for i in range(len(a)):
            dist += (a[i] - b[i])**2
        return dist

    def guess(self, text):
        new_p = self.parametrization(text)
        mind = -1
        current_language = ''
        for data in self.data_set:
            newd = self.dist(new_p, data[1])
            if mind == -1 or newd < mind:
                mind = newd
                current_language = data[0]
        return current_language
