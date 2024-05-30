import datetime
hari_ini = datetime.date.today()
list_merk = [] # Menampung merk sepatu yang diinput
list_tipe = [] # Menampung tipe sepatu yang diinput
list_ukuran = [] # Menampung ukuran sepatu 
list_harga = [] # Menampung harga dari setiap sepatu 
list_jumlah = [] # Menampung jumlah sepatu yang dibeli 

#list Brand dan Kategori Sepatu
list_brand = [
    'NIKE RUNNING','ADIDAS RUNNING','NEW BALANCE RUNNING','UNDER ARMOUR RUNNING',
    'NIKE BASKETBALL','ADIDAS BASKETBALL','NEW BALANCE BASKETBALL','UNDER ARMOUR BASKETBALL',
    'NIKE FUTSAL','ADIDAS FUTSAL','NEW BALANCE FUTSAL', 'UNDER ARMOUR FUTSAL',
    'NIKE FOOTBALL','ADIDAS FOOTBALL','NEW BALANCE FOOTBALL','UNDER ARMOUR FOOTBALL']

#Dictionary Untuk Sepatu Running
NikeRunning = {
    'AIR SUPERREP': 1799000, 
    'AIR MAX 90 G': 1979000, 
    'AIR ZOOM PEGASUS 39': 1219000,
    'AIR ZOOM ALPHAFLY NEXT%': 2999000,
    'AIR ZOOM ARCADIA 2': 979000
}

AdidasRunning = {
    'DURAMO SL 2.0': 900000,
    'ULTRABOOST 22': 3300000,
    'ADIZERO SL': 2000000,
    'DURAMO 10 WHITE': 900000,
    'PUREBOOST': 2100000
}

NBRunning = {
    'NEW BALANCE 410V7' : 889000,
    'NEW BALANCE 411 V2' : 669000,
    'NEW BALANCE FRESH FOAM ARISHI V4' : 999000,
    'NEW BALANCE DYNASOFT NITREL V4' : 1199000,
    'NEW BALANCE FUELCELL PROPEL V3' : 1599000
}

UARunning = {
    'UA CHARGED ESCAPE 3 EVO' : 1549000,
    'UA CHARGED BANDIT 6' : 1309000,
    'UA HOVR PHANTOM 2 CLR SFT' : 2599000,
    'UA SURGE 3' : 769000,
    'UA CHARGED PURSUIT' : 1000000 
}

# Dictionary Untuk Sepatu Basket
NikeBasketball = {
    'KYRIE INFINITY EP' : 1979000,
    'LEBRON 19 LOW EP' : 2849000,
    'KD15 EP' : 2489000,
    'ZION 2 PF' : 1869000,
    'GIANNIS IMMORTALITY 2' : 799000
}

AdidasBasketball = {
    'CENTENNIAL 85 HI' : 2200000,
    'HARDEN VOL 6' : 2300000,
    'HARDEN STEPBACK 3' : 1400000,
    'DAME 8' : 2000000,
    'FORUM MID' : 1800000
}

NBBasketball = {
    'KAWHI 2 BLUR "PALMISTRY" WHITE BLACK"' : 2999000,
    'KAHWI 2 GOOSEBUMPS' : 2799000,
    'KAWHI II NEW MONEY' : 3360000,
    'KAWHI BAITED BLACK' : 4130000,
    'BLACK GUM BASKETBALL' : 999000
}

UABasketball = {
    'UA CURRY 1' : 2659000,
    'UA LOCKDOWN 4' : 890000,
    'UA CURRY HOVR SPLASH' : 1899000,
    'UA HOVR HAVOC MEN' : 2299000,
    'UA CURRY LOW' : 650000
}

# Dictionary Untuk Sepatu Futsal 
NikeFutsal = {
    'ZOOM MERCURIAL VAPOR 15':1280000,
    'ZOOM MERCURIAL PRO SUPERFLY 9':1450000,
    'PHANTOM GT 2':1280000,
    'VAPOR 14 ACADEMY':734000,
    'SUPERFLY 8':1350000}

AdidasFutsal = {
    'PREDATOR EDGE 3':1400000,
    'PREDATOR EDGE 4':850000,
    'COPA SENSE 3':1000000,
    'COPA SENSE 4':700000,
    'PREDATOR FREAK':1300000}

