# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/kmol-editor/core/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 688)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/kmol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.h_splitter = QtWidgets.QSplitter(self.centralWidget)
        self.h_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.h_splitter.setObjectName("h_splitter")
        self.v_splitter = QtWidgets.QSplitter(self.h_splitter)
        self.v_splitter.setOrientation(QtCore.Qt.Vertical)
        self.v_splitter.setObjectName("v_splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.v_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.highlighter_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.highlighter_label.setObjectName("highlighter_label")
        self.horizontalLayout.addWidget(self.highlighter_label)
        self.highlighter_option = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.highlighter_option.setObjectName("highlighter_option")
        self.highlighter_option.addItem("")
        self.highlighter_option.addItem("")
        self.highlighter_option.addItem("")
        self.horizontalLayout.addWidget(self.highlighter_option)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exec_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exec_button.setObjectName("exec_button")
        self.horizontalLayout.addWidget(self.exec_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tree_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_widget.setObjectName("tree_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tree_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree_main = QtWidgets.QTreeWidget(self.tree_widget)
        self.tree_main.setDragEnabled(True)
        self.tree_main.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tree_main.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tree_main.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tree_main.setObjectName("tree_main")
        self.verticalLayout_2.addWidget(self.tree_main)
        self.verticalLayout.addWidget(self.tree_widget)
        self.panel_widget = QtWidgets.QTabWidget(self.v_splitter)
        self.panel_widget.setObjectName("panel_widget")
        self.console_tab = QtWidgets.QWidget()
        self.console_tab.setObjectName("console_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.console_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.console = QtWidgets.QTextBrowser(self.console_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setObjectName("console")
        self.verticalLayout_3.addWidget(self.console)
        self.panel_widget.addTab(self.console_tab, "")
        self.find_tab = QtWidgets.QWidget()
        self.find_tab.setObjectName("find_tab")
        self.panel_widget.addTab(self.find_tab, "")
        self.deprecated_tab = QtWidgets.QWidget()
        self.deprecated_tab.setObjectName("deprecated_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.deprecated_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deprecated_label = QtWidgets.QLabel(self.deprecated_tab)
        self.deprecated_label.setObjectName("deprecated_label")
        self.horizontalLayout_2.addWidget(self.deprecated_label)
        self.deprecated_clear = QtWidgets.QPushButton(self.deprecated_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deprecated_clear.sizePolicy().hasHeightForWidth())
        self.deprecated_clear.setSizePolicy(sizePolicy)
        self.deprecated_clear.setObjectName("deprecated_clear")
        self.horizontalLayout_2.addWidget(self.deprecated_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.deprecated_list = QtWidgets.QListWidget(self.deprecated_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deprecated_list.sizePolicy().hasHeightForWidth())
        self.deprecated_list.setSizePolicy(sizePolicy)
        self.deprecated_list.setObjectName("deprecated_list")
        self.verticalLayout_5.addWidget(self.deprecated_list)
        self.panel_widget.addTab(self.deprecated_tab, "")
        self.verticalLayout_4.addWidget(self.h_splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 30))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_new_project = QtWidgets.QAction(MainWindow)
        self.action_new_project.setObjectName("action_new_project")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setIcon(icon)
        self.action_about.setObjectName("action_about")
        self.action_mde_tw = QtWidgets.QAction(MainWindow)
        self.action_mde_tw.setObjectName("action_mde_tw")
        self.action_about_qt = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Logo_Qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_qt.setIcon(icon1)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_New_Window = QtWidgets.QAction(MainWindow)
        self.action_New_Window.setObjectName("action_New_Window")
        self.action_save_all = QtWidgets.QAction(MainWindow)
        self.action_save_all.setObjectName("action_save_all")
        self.menu_File.addAction(self.action_new_project)
        self.menu_File.addAction(self.action_open)
        self.menu_File.addAction(self.action_save)
        self.menu_File.addAction(self.action_save_all)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_New_Window)
        self.menu_File.addAction(self.action_close)
        self.menu_Help.addAction(self.action_mde_tw)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_about_qt)
        self.menu_Help.addAction(self.action_about)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.panel_widget.setCurrentIndex(0)
        self.action_close.triggered.connect(MainWindow.close)
        self.deprecated_clear.clicked.connect(self.deprecated_list.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kmol editor"))
        self.highlighter_label.setText(_translate("MainWindow", "Highlighter:"))
        self.highlighter_option.setItemText(0, _translate("MainWindow", "Markdown"))
        self.highlighter_option.setItemText(1, _translate("MainWindow", "HTML"))
        self.highlighter_option.setItemText(2, _translate("MainWindow", "Python"))
        self.exec_button.setText(_translate("MainWindow", "Execute Script"))
        self.tree_main.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.tree_main.headerItem().setText(1, _translate("MainWindow", "Path"))
        self.panel_widget.setTabText(self.panel_widget.indexOf(self.console_tab), _translate("MainWindow", "Console"))
        self.panel_widget.setTabText(self.panel_widget.indexOf(self.find_tab), _translate("MainWindow", "Find and Replace"))
        self.deprecated_label.setText(_translate("MainWindow", "The contents of deleted nodes."))
        self.deprecated_clear.setText(_translate("MainWindow", "Clear"))
        self.panel_widget.setTabText(self.panel_widget.indexOf(self.deprecated_tab), _translate("MainWindow", "Deprecated"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_new_project.setText(_translate("MainWindow", "New Project"))
        self.action_new_project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_close.setText(_translate("MainWindow", "Close"))
        self.action_about.setText(_translate("MainWindow", "About Kmol editor"))
        self.action_about.setShortcut(_translate("MainWindow", "F1"))
        self.action_mde_tw.setText(_translate("MainWindow", "mde.tw"))
        self.action_about_qt.setText(_translate("MainWindow", "About Qt"))
        self.action_New_Window.setText(_translate("MainWindow", "New Window"))
        self.action_save_all.setText(_translate("MainWindow", "Save All"))
        self.action_save_all.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

