class Personal:
    def __init__(self,nama,sex="L"):
        self.ayah = None
        self.ibu = None
        self.sex = sex
        self.nama = nama
        self.anak = []      # list dari objek anak/personal
        self.istri = []     # list dari objek istri/personal
        self.suami = []     # list dari objek suami/personal
        self.saudara = []   # list dari objek saudara/personal
        self.saudaraKandung = [] # list dari objek saudara kandung personal
        self.saudaraTiri = [] # list dari objek saudara tiri personal
        self.saudaraSepupu = [] # list dari objek saudara sepupu personal
        
        
    #===== INGET CEK NAMA PANGGILANNYA :)))
    
    
    def setAyah(self,ayah): # ayah = objeck dari personal
        self.ayah = ayah
        
        self.in_anak = 0
        for anak in ayah.anak:
            if (anak==self):
                self.in_anak = 1
                
        if (self.in_anak == 0):
            ayah.setAnak(self)
        
    def setIbu(self,ibu):
        self.ibu = ibu
        
        self.in_anak = 0
        for anak in ibu.anak:
            if (anak==self):
                self.in_anak = 1
                
        if (self.in_anak == 0):
            ibu.setAnak(self)
    
    def setIstri(self,istri):
        if (self.sex=="L"):
            self.istri.append(istri)
            
            self.in_suami = 0
            for suami in istri.suami:
                if (self == suami):
                    self.in_suami = 1
            if (self.in_suami == 0):
                istri.setSuami(self)
        
        
    def setSuami(self,suami):
        if (self.sex=="P"):
            self.suami.append(suami)

            self.in_istri = 0
            for istri in suami.istri:
                if (self == istri):
                    self.in_istri = 1
            if (self.in_istri == 0):
                suami.setIstri(self)

        
    def setAnak(self,anak):
        self.anak.append(anak)
        if (self.sex == "L"):
            if(anak.ayah != self):
                anak.setAyah(self)
        else:
            if(anak.ibu != self):
                anak.setIbu(self)
        
    def setSaudaraKandung(self, sdr):
        if self.ibu.nama == sdr.ibu.nama and self.ayah.nama == sdr.ayah.nama:
            self.saudaraKandung.append(sdr)
            
            self.in_saudarak = 0
            for saudara in sdr.saudaraKandung:
                if (self == saudara):
                    self.in_saudarak = 1
            if (self.in_saudarak == 0):
                sdr.setSaudaraKandung(self)
    
    def setSaudaraTiri(self, sdr):
        if self.ibu.nama != sdr.ibu.nama or self.ayah.nama != sdr.ayah.nama:
            self.saudaraTiri.append(sdr)
            
            self.in_saudarat = 0
            for saudara in sdr.saudaraTiri:
                if (self == saudara):
                    self.in_saudarat = 1
            if (self.in_saudarat == 0):
                sdr.setSaudaraTiri(self)

    def setSaudaraSepupu(self, sdr):
        check = self.ibu
        check2 = self.ayah
        if check in sdr.ibu.saudaraKandung or check in sdr.ayah.saudaraKandung:
            self.saudaraSepupu.append(sdr)
            
        elif check2 in sdr.ibu.saudaraKandung or check2 in sdr.ayah.saudaraKandung:
            self.saudaraSepupu.append(sdr)
            
        self.in_saudarasp = 0
        for saudara in sdr.saudaraSepupu:
            if (self == saudara):
                self.in_saudarasp = 1
        if (self.in_saudarasp == 0):
            sdr.saudaraSepupu.append(self)
        
        
# Saudara kandung -> 
#       Syaratnya : Ayah dan Ibunya harus sama
# Saudara tiri ->
#       Syaratnya : Ayahnya berbeda atau Ibunya berbeda
# Saudara sepupu ->
#       Syaratnya : Anak dari saudara ayah kandung maupun saudara ibu kandung
# Cucu ->
#       Syaratnya : Anak dari semua anak kandung
# Mertua ->
#       Syaratnya : Ayah atau Ibu dari suami/istri
# Kakek ->
#       Syaratnya : Ayah dari ayah kandung atau ibu kandung
# Nenek ->
#       Syaratnya : Ibu dari ayah kandung atau ibu kandung
# Menantu ->
#       Syaratnya : Suami atau istri dari anak kandung
# Paman->
#       Syaratnya : Saudara laki-laki dari ayah kandung atau ibu kandung    
# Bibi ->
#       Syaratnya : Saudara perempuan dari ayah kandung atau ibu kandung    
# Ponakan ->
#       Syaratnya : Anak dari saudara kandung istri atau suami
# Ipar  ->
#       Syaratnya : Saudara dari suami atau istri

