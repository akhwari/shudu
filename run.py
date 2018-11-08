from PyQt4 import QtCore, QtGui
from shudu import Ui_Dialog
from sudoku import *


shudu = [['' for i in range(9)] for i in range(9)]

# inherit QDialog class
class QDlgXXX(QtGui.QDialog):
    def __init__(self):
        super(QDlgXXX, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(self.ui.tableWidget.columnCount()):
                item = QtGui.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)
        self.ui.pushButton_2.clicked.connect(self.btnclkClear)
        self.ui.pushButton_3.clicked.connect(self.btnclkCalculate)
        self.ui.tableWidget.itemChanged.connect(self.itemchg)
        self.ui.comboBox.activated.connect(self.comboxact)

    def btnclkClear(self):
        self.ui.tableWidget.itemChanged.disconnect()
        for i in range(9):
            for j in range(9):
                shudu[i][j] = ''
                self.ui.tableWidget.item(i, j).setText('')
        prt_9x9(shudu)
        self.ui.tableWidget.itemChanged.connect(self.itemchg)

    def btnclkCalculate(self):
        self.ui.tableWidget.itemChanged.disconnect()
        calculate(shudu)
        for i in range(9):
            for j in range(9):
                self.ui.tableWidget.item(i, j).setText(shudu[i][j])
        self.ui.tableWidget.itemChanged.connect(self.itemchg)

    def itemchg(self, item=None):
        r = item.row()
        c = item.column()
        t = str(item.text())
        if t in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            shudu[r][c] = t
            if chk_1x1(shudu, r, c) == 'NNN':
                shudu[r][c] = ''
                item.setText('')
        else:
            shudu[r][c] = ''
            item.setText('')
        prt_9x9(shudu)

    def comboxact(self, index):
        self.ui.tableWidget.itemChanged.disconnect()
        for i in range(9):
            for j in range(9):
                if index == 0:
                    shudu[i][j] = shudu3[i][j]
                elif index == 1:
                    shudu[i][j] = shudu4[i][j]
                elif index == 2:
                    shudu[i][j] = shudu5[i][j]
                elif index == 3:
                    shudu[i][j] = shudu6[i][j]
                elif index == 4:
                    shudu[i][j] = shudu7[i][j]
                elif index == 5:
                    shudu[i][j] = shudu8[i][j]
                elif index == 6:
                    shudu[i][j] = shudu9[i][j]
                else:
                    shudu[i][j] = ''
                self.ui.tableWidget.item(i, j).setText(shudu[i][j])
        prt_9x9(shudu)
        self.ui.tableWidget.itemChanged.connect(self.itemchg)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QDlgXXX()
    Dialog.show()
    sys.exit(app.exec_())


