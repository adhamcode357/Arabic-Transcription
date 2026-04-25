import sys
from arabic import ArabicTranscription as AT
sys.stdout.reconfigure(encoding='utf-8')
# File Name --> morphological
class Morphological:
    def __init__(self, ara_trans):
        self.prefix = ["لل","ال","و","ل"]
        self.suffix = ["هن","هم","ون","ها","ك","ي"]
        self.transcribe = ara_trans
        
    def return_prefix(self, word: str): 
        if (word.startswith('لل')):
            return 'لل'
        for p in self.prefix:
            if word.startswith(p):
                return p
        return ""

    def return_suffix(self, word: str):
        for s in self.suffix:
            if word.endswith(s):
                return s
        return ""
    
    def stem(self, word: str):
        p = self.return_prefix(word) 
        s = self.return_suffix(word)
        
        stem = word[len(p): len(word) - len(s)]
        
        if stem.endswith('ت'):
            stem = stem[:-1] + 'ة'
        if stem.endswith('ئ'):
            stem = stem[:-1] + 'ء'
        
        return stem 
                
    def transcribe_morph(self, word: str):
        p = self.return_prefix(word)
        s = self.return_suffix(word)
        w = self.stem(word)

        p_tr = self.transcribe.transcribe(p) if p else ""
        w_tr = self.transcribe.transcribe(w) if w else ""
        s_tr = self.transcribe.transcribe(s) if s else ""

        return (
            f"📌 Word: {word}\n"
            f" ──> \n"
            f"🔹 Prefix : {p} → /{p_tr}/\n"
            f"🔹 Stem   : {w} → /{w_tr}/\n"
            f"🔹 Suffix : {s} → /{s_tr}/"
        )



at = AT()        
m = Morphological(at) 

words = [  
    "الكتاب",
    "نسائهن",
    "للطلاب",
    "كتابهم",
    "مدرستي",
    "قلمك",
    "معلمون"
]             

for word in words:
    print(m.transcribe_morph(word))