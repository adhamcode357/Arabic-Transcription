import sys
sys.stdout.reconfigure(encoding='utf-8')
# File Name --> active 

from arabic import ArabicTranscription
from VerbCategory import VerbType

class ActiveParticiple:
    
    def __init__(self, arabic_trans):
        self.arabic = arabic_trans
        
        
    def classify_verb(self, word: str):
        if word.endswith(('ى','ي')):
            return VerbType.NAQIS
        
        elif len(word) >= 3 and word[1] in ['ا','و','ي']:
            return VerbType.AJWAF
        
        elif len(word) >= 3 and word[1] == word[2]:
            return VerbType.MUDAAF
        
        elif word.endswith('أ'):
            return VerbType.MAHMOUZ_AKHIR
        
        elif word.startswith('أ'):
            return VerbType.MAHMOUZ_AWWAL
        
        else:
            return VerbType.REGULAR
        
    def convert_verb_to_active(self, word):
        tashkeel = ['َ','ً','ُ','ٌ','ِ','ٍ','ْ','ّ']
    
        for t in tashkeel:
            word = word.replace(t, "")
            
        if len(word) < 3:
            return word 
        
        classify = self.classify_verb(word)
        
        first = word[0]
        sec = word[1]
        last = word[2]

        if classify == VerbType.NAQIS:
            return first + 'ا' + sec + 'ٍ'
        
        elif classify == VerbType.AJWAF:
            return first + 'ائِ' + last
        
        elif classify == VerbType.MUDAAF:
            return first + 'ا' + sec + 'ّ'
        
        elif classify == VerbType.MAHMOUZ_AKHIR:
            return first + 'ا' + sec + 'ِئ'
        
        elif classify == VerbType.MUDAAF:
            return first + 'ا' + sec + sec
        
        else:  # REGULAR
            return first + 'ا' + sec + 'ِ' + last

    
    def transcribe_word(self, word: str):
        return f'/{self.arabic.transcribe(word)}/ > /{self.arabic.transcribe(self.convert_verb_to_active(word))}/'
    


at = ArabicTranscription()
ap = ActiveParticiple(at)

#for w in words:
    #print(ap.transcribe_word(w))
    
    
