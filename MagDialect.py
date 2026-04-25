# File Name MDialect

class MaghrebiDialect:
    def __init__(self):

        self.maghrebi_to_ipa = {

        'ب': 'b',
        'ت': 't',
        'ث': 't',   # often → t
        'ج': 'ʒ',
        'ح': 'ħ',
        'خ': 'x',
        'د': 'd',
        'ذ': 'd',   # → d
        'ر': 'r',
        'ز': 'z',
        'س': 's',
        'ش': 'ʃ',

        'ص': 'sˤ',
        'ض': 'dˤ',
        'ط': 'tˤ',
        'ظ': 'dˤ',

        'ع': 'ʕ',
        'غ': 'ɣ',

        'ف': 'f',
        'ق': 'q',   # often stays q!
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',
         'َ': 'a',
        'ِ': 'i',
        'ُ': 'u',

        'ء': 'ʔ',

        'و': 'w',
        'ي': 'j',

        'ا': 'a',
        'و': 'u',
        'ي': 'i',
        }

    def transcribe(self, word):
       
        word = word.strip()

       
        tanween = ['ً', 'ٍ', 'ٌ']
        for t in tanween:
            word = word.replace(t, '')

        result = ""
        i = 0

        while i < len(word):
            char = word[i]

           
            if char == 'ّ':
                if result:
                    result += result[-1]
                i += 1
                continue

           
            if char == 'ا':
                result += 'a'
                i += 1
                continue

            elif char == 'و':
                
                if i > 0 and word[i-1] in ['َ', 'ِ', 'ُ']:
                    result += 'w'
                else:
                    result += 'u'
                i += 1
                continue

            elif char == 'ي':
                if i > 0 and word[i-1] in ['َ', 'ِ', 'ُ']:
                    result += 'j'
                else:
                    result += 'i'
                i += 1
                continue

            # =====================
            # NORMAL MAPPING
            # =====================
            if char in self.maghrebi_to_ipa:
                result += self.maghrebi_to_ipa[char]
            else:
                result += char

            i += 1

        return result