sokel = Personal("Sokel", "L")
dani = Personal("Dani", "P")

sirtha = Personal("Sirtha", "L")
suji = Personal("Suji", "P")

sugiarta = Personal("Sugiarta", "L")
widari = Personal("Ardi Widari", "P")
prianka = Personal("Prianka", "P")
ardhiya = Personal("Ardhiya", "P")
luxtor = Personal("Luxtor", "L")

utu = Personal("Utu", "P")
ketut = Personal("Ketut", "L")
wira = Personal("Wira", "L")
aris = Personal("Aris", "L")

arjana = Personal("Arjana", "L")
sus = Personal("Sus", "P")
leli = Personal("Leli", "P")
made = Personal("Made", "L")
intan = Personal("Intan", "P")

deduk = Personal("Deduk", "L")
ayu = Personal("Ayu", "P")
radha = Personal("Radha", "P")
dana = Personal("Dana", "L")

'''======================== KELUARGA INTI =========================='''
sugiarta.setIstri(widari)
sugiarta.setAnak(prianka)
sugiarta.setAnak(ardhiya)
sugiarta.setAnak(luxtor)

widari.setAnak(prianka)
widari.setAnak(ardhiya)
widari.setAnak(luxtor)

ardhiya.setSaudaraKandung(prianka)
ardhiya.setSaudaraKandung(luxtor)
prianka.setSaudaraKandung(luxtor)

'''========================================================='''
ketut.setIstri(utu)
ketut.setAnak(wira)
ketut.setAnak(aris)

utu.setAnak(wira)
utu.setAnak(aris)
wira.setSaudaraKandung(aris)

'''========================================================='''
arjana.setIstri(sus)
arjana.setAnak(leli)
arjana.setAnak(made)
arjana.setAnak(intan)

sus.setAnak(leli)
sus.setAnak(made)
sus.setAnak(intan)

'''========================================================='''
deduk.setIstri(ayu)
deduk.setAnak(radha)
deduk.setAnak(dana)

ayu.setAnak(radha)
ayu.setAnak(dana)


'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
'''======================== KELUARGA BESAR =========================='''
sokel.setIstri(dani)
sokel.setAnak(deduk)
sokel.setAnak(sugiarta)

dani.setAnak(deduk)
dani.setAnak(sugiarta)

sirtha.setIstri(suji)
sirtha.setAnak(widari)
sirtha.setAnak(utu)
sirtha.setAnak(arjana)

suji.setAnak(widari)
suji.setAnak(utu)
suji.setAnak(arjana)

widari.setSaudaraKandung(utu)
widari.setSaudaraKandung(arjana)

sugiarta.setSaudaraKandung(deduk)

ardhiya.setSaudaraSepupu(wira)
ardhiya.setSaudaraSepupu(aris)
ardhiya.setSaudaraSepupu(leli)
ardhiya.setSaudaraSepupu(made)
ardhiya.setSaudaraSepupu(intan)
ardhiya.setSaudaraSepupu(radha)
ardhiya.setSaudaraSepupu(dana)


print("Nama :",sirtha.nama)
for istri in sirtha.istri:
    print("  (Istri)",istri.nama)

print("")
print("Anak-anak dari",sirtha.nama,"adalah : ")
for anak in sirtha.anak:
    print(anak.nama)
    if (anak.sex == "L"):
        for istri in anak.istri:
            print("  (Istri)",istri.nama, "--> Menantu")
    else:
        for suami in anak.suami:
            print("  (Suami)",suami.nama, "--> Menantu")
    for child in anak.anak:
        print("    (Anak)",child.nama, "---> Cucu")
    
    print("")