NBFutsal = {
    'AUDAZO V5+ PRO':1600000,
    'MSVRCIBO BOOTS':1100000,
    'AUDAZO V5+ PRO SUEDE':2600000,
    'FURON TF NB':2700000,
    'FURON V7 DISPATCH':1250000}
 
UAFutsal = {
    'CLUTCHFIT FORCE 2.0 TR':770000,
    'SPEEDFORM CRM LEATHER FG':2500000}

# Dictionary Untuk Sepatu Football
NikeFootball = {
    'MERCURIAL VAPOR 14 ELITE': 1400000,
    'TIEMPO LEGEND 9 ELITE': 4500000,
    'KING OF DRIBBLE': 1000000,
    'MERCURIAL SUPERFLY 7 ELITE': 1000000}

AdidasFootball = {
    'X SPEEDPORTAL 3': 1400000,
    'PREDATOR EDGE 1FG': 3500000,
    'COPA SENSE 1FG': 2800000,
    'XSPEEDFLOW 1FG': 2300000,
    'PREDATOR EGDE 1 LOW': 2300000}
 

NBFootball = {
    'FURON V7 DESTROY': 1800000,
    'FURON 6+ SOD ': 4200000,
    'PRO FG ORIGINAL ': 3400000,
    'TAKELA V1 PRO': 2200000}

UAFootball = {
    'CLONE MAGNETICO FG': 1400000,
    'FB TEAM MAGNETICO': 2100000,
    'SPOTLIGHT FG HIGH':2300000,
    'CLONE MAGNETICO PRO FG':450000,
    'MAGNETICO CONTROL':1500000}


# list Sepatu Running
NikeRunning_ = ['AIR SUPERREP','AIR MAX 90 G','AIR ZOOM PEGASUS 39','AIR ZOOM ALPHAFLY NEXT%','AIR ZOOM ARCADIA 2']
AdidasRunning_ = ['DURAMO SL 2.0','ULTRABOOST 22','ADIZERO SL','DURAMO 10 WHITE','PUREBOOST']
NBRunning_ = ['NEW BALANCE 410V7','NEW BALANCE 411 V2','NEW BALANCE FRESH FOAM ARISHI V4','NEW BALANCE DYNASOFT NITREL V4','NEW BALANCE FUELCELL PROPEL V3']
UARunning_ = ['UA CHARGED ESCAPE 3 EVO','UA CHARGED BANDIT 6','UA HOVR PHANTOM 2 CLR SFT','UA SURGE 3','UA CHARGED PURSUIT']

# list Sepatu Basketball
NikeBasketball_ = ['KYRIE INFINITY EP','LEBRON 19 LOW EP','KD15 EP','ZION 2 PF','GIANNIS IMMORTALITY 2']
AdidasBasketball_ = ['CENTENNIAL 85 HI','HARDEN VOL 6','HARDEN STEPBACK 3','DAME 8','FORUM MID']
NBBasketball_ = ['KAWHI 2 BLUR "PALMISTRY" WHITE BLACK','KAWHI 2 GOOSEBUMPS','KAWHI II MONEY','KAWHI BAITED BLACK','BLACK GUM BASKETBALL']
UABasketball_ = ['UA CURRY 1','UA LOCKDOWN 4','UA CURRY HOOVR SPLASH','UA HOVR HAVOC MEN','UA CURRY LOW']

# list Sepatu Futsal
NikeFutsal_ = ['ZOOM MERCURIAL VAPOR 15','ZOOM MERCURIAL PRO SUPERFLY 9','PHANTOM GT 2','VAPOR 14 ACADEMY','SUPERFLY 8']
AdidasFutsal_ = ['PREDATOR EDGE 3','PREDATOR EDGE 4','COPA SENSE 3','COPA SENSE 4','PREDATOR FREAK']
NBFutsal_ = ['AUDAZO V5+ PRO','MVSCRIBO BOOTS','AUDAZO V5+ PRO SUEDE','FURON TF NB']
UAFutsal_ = ['CLUTCHFIT FORCE 2.0 TR', 'SPEEDFORM CRM LEATHER FG']

