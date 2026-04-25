# file Name LDialect

class LevDialect:
    def __init__(self):

        self.levantine_to_ipa = {

        # Consonants
        'ب': 'b',
        'ت': 't',
        'ث': 's',      
        'ج': 'ʒ',      
        'ح': 'ħ',
        'خ': 'x',
        'د': 'd',
        'ذ': 'z',
        'ر': 'r',
        'ز': 'z',
        'س': 's',
        'ش': 'ʃ',

        'ص': 'sˤ',
        'ض': 'dˤ',
        'ط': 'tˤ',
        'ظ': 'zˤ',

        'ع': 'ʕ',
        'غ': 'ɣ',

        'ف': 'f',
        'ق': 'ʔ',  
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',

        'ء': 'ʔ',

        # Glides
        'و': 'w',
        'ي': 'j',

        # Vowels
        'ا': 'aː',
        'و': 'uː',
        'ي': 'iː',
        }

    def transcribe(self, word):
        diacritics = ['َ', 'ِ', 'ُ', 'ْ', 'ً', 'ٍ', 'ٌ', 'ّ']
        for d in diacritics:
            word = word.replace(d, '')
        return ''.join(self.levantine_to_ipa.get(c, c) for c in word)