class GulfDialect:
    def __init__(self):
        self.gulf_to_ipa = {
            'ب': 'b',
            'ت': 't',
            'ث': 'θ',   
            'ج': 'j',      
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
            'ق': 'g',      # Gulf: g sound
            'ك': 'k',
            'ل': 'l',
            'م': 'm',
            'ن': 'n',
            'ه': 'h',
            'و': 'w',
            'ي': 'j',
            'ء': 'ʔ',
            'ا': 'aː',
            'ى': 'aː',
             'َ': 'a',
            'ِ': 'i', 
            'ُ': 'u',
            'ً': 'an',
            'ٍ': 'in',
            'ٌ': 'un',
            'ْ': ''
        }
        
     

    def transcribe(self, word):
        tanween = ['ً', 'ٍ', 'ٌ']
        for t in tanween:
            word = word.replace(t, '')
        
        result = ''
        for c in word:
            if c in self.gulf_to_ipa:
                result += self.gulf_to_ipa[c]
            else:
                result += c
        
        return result