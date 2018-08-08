# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\kmol-editor\core\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 829)
        MainWindow.setAcceptDrops(True)
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
        self.verticalWidget = QtWidgets.QWidget(self.v_splitter)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.highlighter_label = QtWidgets.QLabel(self.verticalWidget)
        self.highlighter_label.setObjectName("highlighter_label")
        self.horizontalLayout.addWidget(self.highlighter_label)
        self.highlighter_option = QtWidgets.QComboBox(self.verticalWidget)
        self.highlighter_option.setObjectName("highlighter_option")
        self.horizontalLayout.addWidget(self.highlighter_option)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exec_button = QtWidgets.QPushButton(self.verticalWidget)
        self.exec_button.setObjectName("exec_button")
        self.horizontalLayout.addWidget(self.exec_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tree_widget = QtWidgets.QWidget(self.verticalWidget)
        self.tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_widget.setObjectName("tree_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tree_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edge_line_option = QtWidgets.QCheckBox(self.tree_widget)
        self.edge_line_option.setObjectName("edge_line_option")
        self.horizontalLayout_5.addWidget(self.edge_line_option)
        self.auto_expand_option = QtWidgets.QCheckBox(self.tree_widget)
        self.auto_expand_option.setObjectName("auto_expand_option")
        self.horizontalLayout_5.addWidget(self.auto_expand_option)
        self.trailing_blanks_option = QtWidgets.QCheckBox(self.tree_widget)
        self.trailing_blanks_option.setChecked(True)
        self.trailing_blanks_option.setObjectName("trailing_blanks_option")
        self.horizontalLayout_5.addWidget(self.trailing_blanks_option)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
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
        self.console.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.console.setObjectName("console")
        self.verticalLayout_3.addWidget(self.console)
        self.panel_widget.addTab(self.console_tab, "")
        self.find_tab = QtWidgets.QWidget()
        self.find_tab.setObjectName("find_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.find_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_bar = QtWidgets.QLineEdit(self.find_tab)
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_2.addWidget(self.search_bar)
        self.find_next_button = QtWidgets.QPushButton(self.find_tab)
        self.find_next_button.setObjectName("find_next_button")
        self.horizontalLayout_2.addWidget(self.find_next_button)
        self.find_previous_button = QtWidgets.QPushButton(self.find_tab)
        self.find_previous_button.setObjectName("find_previous_button")
        self.horizontalLayout_2.addWidget(self.find_previous_button)
        self.wrap_around = QtWidgets.QCheckBox(self.find_tab)
        self.wrap_around.setChecked(True)
        self.wrap_around.setObjectName("wrap_around")
        self.horizontalLayout_2.addWidget(self.wrap_around)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.match_case_option = QtWidgets.QCheckBox(self.find_tab)
        self.match_case_option.setObjectName("match_case_option")
        self.horizontalLayout_4.addWidget(self.match_case_option)
        self.whole_word_option = QtWidgets.QCheckBox(self.find_tab)
        self.whole_word_option.setObjectName("whole_word_option")
        self.horizontalLayout_4.addWidget(self.whole_word_option)
        self.re_option = QtWidgets.QCheckBox(self.find_tab)
        self.re_option.setObjectName("re_option")
        self.horizontalLayout_4.addWidget(self.re_option)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.find_project_button = QtWidgets.QPushButton(self.find_tab)
        self.find_project_button.setObjectName("find_project_button")
        self.horizontalLayout_4.addWidget(self.find_project_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.replace_bar = QtWidgets.QLineEdit(self.find_tab)
        self.replace_bar.setObjectName("replace_bar")
        self.horizontalLayout_3.addWidget(self.replace_bar)
        self.replace_node_button = QtWidgets.QPushButton(self.find_tab)
        self.replace_node_button.setObjectName("replace_node_button")
        self.horizontalLayout_3.addWidget(self.replace_node_button)
        self.replace_project_button = QtWidgets.QPushButton(self.find_tab)
        self.replace_project_button.setObjectName("replace_project_button")
        self.horizontalLayout_3.addWidget(self.replace_project_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.find_list = QtWidgets.QListWidget(self.find_tab)
        self.find_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.find_list.setObjectName("find_list")
        self.verticalLayout_6.addWidget(self.find_list)
        self.panel_widget.addTab(self.find_tab, "")
        self.verticalLayout_4.addWidget(self.h_splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.macros_toolbar = QtWidgets.QToolBar(MainWindow)
        self.macros_toolbar.setObjectName("macros_toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.macros_toolbar)
        self.action_new_project = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_project.setIcon(icon1)
        self.action_new_project.setObjectName("action_new_project")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setIcon(icon1)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setIcon(icon1)
        self.action_save.setObjectName("action_save")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setIcon(icon1)
        self.action_close.setObjectName("action_close")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setIcon(icon)
        self.action_about.setObjectName("action_about")
        self.action_mde_tw = QtWidgets.QAction(MainWindow)
        self.action_mde_tw.setObjectName("action_mde_tw")
        self.action_about_qt = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Logo_Qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about_qt.setIcon(icon2)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_New_Window = QtWidgets.QAction(MainWindow)
        self.action_New_Window.setIcon(icon1)
        self.action_New_Window.setObjectName("action_New_Window")
        self.action_save_all = QtWidgets.QAction(MainWindow)
        self.action_save_all.setIcon(icon1)
        self.action_save_all.setObjectName("action_save_all")
        self.action_open_from_dir = QtWidgets.QAction(MainWindow)
        self.action_open_from_dir.setObjectName("action_open_from_dir")
        self.menu_File.addAction(self.action_new_project)
        self.menu_File.addAction(self.action_open)
        self.menu_File.addAction(self.action_open_from_dir)
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
        self.action_close.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kmol editor"))
        self.highlighter_label.setText(_translate("MainWindow", "Highlighter:"))
        self.exec_button.setText(_translate("MainWindow", "Execute Script"))
        self.edge_line_option.setText(_translate("MainWindow", "Edge Line"))
        self.auto_expand_option.setText(_translate("MainWindow", "Auto Expand"))
        self.trailing_blanks_option.setText(_translate("MainWindow", "Remove Trailing Blanks"))
        self.tree_main.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.tree_main.headerItem().setText(1, _translate("MainWindow", "Path"))
        self.panel_widget.setTabText(self.panel_widget.indexOf(self.console_tab), _translate("MainWindow", "Console"))
        self.find_next_button.setText(_translate("MainWindow", "Find Next"))
        self.find_previous_button.setText(_translate("MainWindow", "Find Previous"))
        self.wrap_around.setText(_translate("MainWindow", "Wrap around"))
        self.match_case_option.setText(_translate("MainWindow", "Match case"))
        self.whole_word_option.setText(_translate("MainWindow", "Whole word"))
        self.re_option.setText(_translate("MainWindow", "Regular expression"))
        self.find_project_button.setText(_translate("MainWindow", "Find in Project"))
        self.replace_node_button.setText(_translate("MainWindow", "Replace in Node"))
        self.replace_project_button.setText(_translate("MainWindow", "Rplace in Project"))
        self.panel_widget.setTabText(self.panel_widget.indexOf(self.find_tab), _translate("MainWindow", "Find and Replace"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.macros_toolbar.setWindowTitle(_translate("MainWindow", "Macro toolbar"))
        self.action_new_project.setText(_translate("MainWindow", "New Project"))
        self.action_new_project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "Open Project"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "Save Project"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_close.setText(_translate("MainWindow", "Close"))
        self.action_about.setText(_translate("MainWindow", "About Kmol editor"))
        self.action_about.setShortcut(_translate("MainWindow", "F1"))
        self.action_mde_tw.setText(_translate("MainWindow", "mde.tw"))
        self.action_about_qt.setText(_translate("MainWindow", "About Qt"))
        self.action_New_Window.setText(_translate("MainWindow", "New Window"))
        self.action_save_all.setText(_translate("MainWindow", "Save All"))
        self.action_save_all.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_open_from_dir.setText(_translate("MainWindow", "Open from Directory"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

