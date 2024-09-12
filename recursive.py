def f(s, i):#s yi input i yi index olarak düşündüm
    if s.count('(') !=s.count(')') and i==0: # s de ki açık ve kapalı panranteszleri sayacak ama her seferinde çalışmasın diye i=0 şartı ekledim gerçi her seferinde çalışsada bir zararı dokunmuyor bize
        raise ValueError("Parantezler Eşit Değil")#hatayı verdik
    sonuc = '' #bu bizim nihai sonucumuz yani fonksiyonun dışındaki printte yazacak değer ilk başta da boş veriyoruz
    while i < len(s):
        if s[i].isdigit():#burda da python un güzelliğinden yararlanıp o index deki eleman sayı mı değil mi kontrol ediyoruz
            carpan = 0 # metnin kaç kere yazılması gerektiğini tutan eleman
            while i < len(s) and s[i].isdigit():  # bir döngü daha bunun amacı ard arda gelen elemanları doğru ondalıklı biçimde göstermek 12 yi 1 ve 2 değilde 12 şeklinde göstersin
                carpan = carpan * 10 + int(s[i]) # Mesela 12(ab) olsun ilk karşılaştığımız sayı 1 carpan ın değeri 1 olur i yi 1 dahaa artttırdım yine sayı denk geldiyse bu sefer 10 la çarpıp ikinci denk geldiğim sayıyı da toplarım
                
                i += 1
            if s[i] == '(':#burdaki amaç sayıdan sonra '(' geliyor mu task de istediğiniz gibi
               i += 1  #eğer geliyorsa i yi arttır diğer elemana geç çünkü açık parantezle bir işimiz yok
               cozulmus_metin, i = f(s, i)#Geldik Recursive fonksiyona .Alttaki metine göre inceleyecek olursak şuan i=2 yani f(s,2) yi çağırcak aynı bizim faktöriyeldeki gibi 
               """
               Burdan anlatması daha kolay olacak 
               Çözülmüş metnin ilk değeri a olacak
               2. değeri :ab
               3. değeri :abc olacak
               sonra '(' denk geldiği için sonucu ve i yi returnleyecek aşağıdaki fonksiyonda 
               iç içe kısımlar bittikten sonra 
               """
               print(f"{cozulmus_metin}'nın çarpanı:{carpan}")
               sonuc += cozulmus_metin * carpan # çözülmüş metnin son halindne sonra carpan kaçsa okadar kere ard arda yazılacak ve sonuca dahil edilecek 
               print(f"Çarpılmış hali {sonuc}")
               i += 1 # bi sonraki işlem için i yi arttırıcaz eğer zaten artık döngü şartı sağlanmıyor ise döngü kırılacak
               
            else:
                raise ValueError("Sayıdan Sonra '(' gelmeli")
        elif s[i] == ')':
         return sonuc, i # çözülmüş metnin son halini verir
        else:
          
            sonuc += s[i]
            print(sonuc)
            i += 1
    
    return sonuc # bizim fonksiyonun asıl nihai sonucunu bu return verecek
try:
     metin = "3(abc)4(b)"
     cozulmus_metin= f(metin,0)#fonksiyon diğer
     print(f"Sonuç:{cozulmus_metin}")
except ValueError as e:
     print(e)
"""
Özet:
-Parantezler sayılır eşit değilse raislenir ve hiç bir çıktı vermeden error verir
-Metin  alınır ve 3 şart var:
     -Ya sayı olabilir
     -Ya ( olavilir
     -Ya da düz metin olabilir

     SAyıysa:
          - kaç kere çarpılcağını belirleirz.
          -Sayıdan sonra parantez mi geliyor kontrol ederiz gelmiyorsa error verdidiriz
          -parantez geliyorsa bir index arttıırız ve recursive fonksiyonla kendi kendini çağırarak çözülmüş metine eşitler en son ) denk geldiğinde çözülmüş metnin son halini 
          alır ve kaç kere yazıdırılacaksa yazdırılır.

"""