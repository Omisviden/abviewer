import sys
import json

from PyQt5.QtWidgets import QMainWindow, QAction, QDesktopWidget, QApplication, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QGridLayout, QPushButton, QLayoutItem
from PyQt5.QtGui import QIcon, QImage, QBrush, QPalette
from PyQt5.QtCore import QSize, Qt

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    
    def initUI(self):

        # Menu creation
        exitAct = QAction(QIcon('res/cat.jpeg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Alt+Shift+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        
        createAct = QAction(QIcon('res/HYPERBRUH.jpeg'), 'Create new block', self) # Dope icon(...?)
        createAct.setShortcut('F5')
        createAct.setStatusTip('Create new block')

        # Creating a statusBar to show statusTips
        self.statusBar()
        
        # Adding stuff to the window
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(createAct)
        toolbar = self.addToolBar('Create')
        toolbar.addAction(createAct)
        toolbar.addAction(exitAct)

        # QGridLayout setup
        self.grid = QGridLayout()
        self.combos = [
        '1', '1', '1', '', '1.5',                     # 1: Attacks from top right
        '2', '1', '1', '', '2.5',                   # 2: Attacks from top left
        '1', '1', '1', '', '3.5',                     # 3: Attacks from bottom right          (.5 means attacks ending in the starting position are taken out
        '1', '1', '1', '', '4.5']                     # 4: Attacks from bottom left                              because alternate attacks do not allow them) 

        comboList = {}

        positions = [(i,j) for i in range(5) for j in range(5)]
        for position, drawcombo in zip(positions, self.combos):
            self.combo = QComboBox()
            pcstr = """self.combo.setAutoFillBackground(True)
            p = QPalette()
            p.setColor(self.backgroundRole(), Qt.black)
            self.setPalette(p)"""
            self.combo.setStyleSheet("background-color: #333333; color: #FFFFFF; selection-background-color: #660000")     
            self.combo.palette().highlight().color().name()
            
            if drawcombo == '':
                continue
            elif drawcombo == '1':
                for x in range(0, 49):
                    data = json.loads("absolver_deck_reviewer/Absolver-Data/attacks/all.json")            
                    self.combo.addItem(QIcon('absolver_deck_reviewer/Absolver-Data/AttackPictos.png/{}.png'.format(x)), "placeholder :D")      
                                

            elif drawcombo == '2': #TODO: Combo selection
                pass
            elif drawcombo == '3':
                pass
            elif drawcombo == '4':
                pass
            elif drawcombo == '1.5':
                pass
            elif drawcombo == '2.5':
                pass
            elif drawcombo == '3.5':
                pass
            elif drawcombo == '4.5':
                pass
                
            else:
                print("Error: Undefined combo at", position)

            self.combo.setFixedSize(120,100)
            self.combo.setIconSize(QSize(100,100))
            self.grid.addWidget(self.combo, *position)

            comboList['combo{0}'.format(position)] = position
            self.combo.currentIndexChanged.connect(
                    lambda ix, p=position: self.logChange(comboList['combo{0}'.format(p)]))
        self.grid.setColumnMinimumWidth(3, 150)


        # Final window stuff
        placeholder = QWidget()
        placeholder.setLayout(self.grid)

        # STOLEN CODE (this piece of stolen code sets a background, disabled because it causes lag)
        bg = QImage("absolver_deck_reviewer/background.png")
        sc_bg = bg.scaled(QSize(1200,800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sc_bg))                     # 10 = Windowrole (??? What does that even mean???)
        self.setPalette(palette)
        # END OF STOLEN CODE

        self.setCentralWidget(placeholder)
        self.setFixedSize(1200,800)
        self.setWindowTitle('Deck builder')
        self.centerOnScreen()
        self.show()
    def centerOnScreen (self):
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                    (resolution.height() / 2) - (self.frameSize().height() / 2))

    def logChange(self, currentCombo):
        print(str(currentCombo) + ' was changed')
        print(self.combos)
        
        changed_combo = self.grid.itemAtPosition(currentCombo[0], currentCombo[1])
        coords = currentCombo[0], currentCombo[1]+1
        adj_combo = self.grid.itemAtPosition(coords[0], coords[1])

        if(adj_combo and adj_combo.widget()):
            adj_combo.widget().deleteLater()
            print("Changed combo is" + self.combos[coords[0]])
        

    def get_json_data(self, count, drawcombo):
            count += 1
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