# list Sepatu Football
NikeFootball_ = ['MERCURIAL VAPOR 14 ELITE','PHANTOM GT2','TIEMPO LEGEND 9 ELITE','KING OF DRIBBLE','MERCURIAL SUPERFLY 7 ELITE']
AdidasFootball_ = ['X SPEEDPORTAL.3','PREDATOR EDGE 1FG','COPA SENSE 1FG','XSPEEDFLOW 1FG','PREDATOR EGDE 1 LOW']
NBFootball_ = ['FURON V7 DESTROY','FURON 6+ SOD','PRO FG ORIGINAL','TAKELA V1 PRO']
UAFootball_ = ['CLONE MAGNETICO FG','FB TEAM MAGNETICO','SPOTLIGHT FG HIGH','CLONE MAGNETICO PRO FG']

# Dictionary Ukuran Sepatu Running
Nike_Running = {
    'AIR SUPERREP': [38,39,40,41,42,43], 
    'AIR MAX 90 G': [39,40,42,44,45,46], 
    'Air ZOOM PEGASUS 39': [38,39,40,42,43,45],
    'AIR ZOOM ALPHAFLY NEXT%': [38,39,40,41,42,45],
    'AIR ZOOM ARCADIA 2': [38,40,41,42,44,46]}   
Adidas_Running = {
    'DURAMO SL 2.0' : [38,39,40,42,43,44,46],
    'ULTRABOOST 22' : [39,40,41,43,44,45,46],
    'ADIZERO SL' : [40,41,42,42.5,43,44],
    'DURAMO 10 WHITE' : [40,40.5,41,42,43,44,45],
    'PUREBOOST' : [40,41,41.5,42,43,44,44.5]}
NB_Running = {
    'NEW BALANCE 410V7' : [38,39,40,41,42,43],
    'NEW BALANCE 411 V2' : [39,40,41,43,44,45,46],
    'NEW BALANCE FRESH FOAM ARISHI V4' : [40.5,41,42,42.5,44,45],
    'NEW BALANCE DYNASOFT NITREL V4' : [40,41,42,42.5,43,44],
    'NEW BALANCE FUELCELL PROPEL V3' : [40,41,42,42.5,43,44]}
UA_Running = {
    'UA CHARGED ESCAPE 3 EVO' : [42,43,43.5,45,46,47],
    'UA CHARGED BANDIT 6' : [39,40,41,43,44,45,46],
    'UA HOVR PHANTOM 2 CLR SFT' : [39,40,41,43,44,45,46],
    'UA SURGE 3' : [40.5,41,42,42.5,44,45],
    'UA CHARGED PURSUIT' : [40.5,41,42,43,44,44.5,45]}

# Dictionary Ukuran Sepatu Basketball
Nike_Basketball = {
    'KYRIE INFINTY EP' : [40,41,42,43,44,45,45.5],
    'LEBRON 19 LOW EP' : [42,43,44,45,46,47,48],
    'KD15 EP' : [41,42,43,44,44.5,46,47],
    'ZION 2 PF' : [41.5,42,43,44,45,47],
    'GIANNIS IMMORTALITY 2' : [40,41,42,42.5,43,44,45]}
Adidas_Basketball = {
    'CENTENNIAL 85 HI' : [39,40,41,43,44,45,46],
    'HARDEN VOL 6' : [42,43,44,45,46,47,48],
    'HARDEN STEPBACK 3' : [41.5,42,43,44,45,47],
    'DAME 8' : [41,42,43,44,44.5,46,47],
    'FORUM MID' : [38,39,40,41,42,45]}
NB_Basketball = {
    'KAWHI 2 BLUR "PALMISTRY" WHITE BLACK' : [41,42,43,44,45,45.5],
    'KAWHI 2 GOOSEBUMPS' : [40,41,41.5,42,43,44,45],
    'KAWHI II NEW MONEY' : [42,43,44,45,46,47,48],
    'KAWHI BAITED BLACK' : [41,42,43,44,44.5,45],
    'BLACK GUM BASKETBALL' : [40,41,42,42.5,43,44]}
UA_Basketball = {
    'UA CURRY 1' : [40,41,42,42.5,43,44],
    'UA LOCKDOWN 4' : [40.5,41,42,42.5,44,45],
    'UA CURRY HOVR SPLASH' : [41,42,43,44,44.5,46,47],
    "UA HOVR HAVOC MEN" : [41.5,42,43,44,45,47],
    'UA CURRY LOW' : [40,41,42,42.5,43,44]}

