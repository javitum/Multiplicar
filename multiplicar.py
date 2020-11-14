import sys
from PyQt5.QtCore import pyqtSlot ,  QSettings
from PyQt5 import QtCore ,  QtWidgets , QtMultimedia
from Ui_multiplicar import *
from random import randint

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.trans=QtCore.QTranslator(self)
        idiomas=['Español', 'English']
        self.comboBoxIdioma.addItems(idiomas)
        self.settings = QSettings('javitum', 'Multiplicar')
        if len(self.settings.childKeys()) !=0: self.cargar_configuracion()
        self.pushButtonGenerar.clicked.connect(self.Generar)
        self.pushButtonComprobar.clicked.connect(self.Comprovar)  
        self.pushButtonReiniciar.clicked.connect(self.Reiniciar)
        self.pushButtonSalir.clicked.connect(self.Salir)
   
    def Generar(self):
        tablas=[]
        self.textEditllevadas1.setText("")
        self.textEditllevadas2.setText("")
        self.textEditllevadas3.setText("")
        self.textEditllevadas4.setText("")
        self.lineEditdecenasdemillares.setText("")
        self.lineEditmillares.setText("")
        self.lineEditcentenas.setText("")
        self.lineEditdecenas.setText("")
        self.lineEditunidades.setText("")
        self.labelresultado_2.setText("")
        self.labelresultado.setText("")
        self.textEditllevadas1.setEnabled(False)
        self.textEditllevadas2.setEnabled(False)
        self.textEditllevadas3.setEnabled(False)
        self.textEditllevadas4.setEnabled(False)
        
        if self.checkBox.isChecked()==True:
            tablas.append(1)
        if self.checkBox_2.isChecked()==True:
            tablas.append(2)
        if self.checkBox_3.isChecked()==True:
            tablas.append(3)
        if self.checkBox_4.isChecked()==True:
            tablas.append(4)
        if self.checkBox_5.isChecked()==True:
            tablas.append(5)
        if self.checkBox_6.isChecked()==True:
            tablas.append(6)
        if self.checkBox_7.isChecked()==True:
            tablas.append(7)
        if self.checkBox_8.isChecked()==True:
            tablas.append(8)
        if self.checkBox_9.isChecked()==True:
            tablas.append(9)
        if self.checkBox_10.isChecked()==True:
            tablas.append(10)
        n_tablas=len(tablas)
        tablaaleatoria=tablas[randint(0, n_tablas-1)]
        self.labelmultiplicador.setText(str(tablaaleatoria))    
        cifras_multiplicando=[]
        if self.checkBox_11.isChecked()==True:
            cifras_multiplicando.append(1)
        if self.checkBox_12.isChecked()==True:
            cifras_multiplicando.append(2)
        if self.checkBox_13.isChecked()==True:
            cifras_multiplicando.append(3)
        if self.checkBox_14.isChecked()==True:
            cifras_multiplicando.append(4)
        if self.checkBox_15.isChecked()==True:
            cifras_multiplicando.append(5)      
        n_cifras=len(cifras_multiplicando)
        cifrasaleatoria=cifras_multiplicando[randint(0, n_cifras-1)]
            
        if cifrasaleatoria==1:
            multiplicando=randint(1, 9)
            self.labelmultiplicando.setText(str(multiplicando))
        if cifrasaleatoria==2:
            multiplicando=randint(1, 99)
            self.labelmultiplicando.setText(str(multiplicando))
            self.textEditllevadas1.setEnabled(True)
        if cifrasaleatoria==3:
            multiplicando=randint(1, 999)
            self.labelmultiplicando.setText(str(multiplicando)) 
            self.textEditllevadas1.setEnabled(True)
            self.textEditllevadas2.setEnabled(True)  
        if cifrasaleatoria==4:
            multiplicando=randint(1, 9999)
            self.labelmultiplicando.setText(str(multiplicando))
            self.textEditllevadas1.setEnabled(True)
            self.textEditllevadas2.setEnabled(True)
            self.textEditllevadas3.setEnabled(True)
        if cifrasaleatoria==5:
            multiplicando=randint(1, 99999)
            self.labelmultiplicando.setText(str(multiplicando)) 
            self.textEditllevadas1.setEnabled(True)
            self.textEditllevadas2.setEnabled(True)
            self.textEditllevadas3.setEnabled(True)
            self.textEditllevadas4.setEnabled(True)
        self.pushButtonGenerar.setEnabled(False)
        self.pushButtonComprobar.setEnabled(True)
        self.lineEditunidades.setFocus()

       
    def Comprovar(self):
        if self.lineEditdecenasdemillares.text()=="":
            decenasdemillares=0
        else:
            decenasdemillares=int(self.lineEditdecenasdemillares.text())*10000
        if self.lineEditmillares.text()=="":
            millares=0
        else:
            millares=int(self.lineEditmillares.text())*1000            
        if self.lineEditcentenas.text()=="":
            centenas=0
        else:
            centenas=int(self.lineEditcentenas.text())*100
        if self.lineEditdecenas.text()=="":
            decenas=0
        else:
            decenas=int(self.lineEditdecenas.text())*10
        if self.lineEditunidades.text()=="":
            unidades=0
        else:
            unidades=int(self.lineEditunidades.text())
        miresultado=decenasdemillares+millares+centenas+decenas+unidades
        multiplicando=int(self.labelmultiplicando.text())
        multiplicador=int(self.labelmultiplicador.text())
        resultado=multiplicando*multiplicador
        self.labelresultado.setText(str(resultado)) 
        if miresultado==resultado:
          self.labelresultado_2.setText(self.tr("Bien")) 
          bien=int(self.labelbien.text())+1
          self.labelbien.setText(str(bien))
        else:
          self.labelresultado_2.setText(self.tr("Mal"))
          mal=int(self.labelmal.text())+1
          self.labelmal.setText(str(mal))
        
        ejercicios=int(self.labelejercicios.text())+1
        self.labelejercicios.setText(str(ejercicios))
        bien=int(self.labelbien.text())
        nota=(bien/ejercicios)*10
        self.labelnota.setText(str(nota))
        self.pushButtonGenerar.setEnabled(True)
        self.pushButtonComprobar.setEnabled(False)
        self.pushButtonGenerar.setFocus()
        
        ejercicios_min=int(self.lineEditEjercicios_min.text())
        nota_min=int(self.lineEditNota_min.text())
        
        if ejercicios>=ejercicios_min and nota>=nota_min:
            self.corazon.setGeometry(1260,520,220,216)
            self.pushButtonGenerar.setEnabled(False)
            self.pushButtonComprobar.setEnabled(False)
            filename = 'Aplausos.mp3'
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player = QtMultimedia.QMediaPlayer()
            self.player.setMedia(content)
            self.player.play()
          
    def Reiniciar(self):
        self.textEditllevadas1.setText("")
        self.textEditllevadas2.setText("")
        self.textEditllevadas3.setText("")
        self.textEditllevadas4.setText("")
        self.lineEditdecenasdemillares.setText("")
        self.lineEditmillares.setText("")
        self.lineEditcentenas.setText("")
        self.lineEditdecenas.setText("")
        self.lineEditunidades.setText("")
        self.labelresultado_2.setText("")
        self.labelresultado.setText("")
        self.labelejercicios.setText("0")
        self.labelmultiplicando.setText("")
        self.labelmultiplicador.setText("")
        self.labelbien.setText("0")
        self.labelmal.setText("0")
        self.labelnota.setText("")
        self.pushButtonGenerar.setEnabled(True)
        self.pushButtonComprobar.setEnabled(False)
        self.corazon.setGeometry(1260,520,1,1)
        MainWindow.guardar_configuracion(self) 
                     
    def Salir(self):
        MainWindow.guardar_configuracion(self) 
        sys.exit()

    @pyqtSlot(str)
    def on_comboBoxIdioma_currentIndexChanged(self, p0):
        idiomas={'Español':'', 'English':'en'}
        idioma_seleccionado=idiomas[p0]
        if idioma_seleccionado:
            self.trans.load(str(idioma_seleccionado))
            QtWidgets.QApplication.instance().installTranslator(self.trans)
        else:
            QtWidgets.QApplication.instance().removeTranslator(self.trans)
        self.retranslateUi(MainWindow)
     
    def guardar_configuracion(self):
        self.settings.setValue('idioma', self.comboBoxIdioma.currentText())
        self.settings.setValue('ejer_min', self.lineEditEjercicios_min.text())
        self.settings.setValue('nota_min', self.lineEditNota_min.text())
        self.settings.setValue('1', self.checkBox.isChecked())
        self.settings.setValue('2', self.checkBox_2.isChecked())
        self.settings.setValue('3', self.checkBox_3.isChecked())
        self.settings.setValue('4', self.checkBox_4.isChecked())
        self.settings.setValue('5', self.checkBox_5.isChecked())
        self.settings.setValue('6', self.checkBox_6.isChecked())
        self.settings.setValue('7', self.checkBox_7.isChecked())
        self.settings.setValue('8', self.checkBox_8.isChecked())
        self.settings.setValue('9', self.checkBox_9.isChecked())
        self.settings.setValue('10', self.checkBox_10.isChecked())
        self.settings.setValue('11', self.checkBox_11.isChecked())
        self.settings.setValue('12', self.checkBox_12.isChecked())
        self.settings.setValue('13', self.checkBox_13.isChecked())
        self.settings.setValue('14', self.checkBox_14.isChecked())
        self.settings.setValue('15', self.checkBox_15.isChecked())
        
    def cargar_configuracion(self):
        self.comboBoxIdioma.setCurrentText(self.settings.value('idioma'))
        self.lineEditEjercicios_min.setText(self.settings.value('ejer_min'))
        self.lineEditNota_min.setText(self.settings.value('nota_min'))
        self.checkBox.setChecked(eval(self.settings.value('1').capitalize()))
        self.checkBox_2.setChecked(eval(self.settings.value('2').capitalize()))
        self.checkBox_3.setChecked(eval(self.settings.value('3').capitalize()))
        self.checkBox_4.setChecked(eval(self.settings.value('4').capitalize()))
        self.checkBox_5.setChecked(eval(self.settings.value('5').capitalize()))
        self.checkBox_6.setChecked(eval(self.settings.value('6').capitalize()))
        self.checkBox_7.setChecked(eval(self.settings.value('7').capitalize()))
        self.checkBox_8.setChecked(eval(self.settings.value('8').capitalize()))
        self.checkBox_9.setChecked(eval(self.settings.value('9').capitalize()))
        self.checkBox_10.setChecked(eval(self.settings.value('10').capitalize()))
        self.checkBox_11.setChecked(eval(self.settings.value('11').capitalize()))
        self.checkBox_12.setChecked(eval(self.settings.value('12').capitalize()))
        self.checkBox_13.setChecked(eval(self.settings.value('13').capitalize()))
        self.checkBox_14.setChecked(eval(self.settings.value('14').capitalize()))
        self.checkBox_15.setChecked(eval(self.settings.value('15').capitalize()))  



  
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
