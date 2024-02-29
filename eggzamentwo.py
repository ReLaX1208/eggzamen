import re 
def let(let):
    if not re.match(r'[а-я]', let):
        return False
    return True
def rep(text, let, noun, ad, verb):
    wor = re.findall(r'\b[' + let + ']+\w*', text)
    if len(wor) < 3:
        return text
    wor = wor[:3]
    for word in wor:
        text = re.sub(r'\b' + word + r'\w*',''.join([noun, ad, verb]), text)
        return text
if __name__ == "__main__":
    text = "В лесу так хорошо, легко. Вышла ласка и начала прыгать"
    let = input("Bukva")
    noun = input("sysh")
    adj = input("pril")
    verb = input("glag")
    texte = rep(text, let, noun, adj, verb)
    print(texte)