import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class MyPyQT_Form(QtWidgets.QWidget):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

        # 基础
        self.basic_attack = 0
        self.basic_crit = 0

        # 现有装备
        self.item_attack = 0
        self.item_ab = 0
        self.item_crit = 0
        self.item_db = 0

        # 比较的装备1
        self.item1_ab = 0
        self.item1_crit = 0
        self.item1_db = 0

        # 比较的装备2
        self.item2_ab = 0
        self.item2_crit = 0
        self.item2_db = 0

        # 面板1
        self.final_attack = 0
        self.final_crit = 0
        self.final_db = 0

        # 勾选框初始值
        self.jing_crt = 0
        self.storm = 1
        self.storm1 = 1
        self.storm2 = 1

        # 1勾选框触发事件
        self.is_jing.stateChanged.connect(self.checkbox_value)
        self.item_storm.stateChanged.connect(self.checkbox_value)
        self.item1_storm.stateChanged.connect(self.checkbox_value)
        self.item2_storm.stateChanged.connect(self.checkbox_value)

        # 2勾选框触发事件
        self.battle5.stateChanged.connect(self.checkbox_battle)
        self.battle10.stateChanged.connect(self.checkbox_battle)
        self.battle20.stateChanged.connect(self.checkbox_battle)
        self.battle40.stateChanged.connect(self.checkbox_battle)
        self.battle100.stateChanged.connect(self.checkbox_battle)
        self.battle3000.stateChanged.connect(self.checkbox_battle)

        # 技能初始系数
        self.skill_bonus = 100

        self.final_attack = 0
        self.total_battle_ab = 0
        self.total_battle_att = 0

        # 2号装备初始值
        self.battle_add2 = 0
        self.item2_damage = 0
        self.item2_damage_crit = 0
        self.item2_skill = 0
        self.item2_skill_crit = 0

        self.battle_add1 = 0
        self.battle_add = 0
        self.item1_damage1 = 0
        self.item1_damage_crit1 = 0
        self.item1_skill1 = 0
        self.item1_skill_crit1 = 0
        self.item1_finalcrt = 0


        self.item2_attack = 0
        self.item2_finalcrt = 0
        self.item2_finaldb = 0

        self.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1037, 951)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(820, 920, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(100, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(100, 200, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(100, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(100, 230, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(100, 260, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(60, 420, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(60, 450, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(60, 480, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QtCore.QRect(20, 670, 991, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(760, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(560, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(560, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(560, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.item1_storm = QtWidgets.QCheckBox(Form)
        self.item1_storm.setGeometry(QtCore.QRect(690, 200, 21, 16))
        self.item1_storm.setText("")
        self.item1_storm.setObjectName("item1_storm")
        self.cals_2 = QtWidgets.QPushButton(Form)
        self.cals_2.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.cals_2.setObjectName("cals_2")
        self.cals_3 = QtWidgets.QPushButton(Form)
        self.cals_3.setGeometry(QtCore.QRect(50, 120, 181, 31))
        self.cals_3.setObjectName("cals_3")
        self.cals_4 = QtWidgets.QPushButton(Form)
        self.cals_4.setGeometry(QtCore.QRect(640, 10, 111, 41))
        self.cals_4.setObjectName("cals_4")
        self.cals_5 = QtWidgets.QPushButton(Form)
        self.cals_5.setGeometry(QtCore.QRect(780, 10, 111, 41))
        self.cals_5.setObjectName("cals_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 50, 81, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 80, 81, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 170, 81, 21))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 200, 81, 21))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 230, 81, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 260, 81, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(660, 80, 81, 21))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(660, 120, 81, 21))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(660, 160, 81, 21))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(790, 80, 81, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(790, 120, 81, 21))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(790, 160, 81, 21))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(150, 420, 181, 21))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(150, 450, 181, 21))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 480, 181, 21))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 370, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 630, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.is_jing = QtWidgets.QCheckBox(Form)
        self.is_jing.setGeometry(QtCore.QRect(90, 300, 121, 16))
        self.is_jing.setObjectName("is_jing")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(200, 300, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(220, 300, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(690, 230, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(560, 230, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.item2_storm = QtWidgets.QCheckBox(Form)
        self.item2_storm.setGeometry(QtCore.QRect(820, 200, 21, 16))
        self.item2_storm.setText("")
        self.item2_storm.setObjectName("item2_storm")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(820, 230, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(560, 200, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.item_storm = QtWidgets.QCheckBox(Form)
        self.item_storm.setGeometry(QtCore.QRect(90, 330, 121, 16))
        self.item_storm.setObjectName("item_storm")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(230, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(260, 330, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(570, 410, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(570, 380, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(660, 380, 81, 21))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(660, 410, 81, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(660, 440, 81, 21))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 290, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(570, 440, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(800, 380, 81, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(800, 410, 81, 21))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(Form)
        self.lineEdit_24.setGeometry(QtCore.QRect(800, 440, 81, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 630, 281, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(680, 350, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(820, 350, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.battle40 = QtWidgets.QCheckBox(Form)
        self.battle40.setGeometry(QtCore.QRect(310, 600, 71, 16))
        self.battle40.setObjectName("battle40")
        self.battle20 = QtWidgets.QCheckBox(Form)
        self.battle20.setGeometry(QtCore.QRect(230, 600, 71, 16))
        self.battle20.setObjectName("battle20")
        self.battle5 = QtWidgets.QCheckBox(Form)
        self.battle5.setGeometry(QtCore.QRect(60, 600, 71, 16))
        self.battle5.setObjectName("battle5")
        self.battle100 = QtWidgets.QCheckBox(Form)
        self.battle100.setGeometry(QtCore.QRect(380, 600, 81, 16))
        self.battle100.setObjectName("battle100")
        self.battle3000 = QtWidgets.QCheckBox(Form)
        self.battle3000.setGeometry(QtCore.QRect(530, 600, 81, 16))
        self.battle3000.setObjectName("battle3000")
        self.battle10 = QtWidgets.QCheckBox(Form)
        self.battle10.setGeometry(QtCore.QRect(150, 600, 51, 16))
        self.battle10.setObjectName("battle10")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 570, 1011, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(670, 600, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.battle_ab = QtWidgets.QLabel(Form)
        self.battle_ab.setGeometry(QtCore.QRect(740, 600, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.battle_ab.setFont(font)
        self.battle_ab.setObjectName("battle_ab")
        self.label_37 = QtWidgets.QLabel(Form)
        self.label_37.setGeometry(QtCore.QRect(780, 600, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.battle_att = QtWidgets.QLabel(Form)
        self.battle_att.setGeometry(QtCore.QRect(830, 600, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.battle_att.setFont(font)
        self.battle_att.setObjectName("battle_att")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 630, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 530, 141, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.skill = QtWidgets.QLineEdit(Form)
        self.skill.setGeometry(QtCore.QRect(200, 530, 81, 31))
        self.skill.setReadOnly(True)
        self.skill.setObjectName("skill")
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setGeometry(QtCore.QRect(500, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 630, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        self.cals_2.clicked.connect(Form.Basic)
        self.cals_3.clicked.connect(Form.Item)
        self.cals_4.clicked.connect(Form.Item1)
        self.cals_5.clicked.connect(Form.Item2)
        self.pushButton.clicked.connect(Form.cal)
        self.pushButton_2.clicked.connect(Form.cur_damage)
        self.pushButton_5.clicked.connect(Form.DIY_defense)
        self.pushButton_6.clicked.connect(Form.skill_factor)
        self.pushButton_3.clicked.connect(Form.compare)
        self.pushButton_4.clicked.connect(Form.damage_compare)
        self.pushButton_7.clicked.connect(Form.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "copyright @ 二次元肥宅Roger"))
        self.label_7.setText(_translate("Form", "1、基础攻击"))
        self.label_9.setText(_translate("Form", "1、装备攻击"))
        self.label_10.setText(_translate("Form", "2、攻击加成%"))
        self.label_12.setText(_translate("Form", "2、暴击伤害"))
        self.label_13.setText(_translate("Form", "3、暴击伤害%"))
        self.label_14.setText(_translate("Form", "4、伤害加成%"))
        self.label_18.setText(_translate("Form", "攻击"))
        self.label_19.setText(_translate("Form", "暴击伤害"))
        self.label_20.setText(_translate("Form", "伤害加成"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1000"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2000"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "4000"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "6000"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "8000"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "自定义防御"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1平砍"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2平砍"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "1暴击"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "2暴击"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "1技能"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "2技能"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "1技暴"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "2技暴"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "wdnmd"))
        self.label_22.setText(_translate("Form", "VS"))
        self.label_23.setText(_translate("Form", "攻击加成"))
        self.label_24.setText(_translate("Form", "暴击伤害"))
        self.label_25.setText(_translate("Form", "伤害加成"))
        self.cals_2.setText(_translate("Form", "一、输入基础属性"))
        self.cals_3.setText(_translate("Form", "二、输入所有装备的总属性"))
        self.cals_4.setText(_translate("Form", "六、现有装备"))
        self.cals_5.setText(_translate("Form", "对比装备"))
        self.pushButton.setText(_translate("Form", "三、面板计算"))
        self.pushButton_2.setText(_translate("Form", "五、现有装备伤害"))
        self.is_jing.setText(_translate("Form", " 5、是静吗？"))
        self.label_15.setText(_translate("Form", "0"))
        self.label_16.setText(_translate("Form", "%暴击伤害"))
        self.label_17.setText(_translate("Form", "1"))
        self.label_21.setText(_translate("Form", "爆伤倍数"))
        self.label_26.setText(_translate("Form", "1"))
        self.label_27.setText(_translate("Form", "是暴风套吗？"))
        self.item_storm.setText(_translate("Form", " 6、是暴风套吗？"))
        self.label_28.setText(_translate("Form", "1"))
        self.label_29.setText(_translate("Form", "爆伤倍数"))
        self.label_30.setText(_translate("Form", "暴击伤害"))
        self.label_31.setText(_translate("Form", "攻击"))
        self.pushButton_3.setText(_translate("Form", "七、面板比对"))
        self.label_32.setText(_translate("Form", "伤害加成"))
        self.pushButton_4.setText(_translate("Form", "八、对比装备伤害"))
        self.label_33.setText(_translate("Form", "1号装备"))
        self.label_34.setText(_translate("Form", "2号装备"))
        self.battle40.setText(_translate("Form", "40%"))
        self.battle20.setText(_translate("Form", "20%"))
        self.battle5.setText(_translate("Form", "萌王5%"))
        self.battle100.setText(_translate("Form", "精灵100%"))
        self.battle3000.setText(_translate("Form", "苍影3000"))
        self.battle10.setText(_translate("Form", "10%"))
        self.label.setText(_translate("Form", "---------------------------------------------------------------------------------------BUFF选择区域----------------------------------------------------------------------------------------------"))
        self.label_35.setText(_translate("Form", "总加成："))
        self.battle_ab.setText(_translate("Form", "0"))
        self.label_37.setText(_translate("Form", "%  +  "))
        self.battle_att.setText(_translate("Form", "0"))
        self.pushButton_5.setText(_translate("Form", "自定义防御"))
        self.pushButton_6.setText(_translate("Form", "四、技能伤害系数%"))
        self.label_36.setText(_translate("Form", "单件装备性价比："))
        self.pushButton_7.setText(_translate("Form", "清空表格"))

    # 暴击和静勾选框
    def checkbox_value(self):
        self.jing_crt = 25 if self.is_jing.isChecked() else 0
        self.storm = 1.5 if self.item_storm.isChecked() else 1
        self.storm1 = 1.5 if self.item1_storm.isChecked() else 1
        self.storm2 = 1.5 if self.item2_storm.isChecked() else 1

        self.label_15.setText(str(self.jing_crt))
        self.label_28.setText(str(self.storm))
        self.label_17.setText(str(self.storm1))
        self.label_26.setText(str(self.storm2))

    # buff勾选框
    def checkbox_battle(self):
        self.att_battle5 = 5 if self.battle5.isChecked() else 0
        self.att_battle10 = 10 if self.battle10.isChecked() else 0
        self.att_battle20 = 20 if self.battle20.isChecked() else 0
        self.att_battle40 = 40 if self.battle40.isChecked() else 0
        self.att_battle100 = 100 if self.battle100.isChecked() else 0
        self.att_battle3000 = 3000 if self.battle3000.isChecked() else 0

        self.total_battle_ab = self.att_battle5 + self.att_battle10 + self.att_battle20 + self.att_battle40 + self.att_battle100
        self.total_battle_att = self.att_battle3000

        self.battle_ab.setText(str(self.total_battle_ab))
        self.battle_att.setText(str(self.att_battle3000))

    # 一、
    def Basic(self):
        self.basic_attack, ok = QInputDialog.getInt(self, '请输入整数', '基础攻击：')  # 用量
        self.basic_crit, ok = QInputDialog.getInt(self, '请输入整数', '基础暴击伤害：')  # 用量
        self.lineEdit.setText(str(self.basic_attack))
        self.lineEdit_2.setText(str(self.basic_crit))

    # 二、总装备
    def Item(self):
        self.item_attack, ok = QInputDialog.getInt(self, '请输入整数', '装备攻击力：')  # 用量
        self.item_ab, ok = QInputDialog.getDouble(self, '请输入数字', '装备攻击加成(%)：')  # 用量
        self.item_crit, ok = QInputDialog.getDouble(self, '请输入数字', '装备暴击伤害(%)：')  # 用量
        self.item_db, ok = QInputDialog.getDouble(self, '请输入数字', '装备伤害加成(%)：')  # 用量

        self.lineEdit_3.setText(str(self.item_attack))
        self.lineEdit_4.setText(str(self.item_ab))
        self.lineEdit_5.setText(str(self.item_crit))
        self.lineEdit_6.setText(str(self.item_db))

    # 六、
    def Item1(self):
        self.item1_ab, ok = QInputDialog.getDouble(self, '装备1攻击加成', '请输入数字(%)：')  # 用量
        self.item1_crit, ok = QInputDialog.getDouble(self, '装备1暴击伤害', '请输入数字(%)：')  # 用量
        self.item1_db, ok = QInputDialog.getDouble(self, '装备1伤害加成', '请输入数字(%)：')  # 用量
        self.lineEdit_7.setText(str(self.item1_ab))
        self.lineEdit_8.setText(str(self.item1_crit))
        self.lineEdit_9.setText(str(self.item1_db))

    def Item2(self):
        self.item2_ab, ok = QInputDialog.getDouble(self, '装备1攻击加成', '请输入数字(%)：')  # 用量
        self.item2_crit, ok = QInputDialog.getDouble(self, '装备1暴击伤害', '请输入数字(%)：')  # 用量
        self.item2_db, ok = QInputDialog.getDouble(self, '装备1伤害加成', '请输入数字(%)：')  # 用量
        self.lineEdit_10.setText(str(self.item2_ab))
        self.lineEdit_11.setText(str(self.item2_crit))
        self.lineEdit_12.setText(str(self.item2_db))

    # 四
    def skill_factor(self):
        self.skill_bonus, ok = QInputDialog.getInt(self, '请输入整数', '输入技能伤害系数(%)：')
        self.skill.setText(str(self.skill_bonus))

    # 三、面板计算
    def cal(self):
        self.final_attack = self.basic_attack * (1 + self.item_ab / 100) + self.item_attack
        self.final_crit = (self.basic_crit + self.item_crit) * self.storm + self.jing_crt
        self.final_db = self.item_db

        self.lineEdit_13.setText(str(round(self.final_attack)))
        self.lineEdit_14.setText(str(self.final_crit))
        self.lineEdit_15.setText(str(self.final_db))

    # 五、
    def cur_damage(self):
        self.defense = [1000, 2000, 4000, 6000, 8000]
        for i in range(len(self.defense)):
            # attack defense difference = add，攻防差
            self.battle_add = int(self.final_attack * (1 + self.total_battle_ab / 100) - self.defense[i] + self.total_battle_att)

            self.item1_damage = int(self.battle_add * (1 + self.final_db / 100))
            self.item1_damage_crit = int(self.item1_damage * (1 + self.final_crit / 100))
            self.item1_skill = int(self.item1_damage) * (self.skill_bonus / 100)
            self.item1_skill_crit = int(self.item1_skill * (1 + self.final_crit / 100))

            self.pingkan = QTableWidgetItem(str(self.item1_damage))
            self.tableWidget.setItem(i, 0, self.pingkan)
            self.pingkanbao = QTableWidgetItem(str(self.item1_damage_crit))
            self.tableWidget.setItem(i, 2, self.pingkanbao)
            self.jineng = QTableWidgetItem(str(self.item1_skill))
            self.tableWidget.setItem(i, 4, self.jineng)
            self.jinengbao = QTableWidgetItem(str(self.item1_skill_crit))
            self.tableWidget.setItem(i, 6, self.jinengbao)

    def DIY_defense(self):
        self.your_DIY_defense, ok = QInputDialog.getInt(self, '请输入整数', '输入你想测试的对象的防御：')
        self.diy_d = str(self.your_DIY_defense) + "防御"

        self.zidingyi = QTableWidgetItem(str(self.diy_d))
        self.tableWidget.setItem(5, 8, self.zidingyi)

        # 1号装备
        self.battle_add = int(
            self.final_attack * (1 + self.total_battle_ab / 100) - self.your_DIY_defense + self.total_battle_att)

        self.item1_damage = int(self.battle_add * (1 + self.final_db / 100))
        self.item1_damage_crit = int(self.item1_damage * (1 + self.final_crit / 100))
        self.item1_skill = int(self.item1_damage) * (self.skill_bonus / 100)
        self.item1_skill_crit = int(self.item1_skill * (1 + self.final_crit / 100))

        self.pingkan = QTableWidgetItem(str(self.item1_damage))
        self.tableWidget.setItem(5, 0, self.pingkan)
        self.pingkanbao = QTableWidgetItem(str(self.item1_damage_crit))
        self.tableWidget.setItem(5, 2, self.pingkanbao)
        self.jineng = QTableWidgetItem(str(self.item1_skill))
        self.tableWidget.setItem(5, 4, self.jineng)
        self.jinengbao = QTableWidgetItem(str(self.item1_skill_crit))
        self.tableWidget.setItem(5, 6, self.jinengbao)

        # 2号装备，无则为0
        self.battle_add2 = int(
            self.item2_attack * (1 + self.total_battle_ab / 100) - self.your_DIY_defense + self.total_battle_att)

        self.item2_damage = int(self.battle_add2 * (1 + self.item2_finaldb / 100))
        self.item2_damage_crit = int(self.item2_damage * (1 + self.item2_finalcrt / 100))
        self.item2_skill = int(self.item2_damage) * (self.skill_bonus / 100)
        self.item2_skill_crit = int(self.item2_skill * (1 + self.item2_finalcrt / 100))

        self.pingkan2 = QTableWidgetItem(str(self.item2_damage))
        self.tableWidget.setItem(5, 1, self.pingkan2)
        self.pingkanbao2 = QTableWidgetItem(str(self.item2_damage_crit))
        self.tableWidget.setItem(5, 3, self.pingkanbao2)
        self.jineng2 = QTableWidgetItem(str(self.item2_skill))
        self.tableWidget.setItem(5, 5, self.jineng2)
        self.jinengbao2 = QTableWidgetItem(str(self.item2_skill_crit))
        self.tableWidget.setItem(5, 7, self.jinengbao2)

    # 七、
    def compare(self):
        # 来自三、的面板
        self.item1_finalcrt = (self.basic_crit + self.item_crit) * self.storm1 + self.jing_crt

        self.lineEdit_19.setText(str(round(self.final_attack)))
        self.lineEdit_20.setText(str(self.item1_finalcrt))
        self.lineEdit_21.setText(str(self.final_db))

        # 来自item2 - 减1加2
        self.item2_attack = self.basic_attack * (1 + (self.item_ab - self.item1_ab + self.item2_ab) / 100) + self.item_attack
        self.item2_finalcrt = (self.basic_crit + self.item_crit - self.item1_crit + self.item2_crit) * self.storm2 + self.jing_crt
        self.item2_finaldb = self.item_db - self.item1_db + self.item2_db

        self.lineEdit_22.setText(str(round(self.item2_attack)))
        self.lineEdit_23.setText(str(self.item2_finalcrt))
        self.lineEdit_24.setText(str(self.item2_finaldb))

    # 八、
    def damage_compare(self):
        self.defense = [1000, 2000, 4000, 6000, 8000]
        for i in range(len(self.defense)):
            # 装备1
            self.battle_add1 = int(self.final_attack * (1 + self.total_battle_ab / 100) - self.defense[i] + self.total_battle_att)

            self.item1_damage1 = int(self.battle_add1 * (1 + self.final_db / 100))
            self.item1_damage_crit1 = int(self.item1_damage1 * (1 + self.item1_finalcrt / 100))
            self.item1_skill1 = int(self.item1_damage1) * (self.skill_bonus / 100)
            self.item1_skill_crit1 = int(self.item1_skill1 * (1 + self.item1_finalcrt / 100))

            self.pingkan1 = QTableWidgetItem(str(self.item1_damage1))
            self.tableWidget.setItem(i, 0, self.pingkan1)
            self.pingkanbao1 = QTableWidgetItem(str(self.item1_damage_crit1))
            self.tableWidget.setItem(i, 2, self.pingkanbao1)
            self.jineng1 = QTableWidgetItem(str(self.item1_skill1))
            self.tableWidget.setItem(i, 4, self.jineng1)
            self.jinengbao1 = QTableWidgetItem(str(self.item1_skill_crit1))
            self.tableWidget.setItem(i, 6, self.jinengbao1)

            # attack defense difference = add，攻防差
            self.battle_add2 = int(
                self.item2_attack * (1 + self.total_battle_ab / 100) - self.defense[i] + self.total_battle_att)

            self.item2_damage = int(self.battle_add2 * (1 + self.item2_finaldb / 100))
            self.item2_damage_crit = int(self.item2_damage * (1 + self.item2_finalcrt / 100))
            self.item2_skill = int(self.item2_damage) * (self.skill_bonus / 100)
            self.item2_skill_crit = int(self.item2_skill * (1 + self.item2_finalcrt / 100))

            # 装备2数据
            self.pingkan2 = QTableWidgetItem(str(self.item2_damage))
            self.tableWidget.setItem(i, 1, self.pingkan2)
            self.pingkanbao2 = QTableWidgetItem(str(self.item2_damage_crit))
            self.tableWidget.setItem(i, 3, self.pingkanbao2)
            self.jineng2 = QTableWidgetItem(str(self.item2_skill))
            self.tableWidget.setItem(i, 5, self.jineng2)
            self.jinengbao2 = QTableWidgetItem(str(self.item2_skill_crit))
            self.tableWidget.setItem(i, 7, self.jinengbao2)

    # 清空
    def clear(self):
        self.tableWidget.clearContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MyPyQT_Form()
    demo.show()
    sys.exit(app.exec_())