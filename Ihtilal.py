import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout, QDialog, QLineEdit,QRadioButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Karakter Sınıfı
class Karakter:
    def __init__(self, isim, zeka, karizma, iletisim, diktator_puani, memleket):
        self.isim = isim
        self.zeka = zeka
        self.karizma = karizma
        self.iletisim = iletisim
        self.diktator_puani = diktator_puani
        self.memleket = memleket

# Karakter Tanımlandı
karakter1 = Karakter("",0,0,0,0,"")



class AnketlerEkrani(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,700,300)
        self.setWindowTitle("Anketler")
        self.initUI()

    def initUI(self):
        self.lblXuna = QLabel("Xuna: ")
        self.lblArigma = QLabel("Arigma: ")
        self.lblSora = QLabel("Sora: ")
        self.XunaAnketAlani = QLineEdit()
        self.XunaAnketAlani.setReadOnly(True)
        self.ArigmaAnketAlani = QLineEdit()
        self.ArigmaAnketAlani.setReadOnly(True)
        self.SoraAnketAlani = QLineEdit()
        self.SoraAnketAlani.setReadOnly(True)
        
        


# Karakter Oluşturma Ekranı
class KarakterOlusturmaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,400,100)
        self.setWindowTitle("Karakter Oluşturma")
        self.initUI()

    def initUI(self):
        self.lblIsim = QLabel("İsim: ")
        self.isimAlani = QLineEdit()
        self.lblMemleket = QLabel("Karkaterinizin doğduğu yeri seçiniz.")
        self.sehir1btn = QRadioButton("Xuna")
        self.sehir1btn.setToolTip("Xuna Enizo ülkesinin başkentidir. Genellikle devlet görevlilerinin yaşadığı çok hareketi ve eylemi olmayan bir şehirdir.")
        self.sehir1btn.setChecked(True)
        self.sehir2btn = QRadioButton("Arigma")
        self.sehir2btn.setToolTip("Arigma Enizo ülkesinin en zengin insanlarının yaşadığı jet-sosyete şehridir. Oldukça hareketli ve pahalıdır.")
        self.sehir3btn = QRadioButton("Sora")
        self.sehir3btn.setToolTip("Sora Enizo ülkesinin üretim yükünü çeken kırsal kesimin yaşadığı şehirdir. Eylem açısından oldukça yoğundur.")
        self.kaydetBtn = QPushButton("Kaydet")
        self.kaydetBtn.clicked.connect(self.actKaydet)

        usthbox = QHBoxLayout()
        usthbox.addWidget(self.lblIsim)
        usthbox.addWidget(self.isimAlani)
        usthbox.addStretch(1)
        usthbox.addWidget(self.kaydetBtn)

        ustaltbox = QHBoxLayout()
        ustaltbox.addWidget(self.lblMemleket)
        
        altbox = QHBoxLayout()
        altbox.addWidget(self.sehir1btn)
        altbox.addStretch(1)
        altbox.addWidget(self.sehir2btn)
        altbox.addStretch(1)
        altbox.addWidget(self.sehir3btn)
        
        mainBox = QVBoxLayout()
        mainBox.addLayout(usthbox)
        mainBox.addLayout(ustaltbox)
        mainBox.addLayout(altbox)
        mainBox.addStretch(1)

        self.setLayout(mainBox)

    def actKaydet(self):
        karakter1.isim = self.isimAlani.text()
        if self.sehir1btn.isChecked():
            karakter1.memleket = "Xuna"
            karakter1.zeka = 3
            karakter1.karizma = 0
            karakter1.iletisim = 0
            karakter1.diktator_puani = 0
        elif self.sehir2btn.isChecked():
            karakter1.memleket = "Arigma"
            karakter1.karizma = 3
            karakter1.iletisim = 0
            karakter1.diktator_puani = 0
            karakter1.zeka = 0
        else:
            karakter1.memleket = "Sora"
            karakter1.iletisim = 3
            karakter1.karizma = 0
            karakter1.diktator_puani = 0
            karakter1.zeka = 0
        

        self.close()
        

# Harita Dialogu
class Harita(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,500,150)
        self.setWindowTitle("Harita")
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.lbl = QLabel()
        pixmap = QPixmap("harita.jpeg")
        self.lbl.setPixmap(pixmap)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

