# -*- coding: cp949 -*- 
import sys
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QPushButton, QFileDialog, QMessageBox, QLabel, QTextEdit
from PyQt5.QtGui import QIcon
from ui_ini_file_out import start


global ininame
ininame = None
global mapname
mapname = None
global savename
savename = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setGeometry(500, 500, 650, 500)  # x, y, w, h
        self.setWindowTitle('INI-Maker V1.01')

        # ---------- Menun bar add ---------------
        # Create new action INI Open
        iniopen_action = QAction(QIcon('ini.png'), '&INI Open', self)
        iniopen_action.setShortcut('Ctrl+I')
        iniopen_action.setStatusTip('INI File OPEN')
        iniopen_action.triggered.connect(self.ini_opencall)

        # Map Open new action
        mapopen_action = QAction(QIcon('map.png'), '&Map Open', self)
        mapopen_action.setShortcut('Ctrl+M')
        mapopen_action.setStatusTip('MAP File OPEN')
        mapopen_action.triggered.connect(self.map_opencall)

        savefile_action = QAction(QIcon('save.png'), '&Save File', self)
        savefile_action.setShortcut('Ctrl+S')
        savefile_action.setStatusTip('Save File Path')
        savefile_action.triggered.connect(self.savefile_call)

        # Exit action
        close_action = QAction(QIcon('close.png'), '&Exit', self)
        close_action.setShortcut('Ctrl+Q')
        close_action.setStatusTip('EXIT')
        close_action.triggered.connect(self.menu_closecall)

        # Info action
        info_action = QAction(QIcon('info.png'), '&Info', self)
        #info_action.setShortcut('Ctrl+Q')
        info_action.setStatusTip('Info')
        info_action.triggered.connect(self.menu_infocall)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(iniopen_action)
        file_menu.addAction(mapopen_action)
        file_menu.addAction(savefile_action)
        file_menu.addAction(close_action)

        file_menu = menu_bar.addMenu('&Info')
        file_menu.addAction(info_action)


        # ---------- Status bar add --------------
        # 화면에 상태바 추가
        status_bar = self.statusBar()
        self.setStatusBar(status_bar)

        # ---------- push button --------------
        # clicked 이벤트 발생 버튼
        self.pb_clicked = QPushButton('start', self)
        self.pb_clicked.setGeometry(10, 30, 150, 30)
        self.pb_clicked.clicked.connect(self.button_clicked)
        self.pb_clicked.setText('Start')
        self.disable_but(self.pb_clicked)

        # QLabel 설정
        self.pathLabel = QLabel('INI File Path : ', self)
        self.pathLabel.setGeometry(10, 60, 600, 50)

        self.pathLabe2 = QLabel('MAP File Path : ', self)
        self.pathLabe2.setGeometry(10, 80, 600, 50)

        self.pathLabe3 = QLabel('SAVE Path : ', self)
        self.pathLabe3.setGeometry(10, 100, 600, 50)

        # QTextEdit 파일 읽은 내용 표시
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(10, 150, 600, 300)

        # QDialog MessageBox 설정
        self.msg = QMessageBox()

    # ini open 함수 호출
    def ini_opencall(self):
        #print('ini call')
        global ininame 
        ininame = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'INI File(*.ini)')
        self.pathLabel.setText('INI File Path : '+ininame[0])
        if len(ininame[0]) == 0 :
            ininame = None
        self.button_set()

    
    # map open 함수 호출
    def map_opencall(self):
        #print('map call')      
        global mapname  
        mapname = QFileDialog.getOpenFileName(self, 'Open File', '',
                                            'MAP File(*.map)')
        self.pathLabe2.setText('MAP File Path : '+mapname[0])
        if len(mapname[0]) == 0 :
            mapname = None
        self.button_set()
        #print(mapname[0])

    # save file 함수 호출
    def savefile_call(self):
        #print('save open call')
        global savename
        savename = QFileDialog.getSaveFileName(self, 'Save File', '',
                                            'INI File(*.ini)')
        self.pathLabe3.setText('SAVE Path : '+savename[0])
        if len(savename[0]) == 0 :
            savename = None
        self.button_set()
        #print(savename[0])
    
    def menu_infocall(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('Info')
        self.msg.setText('Question: jadu9000142@rinnai.co.kr')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()
        #print('QMessageBox 리턴값 ', retval)
        if retval == QMessageBox.Ok :
            print('messagebox ok : ', retval)        

    # 윈도우 종료 함수 호출
    def menu_closecall(self):
        #print('exit menu call')
        sys.exit()

    # start button 함수 호출
    def button_clicked(self):
        #print('button_clicked')
        data, text = start(ininame[0], mapname[0], savename[0])

        self.textEdit.setText(str(data))
        self.textEdit.append(str(text))


        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('Finish!')
        self.msg.setText(str(text))
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
        #self.disable_but(self.pb_clicked)

    # disable button 함수 호출    
    def disable_but(self, vbutton):
        vbutton.setEnabled(False)

    # Enable button 함수 호출            
    def enable_but(self, vbutton):
        vbutton.setEnabled(True)

    # Enable button 활성화 조건 판단     
    def button_set(self) :
        if ininame is None or mapname is None or savename is None :
            self.disable_but(self.pb_clicked)
        else :
            self.enable_but(self.pb_clicked)
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())