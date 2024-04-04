def rimnum_naturalnum(raqam):
    rim_raqamlar = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    natija = 0
    oldingi_qiymat = 0
    for i in raqam[::-1]:
        qiymat = rim_raqamlar[i]
        if qiymat < oldingi_qiymat:
            natija -= qiymat
        else:
            natija += qiymat
        oldingi_qiymat = qiymat
    return natija
while True:
    rim_raqam = input("Rim raqamini kiriting: ")
    natija = rimnum_naturalnum(rim_raqam)
    print("Natija:", natija)