# Dictionary Ukuran Sepatu Futsal
Nike_Futsal = {
    'ZOOM MERCURIAL VAPOR 15' : [38,39,40,41,42,43,44,45],
    'ZOOM MERCURIAL PRO SUOERFLY 9' : [38,39,40,41,42,45],
    'PHANTOM GT 2' : [40.5,41,42,42.5,44,45],
    'VAPOR 14 ACADEMY' : [41,42,43,44,44.5,46,47],
    'SUPERFLY 8' : [39,40,41,43,44,45,46]}
Adidas_Futsal = {
    'PREDATOR EDGE 3' : [41,42,43,44,44.5,46,47],
    'PREDATOR EDGE 4' : [40.5,41,42,42.5,44,45],
    'COPA SENSE 3' : [38,39,40,41,42,45],
    'COPA SENSE 4' : [41,42,43,44,44.5,46,47],
    'PREDATOR FREAK' : [40,41,42,42.5,43,44]}
NB_Futsal = {
    'AUDAZO V5+ PRO' : [38,39,40,41,42,45],
    'MVSCRIBO BOOTS' : [40,41,42,42.5,43,44],
    'AUDAZO V5+ PRO SUEDE' : [40,41,41.5,42,43,44,45],
    'FURON TF NB' : [40,41,42,42.5,43,44,45],
    'FURON V7 DISPATCH' : [38,39,40,41,42,45]}
UA_Futsal = {
    'CLUTCHFIT FORCE 2.0 TR': [40,41,41.5,42,43,44,45],
    'SPEEDFORM CRM LEATHER FG': [40.5,41,42,42.5,44,45]}

# Dictionary Ukuran Sepatu Football
Nike_Football = {
    'MERCURIAL VAPOR 14 ELITE' : [40.5,41,42,42.5,44,45],
    'PHANTOM GT2' : [39,39.5,40,42,43,44],
    'TIEMPO LEGEND 9 ELITE' : [40.5,41,42,42.5,44,45],
    'KING OF DRIBBLE' : [41,42,43,44,44.5,46,47],
    'MERCURIAL SUPERFLY 7 ELITE' : [41,42,43,44,44.5,46,47]}
Adidas_Football = {
    'X SPEEDPORTAL.3' : [40,41,41.5,42,43,44,45],
    'PREDATOR EDGE 1FG' : [40,41,42,43,44,45,47],
    'COPA SENSE 1FG' : [42,43,44,45,46,47,48],
    'X SPEEDFLOW.1 FG' : [41,42,43,44,44.5,46,47],
    'PREDATOR EGDE 1 LOW' : [39,39.5,41,42,43,44]}
NB_Football = {
    'FURON V7 DESTROY' : [40.5,41,42,42.5,44,45],
    'FURON 6+ SOD' : [41,42,43,44.5,45],
    'PRO FG ORIGINAL' : [40,41,42,43,44,45,47],
    'TAKELA V1 PRO' : [39,40,41,43,44,45,46]}
UA_Football = {
    'CLONE MAGNETICO FG' : [41,42,43,44,44.5,46,47],
    'FB TEAM MAGNETICO' : [40,41,42,42.5,43,44],
    'SPOTLIGHT FG HIGH' : [41,42,43,44,44.5,46,47],
    'CLONE MAGNETICO PRO FG' : [42,43,44,45,46,47,48],
    'MAGNETICO CONTROL' : [40.5,41,42,42.5,44,45]}

