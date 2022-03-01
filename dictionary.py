import json
from difflib import SequenceMatcher as Sm

class DictionaryEn:

    def __init__(self, filepath):
        self.data = json.load(open(filepath))
        self.ratios = {}

    def get_word(self):
        word = input('Please insert a word: ')
        return word.lower()

    def ratio_maker(self, word):
        self.ratios = {k: [v, Sm(None, k, word).ratio()] for k, v in self.data.items()}
        return self.ratios

    def translate(self):
        if len(self.ratios) > 0:
            max_match = max(self.ratios, key=lambda k: self.ratios[k][1])
            if self.ratios[max_match][1] == 1:
                return print(*self.ratios[max_match][0], sep='\n')
            elif self.ratios[max_match][1] > 0.8:
                question = input("Did you mean {}? Press Y if yes and N if no. ".format(max_match))
                if question.lower() in ['y', 'n']:
                    if question.lower() == 'y':
                        return print(*self.ratios[max_match][0], sep='\n')
                    else:
                        return print('Ok. Bye!')
                else:
                    return print('Wrong letter. Bye!')
            else:
                return print('No match found. Bye!')
        else:
            return print('Please calculate ratios first with ratio_maker(word)')


if __name__ == '__main__':
    d = DictionaryEn('data.json')
    d.ratio_maker(d.get_word())
    d.translate()
