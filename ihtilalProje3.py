import sys
import sqlite3
from PyQt5 import QtWidgets

conn = sqlite3.connect("OyunDosyasi.db")
cursor = conn.cursor()



class Karakter:
    def __init__(self,isim,karizma,zeka,memleket,konusma):
        self.isim = isim
        self.karizma = karizma
        self.zeka = zeka
        self.memleket = memleket
        self.konusma = konusma

    def Kaydet(self):
        cursor.execute("create table if not exist Karakter()")
        
karakter1 = Karakter("",0,0,"",0)


class KarakterOlusturmaDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Karakter Oluşturma")
        self.setGeometry(300, 300, 720, 360)
        self.initUI()
    
    def initUI(self):
        
        self.isim_label = QtWidgets.QLabel("İsminiz: ")
        self.isim_alani = QtWidgets.QLineEdit()
        self.sehir1_label = QtWidgets.QLabel("şehir bir yazı alanı")
        self.sehir2_label = QtWidgets.QLabel("şehir iki yazı alanı")
        self.sehir3_label = QtWidgets.QLabel("şehir üç yazı alanı")
        self.sehir1_rb = QtWidgets.QRadioButton("Şehir 1")
        self.sehir2_rb = QtWidgets.QRadioButton("Şehir 2")
        self.sehir3_rb = QtWidgets.QRadioButton("Şehir 3")
        self.karakterkaydet_btn = QtWidgets.QPushButton("Karakteri Oluştur")

        kUstBox = QtWidgets.QVBoxLayout()
        kUstBox.addWidget(self.isim_label)
        kUstBox.addWidget(self.isim_alani)

        kOrtaUstBox = QtWidgets.QHBoxLayout()
        kOrtaUstBox.addWidget(self.sehir1_label)
        kOrtaUstBox.addWidget(self.sehir2_label)
        kOrtaUstBox.addWidget(self.sehir3_label)

        kOrtaAltBox = QtWidgets.QHBoxLayout()
        kOrtaAltBox.addWidget(self.sehir1_rb)
        kOrtaAltBox.addWidget(self.sehir2_rb)
        kOrtaAltBox.addWidget(self.sehir3_rb)

        kBox = QtWidgets.QHBoxLayout()
        kBox.addStretch()
        kBox.addWidget(self.karakterkaydet_btn)

        kMainBox = QtWidgets.QVBoxLayout()
        kMainBox.addLayout(kUstBox)
        kMainBox.addLayout(kOrtaUstBox)
        kMainBox.addLayout(kOrtaAltBox)
        kMainBox.addLayout(kBox)

        self.setLayout(kMainBox)
        self.karakterkaydet_btn.clicked.connect(self.actKaydet)

    def actKaydet(self):
        karakter1.isim = self.isim_alani.text()
        self.close()
        
    
        


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle("İhtilal")
        self.initUI()
    
    def initUI(self):
        self.hikaye = ["İhtilal Oyununa Hoş Geldiniz.","Önce Karakter Oluşturalım","Tebrikler Karakterinizi Oluşturdunuz.","Oyuna Başlayalım","","","","","","","","","","",""]
        self.ileriSayac = 0

        self.btnStat = QtWidgets.QPushButton("İstatistikler")
        self.btnMap = QtWidgets.QPushButton("Harita")
        self.saveBtn = QtWidgets.QPushButton("Kaydet")
        self.ileriBtn = QtWidgets.QPushButton("İleri")
        self.ileriBtn.clicked.connect(self.actIleri)
        self.geriBtn = QtWidgets.QPushButton("Geri")
        self.geriBtn.clicked.connect(self.actGeri)
        self.txtHikaye = QtWidgets.QLineEdit()
        self.txtHikaye.setReadOnly(True)

        ustBox = QtWidgets.QHBoxLayout()
        ustBox.addWidget(self.btnStat)
        self.btnStat.clicked.connect(self.showStat)
        ustBox.addWidget(self.btnMap)
        ustBox.addStretch()
        ustBox.addWidget(self.saveBtn)

        altBox = QtWidgets.QHBoxLayout()
        altBox.addWidget(self.txtHikaye)
        altBox.addWidget(self.ileriBtn)
        altBox.addWidget(self.geriBtn)

        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addLayout(ustBox)
        mainBox.addStretch()
        mainBox.addLayout(altBox)
        self.setLayout(mainBox)
        self.show()
        
    def actIleri(self):
        self.txtHikaye.setText(self.hikaye[self.ileriSayac])
        self.ileriSayac += 1
        if self.ileriSayac == 2:
            self.show_character_creation_dialog()

    def actGeri(self):
        self.txtHikaye.setText(self.hikaye[self.ileriSayac])
        self.ileriSayac -= 1
        

        
    def show_character_creation_dialog(self):
        dialog = KarakterOlusturmaDialog()
        dialog.exec_()
        
    def showStat(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Stats")
        dialog.setGeometry(200,200,720,360)
        statName = QtWidgets.QLabel()
        statName.setText("İsim: {}".format(karakter1.isim))
        statKarizma = QtWidgets.QLabel()
        statKarizma.setText("Karizma: {}".format(karakter1.karizma))
        statZeka = QtWidgets.QLabel()
        statZeka.setText("Zeka: {}".format(karakter1.zeka))
        statKonusma = QtWidgets.QLabel()
        statKonusma.setText("Konuşma: {}".format(karakter1.konusma))
        statVbox = QtWidgets.QVBoxLayout()
        statVbox.addWidget(statName)
        statVbox.addWidget(statKarizma)
        statVbox.addWidget(statZeka)
        statVbox.addWidget(statKonusma)
        statVbox.addStretch()
        dialog.setLayout(statVbox)
        dialog.exec_()

app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec_())
