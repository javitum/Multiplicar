import sys
from Ui_multiplicar import *
from random import randint

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Multiplicar")
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
        self.textEditdecenasdemillares.setText("")
        self.textEditmillares.setText("")
        self.textEditcentenas.setText("")
        self.textEditdecenas.setText("")
        self.textEditunidades.setText("")
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
        self.textEditunidades.setFocus()

       
    def Comprovar(self):
        if self.textEditdecenasdemillares.toPlainText()=="":
            decenasdemillares=0
        else:
            decenasdemillares=int(self.textEditdecenasdemillares.toPlainText())*10000
        if self.textEditmillares.toPlainText()=="":
            millares=0
        else:
            millares=int(self.textEditmillares.toPlainText())*1000            
        if self.textEditcentenas.toPlainText()=="":
            centenas=0
        else:
            centenas=int(self.textEditcentenas.toPlainText())*100
        if self.textEditdecenas.toPlainText()=="":
            decenas=0
        else:
            decenas=int(self.textEditdecenas.toPlainText())*10
        if self.textEditunidades.toPlainText()=="":
            unidades=0
        else:
            unidades=int(self.textEditunidades.toPlainText())
        miresultado=decenasdemillares+millares+centenas+decenas+unidades
        multiplicando=int(self.labelmultiplicando.text())
        multiplicador=int(self.labelmultiplicador.text())
        resultado=multiplicando*multiplicador
        self.labelresultado.setText(str(resultado)) 
        if miresultado==resultado:
          self.labelresultado_2.setText("Bien") 
          bien=int(self.labelbien.text())+1
          self.labelbien.setText(str(bien))
        else:
          self.labelresultado_2.setText("Mal") 
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
        if ejercicios>=20 and nota>=8:
            self.corazon.setGeometry(1260,520,220,216)
        else:
            self.corazon.setGeometry(1260,520,1,1)
          
    def Reiniciar(self):
        self.textEditllevadas1.setText("")
        self.textEditllevadas2.setText("")
        self.textEditllevadas3.setText("")
        self.textEditllevadas4.setText("")
        self.textEditdecenasdemillares.setText("")
        self.textEditmillares.setText("")
        self.textEditcentenas.setText("")
        self.textEditdecenas.setText("")
        self.textEditunidades.setText("")
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
                     
    def Salir(self):
        sys.exit()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