print("==========================================")
print("Nama :",widari.nama)
for suami in widari.suami:
    print("  (Mertua)", suami.ibu.nama, "dan", suami.ayah.nama)
    print("  (Suami)",suami.nama)
    for saudara in suami.saudaraKandung:
        print("    (Ipar)", saudara.nama)
        for anak in saudara.anak:
            print("      (Ponakan)", anak.nama)
print("")

print("Saudara kandung", widari.nama, "adalah : ")
for saudara in widari.saudaraKandung:
    print(" (Saudara Kandung)", saudara.nama)
    for anak in saudara.anak:
        print("    (Ponakan)", anak.nama)
print("")

print("")
print("Anak-anak dari",widari.nama,"adalah : ")
for anak in widari.anak:
    print(anak.nama)
    for saudara in anak.saudaraKandung:
        print("  (Saudara Kandung)",saudara.nama)
        
    print("")
    for saudara in anak.ibu.saudaraKandung:
        if (saudara.sex == "P"):
            print("  (Bibi)", saudara.nama)
            for anak in saudara.anak:
                print("     (Saudara Sepupu)", anak.nama)
        
        else:
            print("  (Paman)", saudara.nama)
            for anak in saudara.anak:
                print("     (Saudara Sepupu)", anak.nama)
                
    print("")
    print("------------------------------------------")

print("==========================================")
print("Nama :",sugiarta.nama)
for istri in sugiarta.istri:
    print("  (Mertua)", istri.ibu.nama, "dan", istri.ayah.nama)
    print("  (Suami)",istri.nama)
    for saudara in istri.saudaraKandung:
        print("    (Ipar)", saudara.nama)
        for anak in saudara.anak:
            print("      (Ponakan)", anak.nama)
print("")

print("Saudara kandung", sugiarta.nama, "adalah : ")
for saudara in sugiarta.saudaraKandung:
    print(" (Saudara Kandung)", saudara.nama)
    for anak in saudara.anak:
        print("    (Ponakan)", anak.nama)
print("")

print("")
print("Anak-anak dari",sugiarta.nama,"adalah : ")
for anak in sugiarta.anak:
    print(anak.nama)
    for saudara in anak.saudaraKandung:
        print("  (Saudara Kandung)",saudara.nama)
        
    print("")
    for saudara in anak.ayah.saudaraKandung:
        if (saudara.sex == "P"):
            print("  (Bibi)", saudara.nama)
            for anak in saudara.anak:
                print("     (Saudara Sepupu)", anak.nama)
        
        else:
            print("  (Paman)", saudara.nama)
            for anak in saudara.anak:
                print("     (Saudara Sepupu)", anak.nama)
                
    print("")
    print("------------------------------------------")
    
print("==========================================")
print("Nama :",ardhiya.nama)
print("  (Ibu)", ardhiya.ibu.nama)
print("    (Kakek)", ardhiya.ibu.ayah.nama)
print("    (Nenek)", ardhiya.ibu.ibu.nama)
print("")
print("  (Ayah)", ardhiya.ayah.nama)
print("    (Kakek)", ardhiya.ayah.ayah.nama)
print("    (Nenek)", ardhiya.ayah.ibu.nama)
print("")    

print("Saudara kandung", ardhiya.nama, "adalah : ")
for saudara in ardhiya.saudaraKandung:
    print("  (Saudara Kandung)", saudara.nama)
print("")

print("Saudara sepupu", ardhiya.nama, "adalah : ")
for saudara in ardhiya.saudaraSepupu:
    print("  (Saudara Sepupu)", saudara.nama)
print("")  

# print("Saudara tiri", ardhiya.nama, "adalah : ")
# for saudara in ardhiya.saudaraTiri:
#     print(" (saudara tiri)", saudara.nama)
# print("")

# print("Saudara kandung", prianka.nama, "adalah : ")
# for saudara in prianka.saudaraKandung:
#     print(" (saudara kandung)", saudara.nama)
# print("")

# print("Saudara kandung", luxtor.nama, "adalah : ")
# for saudara in luxtor.saudaraKandung:
#     print(" (saudara kandung)", saudara.nama)
# print("")        

# print("Tante dari", wira.nama, "adalah : ")
# for saudara in wira.ibu.saudaraKandung:
#     print(" (saudara kandung)", saudara.nama)
# print("")  
