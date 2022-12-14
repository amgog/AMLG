# -*- coding: utf-8 -*-
import copy

import numpy as np

# Form implementation generated from reading ui file 'result1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import readdata, classify
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

# path = "D:\pycharm\project\pythonProject\四类数据477.xlsx"
# ab = readdata.read_excel_file(path, 'Sheet1')
# # asam = readdata.sum_excel_file(ab)


global coldata, testdata, dataset, a, t, r, c, method, dic, cldic
# t = 10
c = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
tt = {
    'svm': ['kernal', 'decision_function_shape', 'degree', 'coef0', 'gamma', 'C', 'tol', '参数8', '参数9'],
    'dct': ['criterion', 'splitter', 'max_leaf_nodes', 'max_depth', 'min_impurity_decrease', 'min_samples_split',
            'min_samples_leaf', 'random_state', '参数9'],
    'ada': ['algorithm','base_estimator','n_estimators','learning_rate','random_state','参数6','参数7','参数8','参数9'],
    'ran': ['criterion','bootstrap','max_depth','min_samples_leaf','min_samples_split','max_features',
            'max_leaf_nodes','n_estimators','参数9']
}
ttl = {
    'svm':[['rbf','linear','poly','sigmoid'], ['ovo','ovr'],'3','0','auto','1','0.001','',''],
    'dct':[['gini','entropy'],['best','random'],'None','None','0','2','1','None',''],
    'ran':[['gini','entropy'],['True','False'],'1','1','2','None','None','100',''],
    'ada':[['SAMME','SAMME.R'],['None'],'50','1','None','','','','']
}

# r = ['80','10','10']
coldata = {}
dic = {}
pr = ['总体精确率', '训练精确率', '测试精确率', '验证精确率']
rr = ['总体召回率', '训练召回率', '测试召回率', '验证召回率']
prc = ['分类总体精确率', '分类训练精确率', '分类测试精确率', '分类验证精确率']
rrc = ['分类总体召回率', '分类训练召回率', '分类测试召回率', '分类验证召回率']


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]