# Fungsi Untuk Menampilkan Menu Utama
def menu():
    while True:
        print('''
Pilih Menu :
1. Daftar Produk
2. Search Produk
3. Order
4. Exit
''')
        P_menu = int(input("==> "))

        if P_menu == 1:
            daftar_produk()
            lanjutan = int(input('\nPilih Menu:\n1. Menu Awal\n2. Search Produk\n3. Pesan\n\n==> '))
            if lanjutan == 1:
                menu()
            elif lanjutan == 2:
                cari_sepatu()
                lanjut_order = int(input('\nPilih Menu:\n1. Menu Awal\n2. Pesan\n\n==> '))
                if lanjut_order == 1:
                    menu()
                elif lanjut_order == 2:
                    ulang = 0
                    while ulang == 0:
                        try:
                            order()
                            ulang = 1
                            bill()

                        except KeyError:
                            stop = int(input('Apakah anda ingin mengisi ulang?\n1. Ya\n2. Tidak\n\n==> '))
                            if stop == 2:
                                ulang = 1
                                menu()

            elif lanjutan == 3:
                ulang = 0
                while ulang == 0:
                    try:
                        order()
                        ulang = 1
                        bill()

                    except KeyError:
                        stop = int(input('Apakah anda ingin mengisi ulang?\n1. Ya\n2. Tidak\n\n==> '))
                        if stop == 2:
                            ulang = 1
                            menu()    
        
        if P_menu == 2:
            cari_sepatu()
            lanjut_order = int(input('\nPilih Menu:\n1. Menu Awal\n2. Pesan\n\n==> '))
            if lanjut_order == 1:
                menu()
            elif lanjut_order == 2:
                ulang = 0
                while ulang == 0:
                    try:
                        order()
                        ulang = 1
                        bill()

                    except KeyError:
                        stop = int(input('Apakah anda ingin mengisi ulang?\n1. Ya\n2. Tidak\n\n==> '))
                        if stop == 2:
                            ulang = 1
                            menu()



        if P_menu == 3:
            ulang = 0
            while ulang == 0:
                try:
                    order()
                    ulang = 1
                    bill()

                except KeyError:
                    stop = int(input('Apakah anda ingin mengisi ulang?\n1. Ya\n2. Tidak\n\n==> '))
                    if stop == 2:
                        menu()
                        break
        if P_menu == 4:
            print('='*40)
            print('='*13,'Terima Kasih','='*13)
            print('='*40)
            break
        break
                
