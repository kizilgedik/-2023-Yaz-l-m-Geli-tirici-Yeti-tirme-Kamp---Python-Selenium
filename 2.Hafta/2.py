##Ödev-2.Hafta

##Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
##
##Bu öğrenci kayıt sistemine;
##
##    Aldığı isim soy isim ile listeye öğrenci ekleyen
##    Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
##    Listeye birden fazla öğrenci eklemeyi mümkün kılan
##    Listedeki tüm öğrencileri tek tek ekrana yazdıran
##    Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
##    Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
##
##fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
##
##Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
##
##
##



ogrenciler = []

def ogrenci_ekle(*args):
    for ogrenci in args:
        ogrenciler.append(ogrenci)
        print(f"{ogrenci} eklendi.")

def ogrenci_sil(ad, soyad):
    for ogrenci in ogrenciler:
        if ogrenci[0] == ad and ogrenci[1] == soyad:
            ogrenciler.remove(ogrenci)
            print(f"{ogrenci} silindi.")

def ogrencileri_listele():
    for ogrenci in ogrenciler:
        print(ogrenci)
def ogrenci_numarasi(ad, soyad):
    for i, ogrenci in enumerate(ogrenciler):
        if ogrenci[0] == ad and ogrenci[1] == soyad:
            print(f"{ad} {soyad} öğrencisi {i} numaralı öğrencidir.")
def ogrencileri_coklu_sil(*args):
    while args:
        ad, soyad = args[:2]
        args = args[2:]
        ogrenci_sil(ad, soyad)

ogrenci_ekle(("Ali", "Yılmaz"), ("Ayşe", "Bakır"), ("Ahmet", "Biçer"))
ogrencileri_listele()
ogrenci_sil("Ayşe", "Bakır")
ogrencileri_listele()
ogrenci_numarasi("Ali", "Yılmaz")
ogrencileri_coklu_sil("Ahmet", "Yılmaz", "Ali", "Kaya")
ogrencileri_listele()

