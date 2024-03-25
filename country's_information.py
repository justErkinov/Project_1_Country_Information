while True:
	a = input("Mamlakat kodini kiriting:")
	b = a.upper()
	davlatlar = {
	    "UZ": {
	        "name": "Uzbekiston",
	        "tili": "O'zbek ",
	        "poytaxt": "Toshkent",
	        "millati": "Uzbek",
	        'aholisi': '35 000 000 ga yaqin',
	        'yer maydoni': '448 978 km?  ',
	        'pul birligi': "so'm",
	        'viloyatlar': 'Toshkent Namangan Andijon Farg?ona Samarqand Buxoro Navoiy Xorazm Sirdaryo Qashqadaryo Jizzax va Qoraqalpog?iston respublikasi'
	    }}
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija['millati'])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
	    print('Viloyatlari:', natija['viloyatlar'])
	davlatlar = {
	    "KZ": {
	        "name": "Kazagistan",
	        "tili": "Kazak va rus",
	        "poytaxt": "Nur Sulton",
	        "millati": "Kazak",
	        'yer maydoni': '2 724 900 000 km? ',
	        'aholisi': '16 593 000 ga yaqin',
	        'pul birligi': 'tenge'}}
	
    
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija['millati'])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
	davlatlar = {
	    "KG": {
	        "name": "Kirgizistan",
	        "tili": "Kirgiz",
	        "poytaxt": "Bishkek",
	        "millati": "Kirgiz",
	        'yer maydoni': '198 500 km? ',
	        'aholisi': '6 389 500 ga yaqin',
	        'pul birligi': 'som'
	    }}
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija['millati'])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
	davlatlar = {
	    "RU": {
	        "name": "Russian",
	        "tili": "Rus",
	        "poytaxt": "Maskva",
	        "millati": "Rus"
	
	
	    }}
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija['millati'])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
	davlatlar = {
	    "AF": {
	        "name": "Afganistan",
	        "tili": 'dari, pushtu',
	        "poytaxt": 'TIBUL',
	        "millati": "Afgan",
	        "aholisi":"32 225 560 gayaqin",
	        'yer maydoni': "652 864 km?",
	        'pul birligi': 'afgoni'
	
	
	    }}
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija['millati'])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
	davlatlar = {
	    "TR": {
	        "name": "Turkiya",
	        "tili": "Turk",
	        "poytaxt": "Ankara",
	        "millati": "Turk",
	        "aholisi":" 80 810 525 gayaqin",
	        'yer maydoni': "783 562 km?",
	        'pul birligi': 'Turk Lirasi'
	
	
	    }}
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija["millati"])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
	davlatlar = {
	    "TKM" or "TM": {
	        "name": "Turkmaniston",
	        "tili": "Turkman",
	        "poytaxt": "Ashxabod",
	        "millati": "Turkman",
	        "aholisi":" 5 125 693 gayaqin",
	        'yer maydoni': "488 100 km?",
	        'pul birligi': 'Manat'
	
	
	    }}
	
	natija = davlatlar.get(b, False)
	if natija:
	    print('Name:', natija['name'])
	    print("Poytaxt:", natija['poytaxt'])
	    print('Tili:', natija['tili'])
	    print('Millati:', natija["millati"])
	    print('Aholisi:', natija['aholisi'])
	    print('Yer maydoni:', natija['yer maydoni'])
	    print('Pul birligi:', natija['pul birligi'])
		
    davlatlar = {
	    "USA": {
	        "name": "'United States of America",
	        "tili": "Englis tili",
	        "poytaxt": "Washington",
	        "millati": "American",
	        "aholisi":" 331 MLN gayaqin",
	        'yer maydoni': "9,833,520 KM",
	        'pul birligi': 'USD'
			
        }}