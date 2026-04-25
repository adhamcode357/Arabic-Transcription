from enum import Enum
class VerbType(Enum):


    # فعل صحيح
    REGULAR = "regular"

    # مهموز الأول (يبدأ بهمزة)
    MAHMOUZ_AWWAL = "mahmouz_awwal"

    # مهموز الآخر (ينتهي بهمزة)
    MAHMOUZ_AKHIR = "mahmouz_akhir"

    # أجوف (الحرف الأوسط حرف علة)
    AJWAF = "ajwaf"

    # ناقص (الحرف الأخير حرف علة)
    NAQIS = "naqis"

    # مضاعف (تكرار الحرف الثاني والثالث)
    MUDAAF = "mudaaf"