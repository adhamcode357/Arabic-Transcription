# file Name EDialect


class EgyDialect:
    def __init__(self):

        self.egyptian_to_ipa = {

       

        'ب': 'b',
        'ت': 't',
        'ث': 's',     
        'ج': 'g',      
        'ح': 'ħ',
        'خ': 'x',
        'د': 'd',
        'ذ': 'z',      # ð → z
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
        'ق': 'ʔ',      # q → glottal stop / 2
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',

        'ء': 'ʔ',

        # =====================
        # Semi-vowels / Glides
        # =====================

        'و': 'w',      # consonant
        'ي': 'j',      # consonant

        # =====================
        # Vowels (short)
        # =====================

        'َ': 'a',
        'ِ': 'i',
        'ُ': 'u',

       
        'ا': 'aː',
        'و': 'uː',
        'ي': 'iː',

       
       

       
        '2': 'ʔ',  
        '3': 'ʕ',   
        '7': 'ħ'    

    }

        
        
    
        
    def transcribe(self, word):
    
        word = word.strip()

        
        tanween = ['ً', 'ٍ', 'ٌ']
        for t in tanween:
            word = word.replace(t, '')

        word = word.replace('أ', 'ء')
        word = word.replace('إ', 'ء')
        word = word.replace('ؤ', 'ء')
        word = word.replace('ئ', 'ء')

        replacements = {
            'ق': 'ء',   # glottal stop (2)
            'ج': 'g',
            'ث': 's',
            'ذ': 'z',
            'ظ': 'z',
            'خ': 'x',
            'غ': 'ɣ',
            'ش': 'ʃ',
        }

        for ar, eg in replacements.items():
            word = word.replace(ar, eg)

     
     

        result = ""
        i = 0

        while i < len(word):
            char = word[i]

            
            if char == 'ا':
                result += 'aː'

            elif char == 'و':
                
                if i > 0 and word[i - 1] in ['a', 'i', 'u']:
                    result += 'w'
                else:
                    result += 'uː'

            elif char == 'ي':
                if i > 0 and word[i - 1] in ['a', 'i', 'u']:
                    result += 'j'
                else:
                    result += 'iː'

           
            else:
                if char in self.egyptian_to_ipa:
                    result += self.egyptian_to_ipa[char]
                else:
                    result += char

            i += 1

       
        result = result.replace("  ", " ")

        return result
            
            
             