# Fungsi Untuk Menampilkan Daftar Kategori Produk
def daftar_produk():
    print('''
Pilih Kategori :
1. Running
2. Basketball
3. Futsal
4. Football''')
    p_kategori = int(input("==> "))

    if p_kategori == 1:
        print("-"*49)
        print("\t\tProduk\t\t\t| Harga |")
        print("-"*49)
        print("="*13," Nike Running Shoes ","="*14)
        for i in NikeRunning:
            if len(i) < 15:
                print(i, "\t\t\t\t:", NikeRunning[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NikeRunning[i])
            elif len(i) > 20:
                print(i, "\t\t:", NikeRunning[i])
        print()
        print("="*12," Adidas Running Shoes ","="*13)
        for i in AdidasRunning:
            if len(i) < 15:
                print(i, "\t\t\t\t:", AdidasRunning[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", AdidasRunning[i])
            elif len(i) > 20:
                print(i, "\t\t:", AdidasRunning[i])
        print()
        print("="*13," New Balance Running ","="*13)
        for i in NBRunning:
            if len(i) < 20:
                print(i, "\t\t\t:", NBRunning[i])
            elif len(i) > 20 and len(i) <= 30:
                print(i, "\t\t:", NBRunning[i])
            elif len(i) > 30:
                print(i, "\t:", NBRunning[i])
        print()
        print("="*13," Under Armour Running ","="*12)
        for i in UARunning:
            if len(i) < 15:
                print(i, "\t\t\t\t:", UARunning[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", UARunning[i])
            elif len(i) == 20:
                print(i, "\t\t\t:", UARunning[i])
            elif len(i) <= 25:
                print(i, "\t\t:", UARunning[i])

        
    elif p_kategori == 2:
        print("-"*49)
        print("\t\tProduk\t\t\t| Harga |")
        print("-"*49)
        print("="*13,"Nike Basketball Shoes","="*13)
        for i in NikeBasketball:
            if len(i) < 15:
                print(i, "\t\t\t\t:", NikeBasketball[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NikeBasketball[i])
            elif len(i) > 20:
                print(i, "\t\t\t:", NikeBasketball[i])
        print()
        print("="*12,"Adidas Basketball Shoes","="*12)
        for i in AdidasBasketball:
            if len(i) < 9:
                print(i, "\t\t\t\t\t:", AdidasBasketball[i])
            elif len(i) >= 9 and len(i) <15:
                print(i, "\t\t\t\t:", AdidasBasketball[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", AdidasBasketball[i])
            elif len(i) > 20:
                print(i, "\t\t\t:", AdidasBasketball[i])
        print()
        print("="*12,"New Balance Basketball","="*13)
        for i in NBBasketball:
            if len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NBBasketball[i])
            elif len(i) == 20:
                print(i, "\t\t\t:", NBBasketball[i])
            elif len(i) >= 24:
                print(i, "\t\t:", NBBasketball[i])
        print()
        print("="*12,"Under Armour Basketball","="*12)
        for i in UABasketball:
            if len(i) < 15:
                print(i, "\t\t\t\t:", UABasketball[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", UABasketball[i])
            elif len(i) >= 20:
                print(i, "\t\t\t:", UABasketball[i])
            


    elif p_kategori == 3:
        print('='*49)
        print("\t\tProduk\t\t\t| Harga |")
        print("-"*49)
        print('='*14," Nike Futsal Shoes ",'='*14)
        for i in NikeFutsal:
            if len(i) < 15:
                print(i, "\t\t\t\t:", NikeFutsal[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NikeFutsal[i])
            elif len(i) > 20:
                print(i, "\t\t:", NikeFutsal[i])
        print()
        print('='*13," Adidas Futsal Shoes ",'='*13)
        for i in AdidasFutsal:
            if len(i) < 15:
                print(i, "\t\t\t\t:", AdidasFutsal[i])
            elif len(i) >= 15 and len(i) < 20:
                print(i, "\t\t\t:", AdidasFutsal[i])
            elif len(i) > 20:
                print(i, "\t\t\t:", AdidasFutsal[i])
        print()
        print('='*14," New Balance Futsal ",'='*13)
        for i in NBFutsal:
            if len(i) < 15:
                print(i, "\t\t\t\t:", NBFutsal[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NBFutsal[i])
            elif len(i) >= 20:
                print(i, "\t\t\t:", NBFutsal[i])
        print()
        print("UA Futsal")
        for i in UAFutsal:
            if len(i) > 20 and len(i) < 24:
                print(i, "\t\t\t:", UAFutsal[i])
            elif len(i) >= 24:
                print(i, '\t\t:', UAFutsal[i])

    elif p_kategori == 4:
        print("-"*49)
        print("\t\tProduk\t\t\t| Harga |")
        print("-"*49)
        print('='*13,' Nike Football Shoes ','='*13)
        for i in NikeFootball:
            if len(i) < 15:
                print(i, "\t\t\t\t:", NikeFootball[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NikeFootball[i])
            elif len(i) >= 26:
                print(i, "\t\t:", NikeFootball[i])
        print()
        print('='*12," Adidas Football Shoes ",'='*12)
        for i in AdidasFootball:
            if len(i) < 15:
                print(i, "\t\t\t\t:", AdidasFootball[i])
            elif len(i) >= 15 and len(i) < 20:
                print(i, "\t\t\t:", AdidasFootball[i])
            elif len(i) > 20:
                print(i, "\t\t\t:", AdidasFootball[i])
        print()
        print('='*9,' New Balance Football Shoes ','='*8)
        for i in NBFootball:
            if len(i) < 15:
                print(i, "\t\t\t\t:", NBFootball[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", NBFootball[i])
            elif len(i) > 20:
                print(i, "\t\t\t:", NBFootball[i])
        print()
        print('='*12," Under Armour Football ",'='*12)
        for i in UAFootball:
            if len(i) < 15:
                print(i, "\t\t\t\t:", UAFootball[i])
            elif len(i) > 15 and len(i) < 20:
                print(i, "\t\t\t:", UAFootball[i])
            elif len(i) > 20:
                print(i, "\t\t\t:", UAFootball[i])

# Fungsi Untuk Melakukan Pemesanan
# Total Harga di set di 0 agar bertambah terus menerus nantinya
Total_harga = 0
def order():
    global Nama, Total_harga
    lanjut = 1
    print("Mohon Jangan Gunakan Spasi Setelah Input Karakter")
    Nama = input("Nama\t\t: ")
    Nama = Nama.upper()
    while lanjut == 1:
        Merk = input("Merk\t\t: ")
        Merk = Merk.upper()
        Kategori = input("Kategori\t: ")
        Kategori = Kategori.upper()
        Tipe = input("Tipe\t\t: ")
        Tipe = Tipe.upper()
        M_Kategori = Merk+' '+Kategori
        harga = 0
        if M_Kategori == 'NIKE RUNNING':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Nike_Running[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Nike_Running[Tipe])
                Tipe = ''
            harga += NikeRunning[Tipe]
        elif M_Kategori == 'ADIDAS RUNNING':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Adidas_Running[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Adidas_Running[Tipe])
                Tipe = ''
            harga += AdidasRunning[Tipe]
        elif M_Kategori == 'NB RUNNING' or M_Kategori == 'NEW BALANCE RUNNING':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in NB_Running[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', NB_Running[Tipe])
                Tipe = ''
            harga += NBRunning[Tipe]
        elif M_Kategori == 'UA RUNNING' or M_Kategori == 'UNDER ARMOUR RUNNING':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in UA_Running[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', UA_Running[Tipe])
                Tipe = ''
            harga += UARunning[Tipe]
        elif M_Kategori == 'NIKE BASKETBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Nike_Basketball[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Nike_Basketball[Tipe])
                Tipe = ''
            harga += NikeBasketball[Tipe]
        elif M_Kategori == 'ADIDAS BASKETBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Adidas_Basketball[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Adidas_Basketball[Tipe])
                Tipe = ''
            harga += AdidasBasketball[Tipe]
        elif M_Kategori == 'NB BASKETBALL' or M_Kategori == 'NEW BALANCE BASKETBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in NB_Basketball[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', NB_Basketball[Tipe])
                Tipe = ''
            harga += NBBasketball[Tipe]
        elif M_Kategori == 'UA BASKETBALL' or M_Kategori == 'UNDER ARMOUR BASKETBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in UA_Basketball[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', UA_Basketball[Tipe])
                Tipe = ''
            harga += UABasketball[Tipe]
        elif M_Kategori == 'ADIDAS FUTSAL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Adidas_Futsal[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Adidas_Futsal[Tipe])
                Tipe = ''
            harga += AdidasFutsal[Tipe]
        elif M_Kategori == 'NIKE FUTSAL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Nike_Futsal[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Nike_Futsal[Tipe])
                Tipe = ''
            harga += NikeFutsal[Tipe]
        elif M_Kategori == 'NEW BALANCE FUTSAL' or M_Kategori == 'NB FUTSAL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in NB_Futsal[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', NB_Futsal[Tipe])
                Tipe = ''
            harga += NBFutsal[Tipe]
        elif M_Kategori == 'UNDER ARMOUR FUTSAL' or M_Kategori == 'UA FUTSAL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in UA_Futsal[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', UA_Futsal[Tipe])
                Tipe = ''
            harga += UAFutsal[Tipe]
        elif M_Kategori == 'NIKE FOOTBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Nike_Football[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Nike_Football[Tipe])
                Tipe = ''
            harga += NikeFootball[Tipe]
        elif M_Kategori == 'ADIDAS FOOTBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in Adidas_Football[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', Adidas_Football[Tipe])
                Tipe = ''
            harga += AdidasFootball[Tipe]
        elif M_Kategori == 'NEW BALANCE FOOTBALL' or M_Kategori == 'NB FOOTBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in NB_Football[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', NB_Football[Tipe])
                Tipe = ''
            harga += NBFootball[Tipe]
        elif M_Kategori == 'UNDER ARMOUR FOOTBALL' or M_Kategori == 'UA FOOTBALL':
            print("Jika Ukuran Di atas 44 Harga Bertambah 100.000")
            Ukuran = float(input("Ukuran\t\t: "))
            if Ukuran not in UA_Football[Tipe]:
                print('Ukuran Tidak Tersedia')
                print('Ukuran Yang Tersedia', UA_Football[Tipe])
                Tipe = ''
            harga += UAFootball[Tipe]
        else:
            print('Merk atau Tipe Tidak Ada Dalam Daftar Produk')
            UAFootball[Tipe]
        if Ukuran > 44:
            harga += 100000
        Jumlah = int(input("Jumlah\t\t: "))
        T_harga = harga * Jumlah
        Total_harga += T_harga
        print(f"Total Harga\t: {Total_harga}")
        list_merk.append(Merk)
        list_tipe.append(Tipe)
        list_ukuran.append(Ukuran)
        list_harga.append(harga)
        list_jumlah.append(Jumlah)
        lanjut = int(input('''
Apakah anda ingin menambah pesanan
1. Ya
2. Tidak

==> '''))

# Binary Search
def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
            pos += 1
        else:
            pos = pos + 1
    
    return pos

# Fungsi Untuk Mencari Sepatu 
def cari_sepatu():
    M = input('Masukkan Merk Yand Dicari : ')
    M = M.upper()
    if M == 'NB':
        M = 'NEW BALANCE'
    elif M == 'UA':
        M = 'UNDER ARMOUR'
    K = input('Masukkan Kategori Yand Dicari : ')
    K = K.upper()
    t = M+' '+K
    if t in list_brand:
        y = input('Masukkan Tipe Yand Dicari : ')
        y = y.upper()

        if t == 'NIKE RUNNING':
            if y in NikeRunning_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NikeRunning_, y)}
Ukuran yang tersedia {Nike_Running[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'ADIDAS RUNNING':
            if y in AdidasRunning_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(AdidasRunning_, y)}
Ukuran yang tersedia {Adidas_Running[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NB RUNNING' or t == 'NEW BALANCE RUNNING':
            if y in NBRunning_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NBRunning_, y)}
Ukuran yang tersedia {NB_Running[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'UA RUNNING' or t == 'UNDER ARMOUR RUNNING':
            if y in UARunning_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(UARunning_, y)}
Ukuran yang tersedia {UA_Running[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NIKE BASKETBALL':
            if y in NikeBasketball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NikeBasketball_, y)}
Ukuran yang tersedia {Nike_Basketball[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'ADIDAS BASKETBALL':
            if y in AdidasBasketball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(AdidasBasketball_, y)}
Ukuran yang tersedia {Adidas_Basketball[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NB BASKETBALL' or t == 'NEW BALANCE BASKETBALL':
            if y in NBBasketball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NBBasketball_, y)}
Ukuran yang tersedia {NB_Basketball[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'UA BASKETBALL' or t == 'UNDER ARMOUR BASKETBALL':
            if y in UABasketball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(UABasketball_, y)}
Ukuran yang tersedia {UA_Basketball[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NIKE FUTSAL':
            if y in NikeFutsal_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NikeFutsal_, y)}
Ukuran yang tersedia {Nike_Futsal[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'ADIDAS FUTSAL':
            if y in AdidasFutsal_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(AdidasFutsal_, y)}
Ukuran yang tersedia {Adidas_Futsal[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NB FUTSAL' or t == 'NEW BALANCE FUTSAL':
            if y in NBFutsal_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NBFutsal_, y)}
Ukuran yang tersedia {NB_Futsal[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'UA FUTSAL' or t == 'UNDER ARMOUR FUTSAL':
            if y in UAFutsal_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(UAFutsal_, y)}
Ukuran yang tersedia {UA_Futsal[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NIKE FOOTBALL':
            if y in NikeFootball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NikeFootball_, y)}
Ukuran yang tersedia {Nike_Football[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'ADIDAS FOOTBALL':
            if y in AdidasFootball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(AdidasFootball_, y)}
Ukuran yang tersedia {Adidas_Football[y]}''')
            else:
                print('Tipe Tidak Tersedia')

        if t == 'NB FOOTBALL' or t == 'NEW BALANCE FOOTBALL':
            if y in NBFootball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(NBFootball_, y)}
Ukuran yang tersedia {NB_Football[y]}''')
            else:
                print('Tipe Tidak Tersedia')
                
        if t == 'UA FOOTBALL' or t == 'UNDER ARMOUR FOOTBALL':
            if y in UAFootball_:
                print(f'''Sepatu berada di rak {Sequential_Search(list_brand, t)} pada slot {Sequential_Search(UAFootball_, y)}
Ukuran yang tersedia {UA_Football[y]}''')
            else:
                print('Tipe Tidak Tersedia')

    else:
        print('Merk Tidak Tersedia')

# Fungsi Untuk Mencetak Bill Atau Bukti Pembayaran
def bill():
    print('='*40)
    print(f'''Nama\t\t\t: {Nama}
                        ''')
    for i in range (len(list_merk)) : 
        print(f'''
Merk\t\t\t: {list_merk[i]}
Tanggal Transaksi\t: {hari_ini}
Tipe\t\t\t: {list_tipe[i]}
Ukuran\t\t\t: {list_ukuran[i]}
Harga\t\t\t: {list_harga[i]}
Jumlah\t\t\t: {list_jumlah[i]}
        ''')
    print(f"Total Harga\t\t: {Total_harga}")
    print('='*40)
    print('='*13,'Terima Kasih','='*13)
    print('='*40)

print("Selamat datang di Toko Sepatu Olesport")

menu()

'''
Kelompok 1 :
1. Abdul Hakim Darassalam 2210512047
2. Abdullah Canggalung 2210512054
3. Ahmad Ro'in Fannani 2210512064
4. Benedicto Geraldo Doa Dawa 2210512081
5. Giann Nagara Sinaga 2210512082
'''