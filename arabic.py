import sys
sys.stdout.reconfigure(encoding='utf-8')

class ArabicTranscription:
    def __init__(self):
        self.solar_letters = [
            'ت','ث','د','ذ','ر','ز','س','ش',
            'ص','ض','ط','ظ','ل','ن'
        ]

        self.arabic_to_ipa = {
            'أ': 'ʔa','إ': 'ʔi','آ': 'ʔaː',
            'ب': 'b','ت': 't','ث': 'θ','ج': 'd͡ʒ',
            'ح': 'ħ','خ': 'x','د': 'd','ذ': 'ð',
            'ر': 'r','ز': 'z','س': 's','ش': 'ʃ',
            'ص': 's̠','ض': 'dˤ','ط': 't̠','ظ': 'ð̠',
            'ع': 'ʕ','غ': 'ɣ','ف': 'f','ق': 'q',
            'ك': 'k','ل': 'l','م': 'm','ن': 'n',
            'ه': 'h','ء': 'ʔ','ئ': 'ʔ',

           
            'َ': 'a','ِ': 'i','ُ': 'u',
            'ْ': '',

            
            'ً': 'an','ٍ': 'in','ٌ': 'un'
        }

    def transcribe(self, word: str):
        result = ""
        i = 0

       
        if word.startswith("ال") and len(word) > 2:
            if word[2] in self.solar_letters:
                result += "ʔa"
            else:
                result += "ʔal"
            i = 2

        while i < len(word):
            char = word[i]

            
            if char == 'ّ':
                if result:
                    result += result[-1]
                i += 1
                continue

           
            if char == 'ا':
                result += 'aː'
                i += 1
                continue

                        
            if char == 'و':
                if i > 0:
                    if word[i-1] == 'ُ':
                        result += 'uː'      
                    elif word[i-1] == 'َ':
                        result += 'w'      
                           
              
                i += 1
                continue


           
            if char == 'ي':
                if i > 0:
                    if word[i-1] == 'ِ':
                        result += 'iː'      
                    elif word[i-1] == 'َ':
                        result += 'j'      
                       
                
                i += 1
                continue
            
            if char in self.arabic_to_ipa:
                result += self.arabic_to_ipa[char]
            else:
                result += char  

            i += 1

        return result

    def print_transcribed_words(self, words=[]):
        for i, word in words:
            print(f' /{self.transcribe(word)}/')