class Ui_Dialog(QtWidgets.QMainWindow):
    signal2 = QtCore.pyqtSignal(dict)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 750)
        self.signal2.connect(self.print_val)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 20, 240, 170))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.cb2 = QtWidgets.QComboBox(Dialog)
        self.cb2.setGeometry(QtCore.QRect(430, 85, 90, 25))
        self.cb2.setObjectName("cb2")
        self.cs2 = QtWidgets.QLabel(Dialog)
        self.cs2.setGeometry(QtCore.QRect(430, 50, 95, 25))
        self.cs2.setAlignment(QtCore.Qt.AlignCenter)
        self.cs2.setObjectName("cs2")
        self.cb3 = QtWidgets.QTextEdit(Dialog)
        self.cb3.setGeometry(QtCore.QRect(540, 85, 90, 25))
        self.cb3.setObjectName("cb3")
        self.cs4 = QtWidgets.QLabel(Dialog)
        self.cs4.setGeometry(QtCore.QRect(650, 50, 90, 25))
        self.cs4.setAlignment(QtCore.Qt.AlignCenter)
        self.cs4.setObjectName("cs4")
        self.cb4 = QtWidgets.QTextEdit(Dialog)
        self.cb4.setGeometry(QtCore.QRect(650, 85, 90, 25))
        self.cb4.setObjectName("cb4")
        self.cs3 = QtWidgets.QLabel(Dialog)
        self.cs3.setGeometry(QtCore.QRect(540, 50, 90, 25))
        self.cs3.setAlignment(QtCore.Qt.AlignCenter)
        self.cs3.setObjectName("cs3")
        self.cb5 = QtWidgets.QTextEdit(Dialog)
        self.cb5.setGeometry(QtCore.QRect(760, 85, 90, 25))
        self.cb5.setObjectName("cb5")
        self.cs5 = QtWidgets.QLabel(Dialog)
        self.cs5.setGeometry(QtCore.QRect(760, 50, 90, 25))
        self.cs5.setAlignment(QtCore.Qt.AlignCenter)
        self.cs5.setObjectName("cs5")
        self.cb1 = QtWidgets.QComboBox(Dialog)
        self.cb1.setGeometry(QtCore.QRect(320, 85, 90, 25))
        self.cb1.setObjectName("cb1")
        self.cs1 = QtWidgets.QLabel(Dialog)
        self.cs1.setGeometry(QtCore.QRect(320, 50, 90, 25))
        self.cs1.setAlignment(QtCore.Qt.AlignCenter)
        self.cs1.setObjectName("cs1")
        self.cs9 = QtWidgets.QLabel(Dialog)
        self.cs9.setGeometry(QtCore.QRect(650, 125, 90, 25))
        self.cs9.setAlignment(QtCore.Qt.AlignCenter)
        self.cs9.setObjectName("cs9")
        self.cb8 = QtWidgets.QTextEdit(Dialog)
        self.cb8.setGeometry(QtCore.QRect(540, 160, 90, 25))
        self.cb8.setObjectName("cb8")
        self.tim = QtWidgets.QLabel(Dialog)
        self.tim.setGeometry(QtCore.QRect(760, 125, 90, 25))
        self.tim.setAlignment(QtCore.Qt.AlignCenter)
        self.tim.setObjectName("tim")
        self.cb7 = QtWidgets.QTextEdit(Dialog)
        self.cb7.setGeometry(QtCore.QRect(430, 160, 90, 25))
        self.cb7.setObjectName("cb7")
        self.cs7 = QtWidgets.QLabel(Dialog)
        self.cs7.setGeometry(QtCore.QRect(430, 125, 95, 25))
        self.cs7.setAlignment(QtCore.Qt.AlignCenter)
        self.cs7.setObjectName("cs7")
        self.cs6 = QtWidgets.QLabel(Dialog)
        self.cs6.setGeometry(QtCore.QRect(320, 125, 90, 25))
        self.cs6.setAlignment(QtCore.Qt.AlignCenter)
        self.cs6.setObjectName("cs6")
        self.cb6 = QtWidgets.QTextEdit(Dialog)
        self.cb6.setGeometry(QtCore.QRect(320, 160, 90, 25))
        self.cb6.setObjectName("cb6")
        self.cs8 = QtWidgets.QLabel(Dialog)
        self.cs8.setGeometry(QtCore.QRect(540, 125, 90, 25))
        self.cs8.setAlignment(QtCore.Qt.AlignCenter)
        self.cs8.setObjectName("cs8")
        self.cb9 = QtWidgets.QTextEdit(Dialog)
        self.cb9.setGeometry(QtCore.QRect(650, 160, 90, 25))
        self.cb9.setObjectName("cb9")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(50, 210, 80, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 210, 80, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 250, 800, 130))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(50, 400, 800, 280))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 800, 250))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 800, 250))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.openfile = QtWidgets.QToolButton(Dialog)
        self.openfile.setGeometry(QtCore.QRect(50, 690, 150, 30))
        self.openfile.setMouseTracking(False)
        self.openfile.setCheckable(True)
        self.openfile.setObjectName("openfile")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 690, 60, 30))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(340, 690, 60, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 690, 60, 30))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(490, 690, 60, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(570, 690, 60, 30))
        self.label_3.setObjectName("label_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(640, 690, 60, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(720, 690, 60, 30))
        self.label_4.setObjectName("label_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(790, 690, 60, 30))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(320, 20, 200, 25))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(520, 20, 90, 25))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(640, 20, 90, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(760, 20, 90, 25))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(620, 20, 10, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(740, 20, 10, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.algorithm1 = QtWidgets.QToolButton(Dialog)
        self.algorithm1.setGeometry(QtCore.QRect(700, 210, 150, 20))
        self.algorithm1.setMouseTracking(False)
        self.algorithm1.setCheckable(True)
        self.algorithm1.setObjectName("algorithm1")
        self.algorithm1.clicked.connect(self.alg_go)
        self.record = QtWidgets.QToolButton(Dialog)
        self.record.setGeometry(QtCore.QRect(510, 210, 150, 20))
        self.record.setMouseTracking(False)
        self.record.setCheckable(True)
        self.record.setObjectName("record")
        self.record.clicked.connect(self.data_record)
        self.plot = QtWidgets.QToolButton(Dialog)
        self.plot.setGeometry(QtCore.QRect(320, 210, 150, 20))
        self.plot.setMouseTracking(False)
        self.plot.setCheckable(True)
        self.plot.setObjectName('plot')
        # self.record.clicked.connect(self.detail_data)
        self.tim10 = QtWidgets.QLineEdit(Dialog)
        self.tim10.setGeometry(QtCore.QRect(760, 160, 90, 25))
        self.tim10.setObjectName("tim10")

        self.tableWidget_2.itemClicked.connect(self.detail_data)
        self.checkBox.setChecked(True)
        self.checkBox.clicked.connect(self.score_val)
        self.checkBox_2.clicked.connect(self.score_val_2)
        self.plot.clicked.connect(self.plot_pic)

        self.tabWidget.setCurrentIndex(1)

        self.series_1 = QtChart.QLineSeries()
        self.series_1.setName('总体')
        self.series_2 = QtChart.QLineSeries()
        self.series_2.setName('训练')
        self.series_3 = QtChart.QLineSeries()
        self.series_3.setName('测试')
        self.series_4 = QtChart.QLineSeries()
        self.series_4.setName('验证')
        self.x_value = QtChart.QValueAxis()
        self.y_value = QtChart.QValueAxis()
        self.charView = QtChart.QChartView()

        self.y_value.setRange(0.00, 1.00)
        self.charView.chart().setAxisY(self.y_value)  # 设置y轴属性
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "结果调优"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "总体"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "训练"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "测试"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "验证"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "精确率"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "召回率"))
        self.cs2.setText(_translate("Dialog", "参数1"))
        self.cs4.setText(_translate("Dialog", "参数1"))
        self.cs3.setText(_translate("Dialog", "参数1"))
        self.cs5.setText(_translate("Dialog", "参数1"))
        self.cs1.setText(_translate("Dialog", "参数1"))
        self.cs9.setText(_translate("Dialog", "参数1"))
        self.tim.setText(_translate("Dialog", "次数"))
        self.cs7.setText(_translate("Dialog", "参数1"))
        self.cs6.setText(_translate("Dialog", "参数1"))
        self.cs8.setText(_translate("Dialog", "参数1"))
        self.checkBox.setText(_translate("Dialog", "精确率"))
        self.checkBox_2.setText(_translate("Dialog", "召回率"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "总体"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "训练"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "测试"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "验证"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "总体"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "训练"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "测试"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "验证"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "总体"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "训练"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "测试"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "验证"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
        self.openfile.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "总体最优："))
        self.label_2.setText(_translate("Dialog", "训练最优："))
        self.label_3.setText(_translate("Dialog", "测试最优："))
        self.label_4.setText(_translate("Dialog", "验证最优："))
        self.label_21.setText(_translate("Dialog", "训练：测试：验证"))
        self.label_5.setText(_translate("Dialog", "："))
        self.label_6.setText(_translate("Dialog", "："))
        self.algorithm1.setText(_translate("Dialog", "确定"))
        self.record.setText(_translate("Dialog", "记录"))
        self.plot.setText(_translate("Dialog", "画图"))

    def show_init(self):
        global a, dataset
        # self.signal2.connect(self.print_val)
        a = readdata.sum_excel_file(dataset)
        self.cb1.clear()
        self.cb2.clear()
        self.cb1.addItems(ttl[method][0])
        self.cb2.addItems(ttl[method][1])
        self.cs2.setText(tt[method][1])
        self.cs4.setText(tt[method][3])
        self.cs3.setText(tt[method][2])
        self.cs5.setText(tt[method][4])
        self.cs1.setText(tt[method][0])
        self.cs9.setText(tt[method][8])
        self.cs7.setText(tt[method][6])
        self.cs6.setText(tt[method][5])
        self.cs8.setText(tt[method][7])
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.clearContents()
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.clearContents()
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.clearContents()
        self.textEdit.setText(r[0])
        self.textEdit_2.setText(r[1])
        self.textEdit_3.setText(r[2])
        self.cb3.setText(c[2])
        self.cb4.setText(c[3])
        self.cb5.setText(c[4])
        self.cb6.setText(c[5])
        self.cb7.setText(ttl[method][6])
        self.cb8.setText(ttl[method][7])
        self.cb9.setText(ttl[method][8])
        # if method == 'ada':
        #     self.cb9.clear()
        #     self.cb9.addItems(ttl[method][8])
        # # self.cb9.addItems[]
        self.tim10.setText(str(t))
        self.charView.chart().addSeries(self.series_1)
        self.charView.chart().addSeries(self.series_2)
        self.charView.chart().addSeries(self.series_3)
        self.charView.chart().addSeries(self.series_4)
        self.series_1.attachAxis(self.y_value)
        self.series_2.attachAxis(self.y_value)
        self.series_3.attachAxis(self.y_value)
        self.series_4.attachAxis(self.y_value)
        global coldata
        coldata = {}
        self.alg_go()

    def alg_go(self):
        global dataset, method
        k = [self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText()]
        coef = [self.cb1.currentText(), self.cb2.currentText(), self.cb3.toPlainText(),
                self.cb4.toPlainText(), self.cb5.toPlainText(), self.cb6.toPlainText(),
                self.cb7.toPlainText(), self.cb8.toPlainText(), self.cb9.toPlainText()]
        a = {
            'method': method,
            'sample_divi': k,
            'times': self.tim10.text(),
            'coef': coef
        }
        p = int(self.tim10.text())
        fdata = classify.algo_times(dataset, a['coef'], a['sample_divi'], p, a['method'], dic, cldic)
        for i in range(len(pr)):
            prp = np.array(fdata[pr[i]])
            prp = np.mean(prp)
            rrp = np.array(fdata[rr[i]])
            rrp = np.mean(rrp)
            item = QtWidgets.QTableWidgetItem("{:.2f}".format(prp))
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem("{:.2f}".format(rrp) + '*')
            self.tableWidget.setItem(i, 1, item)
        global testdata
        testdata = copy.deepcopy(fdata)

    def data_record(self):
        # k = [self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText()]
        # coef = [self.cb1.currentText(), self.cb2.currentText(), self.cb3.currentText(),
        #         self.cb3.currentText(), self.cb4.currentText(), self.cb6.currentText(),
        #         self.cb7.currentText(), self.cb8.currentText(), self.cb9.currentText()]
        # # a = {
        # #     'method': 'dct',
        # #     'sample_divi': k,
        # #     'times': self.tim10.text(),
        # #     'coef': coef
        # # }
        p = int(self.tim10.text())
        global testdata
        fdata = testdata
        #
        # pr = ['总体精确率','训练精确率','测试精确率','验证精确率']
        # rr = ['总体召回率','训练召回率','测试召回率','验证召回率']
        ap = self.tableWidget_2.columnCount()
        self.tableWidget_2.insertColumn(ap)
        if self.checkBox.checkState() == 2:
            for i in range(len(pr)):
                prp = np.array(fdata[pr[i]])
                prp = np.mean(prp)
                item = QtWidgets.QTableWidgetItem("{:.2f}".format(prp))
                self.tableWidget_2.setItem(i, ap, item)
        elif self.checkBox_2.checkState() == 2:
            for i in range(len(pr)):
                rrp = np.array(fdata[rr[i]])
                rrp = np.mean(rrp)
                item = QtWidgets.QTableWidgetItem("{:.2f}".format(rrp) + '*')
                self.tableWidget_2.setItem(i, ap, item)
        global coldata
        coldata[str(ap)] = copy.deepcopy(fdata)
        coldata[str(ap) + 'p'] = copy.deepcopy(p)

    def detail_data(self, Item=None):

        if Item == None:
            return
        ak = Item.column()
        global coldata
        # k = [self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText()]
        # coef = [self.cb1.currentText(), self.cb2.currentText(), self.cb3.currentText(),
        #         self.cb3.currentText(), self.cb4.currentText(), self.cb6.currentText(),
        #         self.cb7.currentText(), self.cb8.currentText(), self.cb9.currentText()]
        # a = {
        #     'method': 'dct',
        #     'sample_divi': k,
        #     'times': self.tim10.text(),
        #     'coef': coef
        # }

        # rdata = classify.svm_classify(ab,a['coef'],a['sample_divi'])
        p = coldata[str(ak) + 'p']
        # self.tableWidget_3.setColumnCount(p)
        # if self.checkBox.checkState() == 2:
        #     for i in range(len(pr)):
        #         for j in range(p):
        #             item = QtWidgets.QTableWidgetItem("{:.2f}".format(rdata[pr[i]]))
        #             self.tableWidget_3.setItem(i, j, item)
        # elif self.checkBox_2.checkState() == 2:
        #     for i in range(len(pr)):
        #         for j in range(p):
        #             item = QtWidgets.QTableWidgetItem("{:.2f}".format(rdata[rr[i]]))
        #             self.tableWidget_3.setItem(i, j, item)

        # fdata = classify.algo_times(ab,coldata[str(ak) + '系数'],coldata[str(ak) + '比例'],p,'dct')
        fdata = coldata[str(ak)]
        optbest = []
        cc = a['class_num']
        title_1 = range(1, p + 1)
        title_1 = list(map(str, title_1))
        title_1 = title_1 * 2
        title_2 = a['class_name'] * p * 2
        title_2 = list(map(str, title_2))
        self.tableWidget_3.setColumnCount(p * 2)
        self.tableWidget_3.setHorizontalHeaderLabels(title_1)
        for name in range(len(pr)):
            ap = np.array(fdata[pr[name]])
            # cn = int(np.argmax(ap)%cc)
            # optbest += get_keys(dic,cn)
            for i in range(0, p):
                item = QtWidgets.QTableWidgetItem("{:.2f}".format(ap[i * cc]))
                # 4是类数目
                self.tableWidget_3.setItem(name, i, item)
        for name in range(len(rr)):
            ap = np.array(fdata[rr[name]])
            # cn = int(np.argmax(ap)%cc)
            # optbest += get_keys(dic,cn)
            for i in range(0, p):
                item = QtWidgets.QTableWidgetItem("{:.2f}".format(ap[i * cc]) + '*')
                self.tableWidget_3.setItem(name, i + p, item)
        self.tableWidget_4.setColumnCount(p * cc * 2)
        self.tableWidget_4.setHorizontalHeaderLabels(title_2)
        for name in range(len(prc)):
            ap = np.array(fdata[prc[name]])
            cn = int(np.argmax(ap) % cc)
            optbest += get_keys(dic, cn)
            for i in range(0, p * cc):
                item = QtWidgets.QTableWidgetItem("{:.2f}".format(ap[i]))
                # 4是类数目
                self.tableWidget_4.setItem(name, i, item)
        for name in range(len(rrc)):
            ap = np.array(fdata[rrc[name]])
            cn = int(np.argmax(ap) % cc)
            optbest += get_keys(dic, cn)
            for i in range(0, p * cc):
                item = QtWidgets.QTableWidgetItem("{:.2f}".format(ap[i]) + '*')
                self.tableWidget_4.setItem(name, i + (p * cc), item)
        self.textBrowser.setText(str(optbest[0]) + '/' + str(optbest[4]) + '*')
        self.textBrowser_2.setText(str(optbest[1]) + '/' + str(optbest[5]) + '*')
        self.textBrowser_3.setText(str(optbest[2]) + '/' + str(optbest[6]) + '*')
        self.textBrowser_4.setText(str(optbest[3]) + '/' + str(optbest[7]) + '*')

    def score_val(self, Item=None):
        if Item == None:
            return
        global coldata
        ap = self.tableWidget_2.columnCount()
        if Item:
            self.checkBox_2.setCheckState(0)
            for j in range(ap):
                for i in range(len(pr)):
                    prp = np.array(coldata[str(j)][pr[i]])
                    prp = np.mean(prp)
                    item = QtWidgets.QTableWidgetItem("{:.2f}".format(prp))
                    self.tableWidget_2.setItem(i, j, item)
        elif Item == False:
            self.checkBox_2.setChecked(2)
            for j in range(ap):
                for i in range(len(pr)):
                    rrp = np.array(coldata[str(j)][rr[i]])
                    rrp = np.mean(rrp)
                    item = QtWidgets.QTableWidgetItem("{:.2f}".format(rrp) + '*')
                    self.tableWidget_2.setItem(i, j, item)

    def score_val_2(self, Item=None):
        if Item == None:
            return
        global coldata
        ap = self.tableWidget_2.columnCount()
        if Item:
            self.checkBox.setCheckState(0)
            for j in range(ap):
                for i in range(len(pr)):
                    rrp = np.array(coldata[str(j)][rr[i]])
                    rrp = np.mean(rrp)
                    item = QtWidgets.QTableWidgetItem("{:.2f}".format(rrp) + '*')
                    self.tableWidget_2.setItem(i, j, item)
        elif Item == False:
            self.checkBox.setChecked(2)
            for j in range(ap):
                for i in range(len(pr)):
                    prp = np.array(coldata[str(j)][pr[i]])
                    prp = np.mean(prp)
                    item = QtWidgets.QTableWidgetItem("{:.2f}".format(prp))
                    self.tableWidget_2.setItem(i, j, item)

    def print_val(self, val):
        global dataset, t, r, c, method, dic,cldic
        dataset = val['dataset']
        t = val['times']
        r = val['sample_divi']
        c = val['coef']
        method = val['method']
        dic = val['dic']
        cldic = val['cldic']
        self.show_init()

    def plot_pic(self):
        k = self.tableWidget_2.columnCount()
        self.charView.setGeometry(QtCore.QRect(650, 650, 1000, 600))
        self.charView.chart().removeAllSeries()
        self.series_1 = QtChart.QLineSeries()
        self.series_1.setName('总体')
        self.series_2 = QtChart.QLineSeries()
        self.series_2.setName('训练')
        self.series_3 = QtChart.QLineSeries()
        self.series_3.setName('测试')
        self.series_4 = QtChart.QLineSeries()
        self.series_4.setName('验证')
        self.x_value = QtChart.QValueAxis()
        self.y_value = QtChart.QValueAxis()
        self.y_value.setRange(0.00, 1.00)
        self.charView.chart().setAxisY(self.y_value)  # 设置y轴属性
        if self.checkBox.checkState() == 2:
            for i in range(k):
                v1 = float(self.tableWidget_2.item(0, i).text())
                self.series_1.append(float(i), v1)
                v2 = float(self.tableWidget_2.item(1, i).text())
                self.series_2.append(float(i), v2)
                v3 = float(self.tableWidget_2.item(2, i).text())
                self.series_3.append(float(i), v3)
                v4 = float(self.tableWidget_2.item(3, i).text())
                self.series_4.append(float(i), v4)
            self.x_value.setRange(1, k)
            self.charView.chart().addSeries(self.series_1)
            self.charView.chart().addSeries(self.series_2)
            self.charView.chart().addSeries(self.series_3)
            self.charView.chart().addSeries(self.series_4)
            self.series_1.attachAxis(self.y_value)
            self.series_2.attachAxis(self.y_value)
            self.series_3.attachAxis(self.y_value)
            self.series_4.attachAxis(self.y_value)
            self.charView.chart().setAxisX(self.x_value)
            self.charView.chart().axisX().setTickCount(k)
            self.charView.chart().setTitle('精确率')
            self.charView.show()

        elif self.checkBox_2.checkState() == 2:
            for i in range(k):
                v1 = float(self.tableWidget_2.item(0, i).text().replace('*', ''))
                self.series_1.append(float(i), v1)
                v2 = float(self.tableWidget_2.item(1, i).text().replace('*', ''))
                self.series_2.append(float(i), v2)
                v3 = float(self.tableWidget_2.item(2, i).text().replace('*', ''))
                self.series_3.append(float(i), v3)
                v4 = float(self.tableWidget_2.item(3, i).text().replace('*', ''))
                self.series_4.append(float(i), v4)
            self.x_value.setRange(1, k)
            self.charView.chart().addSeries(self.series_1)
            self.charView.chart().addSeries(self.series_2)
            self.charView.chart().addSeries(self.series_3)
            self.charView.chart().addSeries(self.series_4)
            self.series_1.attachAxis(self.y_value)
            self.series_2.attachAxis(self.y_value)
            self.series_3.attachAxis(self.y_value)
            self.series_4.attachAxis(self.y_value)
            self.charView.chart().setAxisX(self.x_value)
            self.charView.chart().axisX().setTickCount(k)
            self.charView.chart().setTitle('召回率')
            self.charView.show()

        # # coldata[str(ap)] = copy.deepcopy(fdata)
        # # coldata[str(ap)+'p'] = copy.deepcopy(p)
        #     for j in range(ap):
        #         for i in range(len(pr)):
        #             prp = np.array(coldata[str(j)][pr[i]])
        #             prp = np.mean(prp)
        #             item = QtWidgets.QTableWidgetItem("{:.2f}".format(prp))
        #             self.tableWidget_2.setItem(i, ap, item)
        # elif self.checkBox_2.checkState() == 2:
        #     self.checkBox.setCheckState(0)
        #     # for i in range(len(pr)):
        #     #     rrp = np.array(fdata[rr[i]])
        #     #     rrp = np.mean(rrp)
        #     #     item = QtWidgets.QTableWidgetItem("{:.2f}".format(rrp)+'*')
        #     #     self.tableWidget_2.setItem(i, ap, item)

    # def score_val_2(self,Item = None):
    #     if Item == None:
    #         return
    #     global coldata
    #     ap = self.tableWidget_2.columnCount()
    #     if Item:
    #         self.checkBox_2.setChecked(0)
    #         for j in range(ap):
    #             for i in range(len(pr)):
    #                 prp = np.array(coldata[str(j)][pr[i]])
    #                 prp = np.mean(prp)
    #                 item = QtWidgets.QTableWidgetItem("{:.2f}".format(prp))
    #                 self.tableWidget_2.setItem(i, ap, item)
