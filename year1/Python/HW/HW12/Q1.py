def text(s):
    abb = {
        'be': 'b', 
        'because': 'cuz',
        'see': 'c',
        'the': 'da',
        'okay': 'ok',
        'are': 'r',
        'you': 'u',
        'without': 'w/o',
        'why': 'y',
        'see you': 'cu',
        'ate': '8',
        'great': 'gr8',
        'mate': 'm8',
        'wait': 'w8',
        'later': 'l8r',
        'tomorrow': '2mro',
        'for': '4',
        'before': 'b4',
        'once': '1ce',
        'and': '&',
        'your': 'ur',
        'you’re': 'ur',
        'as far as I know': 'afaik',
        'as soon as possible': 'ASAP',
        'at the moment': 'atm',
        'be right back': 'brb',
        'by the way': 'btw',
        'for your information': 'FYI',
        'in my humble opinion': 'imho',
        'in my opinion': 'imo',
        'laughing out loud': 'lol',
        'oh my god': 'omg',
        'rolling on the floor laughing': 'rofl',
        'talk to you later': 'ttyl'
    }
    
    words = s.split()
    
    result = []
    i = 0
    while i < len(words):
        if i + 3 <= len(words) and ' '.join(words[i:i+4]) in abb:
            result.append(abb[' '.join(words[i:i+4])])
            i += 4
        elif i + 2 <= len(words) and ' '.join(words[i:i+3]) in abb:
            result.append(abb[' '.join(words[i:i+3])])
            i += 3
        elif i + 1 <= len(words) and ' '.join(words[i:i+2]) in abb:
            result.append(abb[' '.join(words[i:i+2])])
            i += 2
        else:
            result.append(abb.get(words[i], words[i]))
            i += 1
    
    return ' '.join(result)

def rev_text(s):
    rev_abb = {
        'b': 'be', 
        'cuz': 'because',
        'c': 'see',
        'da': 'the',
        'ok': 'okay',
        'r': 'are',
        'u': 'you',
        'w/o': 'without',
        'y': 'why',
        'cu': 'see you',
        '8': 'ate',
        'gr8': 'great',
        'm8': 'mate',
        'w8': 'wait',
        'l8r': 'later',
        '2mro': 'tomorrow',
        '4': 'for',
        'b4': 'before',
        '1ce': 'once',
        '&': 'and',
        'ur': 'your',
        'afaik': 'as far as I know',
        'ASAP': 'as soon as possible',
        'atm': 'at the moment',
        'brb': 'be right back',
        'btw': 'by the way',
        'FYI': 'for your information',
        'imho': 'in my humble opinion',
        'imo': 'in my opinion',
        'lol': 'laughing out loud',
        'omg': 'oh my god',
        'rofl': 'rolling on the floor laughing',
        'ttyl': 'talk to you later'
    }
    
    words = s.split()
    result = []
    i = 0
    while i < len(words):
        if i + 3 <= len(words) and ' '.join(words[i:i+4]) in rev_abb:
            result.append(rev_abb[' '.join(words[i:i+4])])
            i += 4
        elif i + 2 <= len(words) and ' '.join(words[i:i+3]) in rev_abb:
            result.append(rev_abb[' '.join(words[i:i+3])])
            i += 3
        elif i + 1 <= len(words) and ' '.join(words[i:i+2]) in rev_abb:
            result.append(rev_abb[' '.join(words[i:i+2])])
            i += 2
        else:
            result.append(rev_abb.get(words[i], words[i]))
            i += 1
    
    return ' '.join(result)

message = 'see you tomorrow at the moment mate as soon as possible'
abb = text(message)
print(abb)
print(rev_text(abb))