# İstatistikler Dialogu
class StatsEkran(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,200)
        self.setWindowTitle("İstatistikler")
        self.initUI()

    def initUI(self):
        # Widget Alanı
        self.lblIsim = QLabel("İsim: ")
        self.isimAlani = QLineEdit()
        self.isimAlani.setReadOnly(True)
        self.isimAlani.setText(karakter1.isim)
        self.lblZeka = QLabel("Zeka: ")
        self.zekaAlani = QLineEdit()
        self.zekaAlani.setReadOnly(True)
        self.zekaAlani.setText(str(karakter1.zeka))
        self.lblKarizma = QLabel("Karizma: ")
        self.karizmaAlani = QLineEdit()
        self.karizmaAlani.setReadOnly(True)
        self.karizmaAlani.setText(str(karakter1.karizma))
        self.lblIletisim = QLabel("İletişim: ")
        self.iletisimALani = QLineEdit()
        self.iletisimALani.setReadOnly(True)
        self.iletisimALani.setText(str(karakter1.iletisim))
        self.lblDp = QLabel("Diktator Puanı: ")
        self.DpAlan = QLineEdit()
        self.DpAlan.setReadOnly(True)
        self.DpAlan.setText(str(karakter1.diktator_puani))
        self.lblMemleket = QLabel("Memleket: ")
        self.memleketAlani = QLineEdit()
        self.memleketAlani.setReadOnly(True)
        self.memleketAlani.setText(karakter1.memleket)


        isimHBox = QHBoxLayout()
        isimHBox.addWidget(self.lblIsim)
        isimHBox.addWidget(self.isimAlani)

        zekaHbox = QHBoxLayout()
        zekaHbox.addWidget(self.lblZeka)
        zekaHbox.addWidget(self.zekaAlani)

        karizmaHbox = QHBoxLayout()
        karizmaHbox.addWidget(self.lblKarizma)
        karizmaHbox.addWidget(self.karizmaAlani)

        iletisimHbox = QHBoxLayout()
        iletisimHbox.addWidget(self.lblIletisim)
        iletisimHbox.addWidget(self.iletisimALani)

        dpHbox = QHBoxLayout()
        dpHbox.addWidget(self.lblDp)
        dpHbox.addWidget(self.DpAlan)

        memleketHBox = QHBoxLayout()
        memleketHBox.addWidget(self.lblMemleket)
        memleketHBox.addWidget(self.memleketAlani)

        vbox = QVBoxLayout()
        vbox.addLayout(isimHBox)
        vbox.addLayout(zekaHbox)
        vbox.addLayout(karizmaHbox)
        vbox.addLayout(iletisimHbox)
        vbox.addLayout(dpHbox)
        vbox.addLayout(memleketHBox)
        
        mainbox = QHBoxLayout()
        mainbox.addLayout(vbox)
        mainbox.addStretch(1)

        self.setLayout(mainbox)



        


class AnaEkran(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("AnaEkran")
        self.setGeometry(10, 10, 1280, 720)
        
    def initUI(self):
        self.hikaye = []
        self.hikayeSayaci = 0

        with open('senaryo.txt','r') as file:
            self.hikaye = file.readlines()

        # Widget alanı
        self.btnStats = QPushButton("İstatistikler")
        self.btnStats.clicked.connect(self.actStats)
        self.btnHarita = QPushButton("Harita")
        self.btnHarita.clicked.connect(self.actHarita)
        self.btnKaydet = QPushButton("Kaydet")
        self.hikayeAlani = QTextEdit()
        self.hikayeAlani.setReadOnly(True)
        self.hikayeAlani.setMaximumHeight(100)
        self.hikayeAlani.setText("İhtilal Oyununa Hoş Geldiniz.")
        self.btnAnketler = QPushButton("Anketler")
        self.btnIleri = QPushButton("Ileri")
        self.btnIleri.clicked.connect(self.actIleri)
        self.lblResim = QLabel()
        self.pixmap = QPixmap()
        self.lblResim.setPixmap(self.pixmap)

        # Ekranın Üst Kısmı
        ustBox = QHBoxLayout()
        ustBox.addWidget(self.btnStats)
        ustBox.addWidget(self.btnHarita)
        ustBox.addWidget(self.btnAnketler)
        ustBox.addStretch()
        ustBox.addWidget(self.btnKaydet)
        ustBox.addWidget(self.btnIleri)

        # Ekranın Orta Kısmı
        ortaBox = QHBoxLayout()
        ortaBox.addStretch(1)
        ortaBox.addWidget(self.lblResim)
        ortaBox.addStretch(1)

        # Ekranın Alt Kısmı
        altBox = QHBoxLayout()
        altBox.addWidget(self.hikayeAlani)

        # Main Box
        mainBox = QVBoxLayout()
        mainBox.addLayout(ustBox)
        mainBox.addLayout(ortaBox)
        mainBox.addLayout(altBox)
        self.setLayout(mainBox)

    # ileri butonunun fonksiyonu
    def actIleri(self):
        self.hikayeAlani.setText(self.hikaye[self.hikayeSayaci])
        self.hikayeSayaci += 1
        if self.hikayeSayaci == 2:
            karakter_olusturma = KarakterOlusturmaDialog()
            karakter_olusturma.exec_()
        

    # Harita Butonunun Fonksiyonu
    def actHarita(self):
        harita = Harita()
        harita.exec_()

    def actStats(self):
        stats = StatsEkran()
        stats.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AnaEkran()
    main.show()  # Ana pencereyi göstermek için show() çağrılmalı
    print()
    sys.exit(app.exec_())
