# file Name IrDialect
class IraqiDialect:
    def __init__(self):

        self.iraqi_to_ipa = {

        'ب': 'b',
        'ت': 't',
        'ث': 'θ',  
        'ج': 'dʒ',
        'ح': 'ħ',
        'خ': 'x',
        'د': 'd',
        'ذ': 'ð',
        'ر': 'r',
        'ز': 'z',
        'س': 's',
        'ش': 'ʃ',

        'ص': 'sˤ',
        'ض': 'dˤ',
        'ط': 'tˤ',
        'ظ': 'ðˤ',

        'ع': 'ʕ',
        'غ': 'ɣ',

        'ف': 'f',
        'ق': 'g',   # often g like Gulf
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',

        'ء': 'ʔ',

        'و': 'w',
        'ي': 'j',
         'َ': 'a',
        'ِ': 'i',
        'ُ': 'u',

        'ا': 'aː',
        'و': 'uː',
        'ي': 'iː',
        }

    def transcribe(self, word):
        tanween = ['ً', 'ٍ', 'ٌ']
        for t in tanween:
            word = word.replace(t, '')
        return ''.join(self.iraqi_to_ipa.get(c, c) for c in word)