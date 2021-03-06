# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GVNEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.EditingContainer = QtWidgets.QWidget(self.centralwidget)
        self.EditingContainer.setObjectName("EditingContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.EditingContainer)
        self.verticalLayout_2.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DataManagerContainer = QtWidgets.QTabWidget(self.EditingContainer)
        self.DataManagerContainer.setObjectName("DataManagerContainer")
        self.TabDialogueEditor = QtWidgets.QWidget()
        self.TabDialogueEditor.setObjectName("TabDialogueEditor")
        self.DEditorTabLayout = QtWidgets.QVBoxLayout(self.TabDialogueEditor)
        self.DEditorTabLayout.setObjectName("DEditorTabLayout")
        self.DialogueEditorToolBar = QtWidgets.QFrame(self.TabDialogueEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DialogueEditorToolBar.sizePolicy().hasHeightForWidth())
        self.DialogueEditorToolBar.setSizePolicy(sizePolicy)
        self.DialogueEditorToolBar.setAutoFillBackground(False)
        self.DialogueEditorToolBar.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border-radius: 4px;\n"
"    background-color: rgb(44,53,57);\n"
"}")
        self.DialogueEditorToolBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DialogueEditorToolBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DialogueEditorToolBar.setObjectName("DialogueEditorToolBar")
        self.DEditorToolbarMainLayout = QtWidgets.QHBoxLayout(self.DialogueEditorToolBar)
        self.DEditorToolbarMainLayout.setContentsMargins(2, 2, 2, 2)
        self.DEditorToolbarMainLayout.setSpacing(0)
        self.DEditorToolbarMainLayout.setObjectName("DEditorToolbarMainLayout")
        self.AddEntryButton = QtWidgets.QToolButton(self.DialogueEditorToolBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntryButton.sizePolicy().hasHeightForWidth())
        self.AddEntryButton.setSizePolicy(sizePolicy)
        self.AddEntryButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Content/Icons/Plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddEntryButton.setIcon(icon)
        self.AddEntryButton.setObjectName("AddEntryButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.AddEntryButton)
        self.DEditorToolbarMainLayout.addWidget(self.AddEntryButton)
        self.RemoveEntryButton = QtWidgets.QToolButton(self.DialogueEditorToolBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveEntryButton.sizePolicy().hasHeightForWidth())
        self.RemoveEntryButton.setSizePolicy(sizePolicy)
        self.RemoveEntryButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Content/Icons/Minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RemoveEntryButton.setIcon(icon1)
        self.RemoveEntryButton.setObjectName("RemoveEntryButton")
        self.buttonGroup.addButton(self.RemoveEntryButton)
        self.DEditorToolbarMainLayout.addWidget(self.RemoveEntryButton)
        self.MoveEntryUpButton = QtWidgets.QToolButton(self.DialogueEditorToolBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MoveEntryUpButton.sizePolicy().hasHeightForWidth())
        self.MoveEntryUpButton.setSizePolicy(sizePolicy)
        self.MoveEntryUpButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Content/Icons/Up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoveEntryUpButton.setIcon(icon2)
        self.MoveEntryUpButton.setObjectName("MoveEntryUpButton")
        self.DEditorToolbarMainLayout.addWidget(self.MoveEntryUpButton)
        self.MoveEntryDownButton = QtWidgets.QToolButton(self.DialogueEditorToolBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MoveEntryDownButton.sizePolicy().hasHeightForWidth())
        self.MoveEntryDownButton.setSizePolicy(sizePolicy)
        self.MoveEntryDownButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Content/Icons/Down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MoveEntryDownButton.setIcon(icon3)
        self.MoveEntryDownButton.setObjectName("MoveEntryDownButton")
        self.DEditorToolbarMainLayout.addWidget(self.MoveEntryDownButton)
        spacerItem = QtWidgets.QSpacerItem(534, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DEditorToolbarMainLayout.addItem(spacerItem)
        self.DEditorTabLayout.addWidget(self.DialogueEditorToolBar)
        self.DialogueTable = QtWidgets.QTableView(self.TabDialogueEditor)
        self.DialogueTable.setObjectName("DialogueTable")
        self.DEditorTabLayout.addWidget(self.DialogueTable)
        self.DataManagerContainer.addTab(self.TabDialogueEditor, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.DataManagerContainer.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.DataManagerContainer)
        self.gridLayout.addWidget(self.EditingContainer, 0, 1, 1, 1)
        self.LineDetailsContainer = QtWidgets.QWidget(self.centralwidget)
        self.LineDetailsContainer.setObjectName("LineDetailsContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LineDetailsContainer)
        self.verticalLayout.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LineDetailsTitle = QtWidgets.QLabel(self.LineDetailsContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LineDetailsTitle.setFont(font)
        self.LineDetailsTitle.setObjectName("LineDetailsTitle")
        self.verticalLayout.addWidget(self.LineDetailsTitle)
        self.lineDetailsToolbar = QtWidgets.QFrame(self.LineDetailsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineDetailsToolbar.sizePolicy().hasHeightForWidth())
        self.lineDetailsToolbar.setSizePolicy(sizePolicy)
        self.lineDetailsToolbar.setAutoFillBackground(False)
        self.lineDetailsToolbar.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border-radius: 4px;\n"
"    background-color: rgb(44,53,57);\n"
"}")
        self.lineDetailsToolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lineDetailsToolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineDetailsToolbar.setObjectName("lineDetailsToolbar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lineDetailsToolbar)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.filterDetailInput = QtWidgets.QLineEdit(self.lineDetailsToolbar)
        self.filterDetailInput.setInputMask("")
        self.filterDetailInput.setText("")
        self.filterDetailInput.setObjectName("filterDetailInput")
        self.horizontalLayout_5.addWidget(self.filterDetailInput)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.lineDetailsToolbar)
        self.DetailsList = QtWidgets.QListView(self.LineDetailsContainer)
        self.DetailsList.setObjectName("DetailsList")
        self.verticalLayout.addWidget(self.DetailsList)
        self.gridLayout.addWidget(self.LineDetailsContainer, 0, 2, 1, 1)
        self.LoggerContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoggerContainer.sizePolicy().hasHeightForWidth())
        self.LoggerContainer.setSizePolicy(sizePolicy)
        self.LoggerContainer.setObjectName("LoggerContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.LoggerContainer)
        self.verticalLayout_3.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.loggerTitle = QtWidgets.QLabel(self.LoggerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loggerTitle.setFont(font)
        self.loggerTitle.setObjectName("loggerTitle")
        self.verticalLayout_3.addWidget(self.loggerTitle)
        self.LoggerToolbar = QtWidgets.QFrame(self.LoggerContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoggerToolbar.sizePolicy().hasHeightForWidth())
        self.LoggerToolbar.setSizePolicy(sizePolicy)
        self.LoggerToolbar.setAutoFillBackground(False)
        self.LoggerToolbar.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border-radius: 4px;\n"
"    background-color: rgb(44,53,57);\n"
"}")
        self.LoggerToolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoggerToolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoggerToolbar.setObjectName("LoggerToolbar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.LoggerToolbar)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.clearLogButton = QtWidgets.QToolButton(self.LoggerToolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLogButton.sizePolicy().hasHeightForWidth())
        self.clearLogButton.setSizePolicy(sizePolicy)
        self.clearLogButton.setText("")
        self.clearLogButton.setIcon(icon)
        self.clearLogButton.setObjectName("clearLogButton")
        self.horizontalLayout_3.addWidget(self.clearLogButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.LoggerToolbar)
        self.logList = QtWidgets.QListWidget(self.LoggerContainer)
        self.logList.setObjectName("logList")
        self.verticalLayout_3.addWidget(self.logList)
        self.gridLayout.addWidget(self.LoggerContainer, 1, 0, 1, 3)
        self.SceneOutlinerContainer = QtWidgets.QWidget(self.centralwidget)
        self.SceneOutlinerContainer.setObjectName("SceneOutlinerContainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.SceneOutlinerContainer)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SceneOutlinerTitle = QtWidgets.QLabel(self.SceneOutlinerContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SceneOutlinerTitle.setFont(font)
        self.SceneOutlinerTitle.setObjectName("SceneOutlinerTitle")
        self.verticalLayout_4.addWidget(self.SceneOutlinerTitle)
        self.SceneOutlinerToolbar = QtWidgets.QFrame(self.SceneOutlinerContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SceneOutlinerToolbar.sizePolicy().hasHeightForWidth())
        self.SceneOutlinerToolbar.setSizePolicy(sizePolicy)
        self.SceneOutlinerToolbar.setAutoFillBackground(False)
        self.SceneOutlinerToolbar.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border-radius: 4px;\n"
"    background-color: rgb(44,53,57);\n"
"}")
        self.SceneOutlinerToolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SceneOutlinerToolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SceneOutlinerToolbar.setObjectName("SceneOutlinerToolbar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SceneOutlinerToolbar)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addChapterButton = QtWidgets.QToolButton(self.SceneOutlinerToolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addChapterButton.sizePolicy().hasHeightForWidth())
        self.addChapterButton.setSizePolicy(sizePolicy)
        self.addChapterButton.setText("")
        self.addChapterButton.setIcon(icon)
        self.addChapterButton.setObjectName("addChapterButton")
        self.horizontalLayout_4.addWidget(self.addChapterButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.SceneOutlinerToolbar)
        self.SceneList = QtWidgets.QTreeView(self.SceneOutlinerContainer)
        self.SceneList.setObjectName("SceneList")
        self.verticalLayout_4.addWidget(self.SceneList)
        self.gridLayout.addWidget(self.SceneOutlinerContainer, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.storyMenu = QtWidgets.QMenu(self.menubar)
        self.storyMenu.setObjectName("storyMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.insertRowAction = QtWidgets.QAction(MainWindow)
        self.insertRowAction.setObjectName("insertRowAction")
        self.removeRowAction = QtWidgets.QAction(MainWindow)
        self.removeRowAction.setObjectName("removeRowAction")
        self.loadDataAction = QtWidgets.QAction(MainWindow)
        self.loadDataAction.setObjectName("loadDataAction")
        self.testAction = QtWidgets.QAction(MainWindow)
        self.testAction.setObjectName("testAction")
        self.loadDialogueFileAction = QtWidgets.QAction(MainWindow)
        self.loadDialogueFileAction.setObjectName("loadDialogueFileAction")
        self.createDialogueFileAction = QtWidgets.QAction(MainWindow)
        self.createDialogueFileAction.setObjectName("createDialogueFileAction")
        self.saveDialogueFileAsAction = QtWidgets.QAction(MainWindow)
        self.saveDialogueFileAsAction.setObjectName("saveDialogueFileAsAction")
        self.fileMenu.addAction(self.exitAction)
        self.storyMenu.addAction(self.createDialogueFileAction)
        self.storyMenu.addAction(self.loadDialogueFileAction)
        self.storyMenu.addAction(self.saveDialogueFileAsAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.storyMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.DataManagerContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GVN Editor"))
        self.DataManagerContainer.setTabText(self.DataManagerContainer.indexOf(self.TabDialogueEditor), _translate("MainWindow", "Dialogue"))
        self.DataManagerContainer.setTabText(self.DataManagerContainer.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.LineDetailsTitle.setText(_translate("MainWindow", "Line Details"))
        self.filterDetailInput.setPlaceholderText(_translate("MainWindow", "Filter..."))
        self.loggerTitle.setText(_translate("MainWindow", "Logger"))
        self.SceneOutlinerTitle.setText(_translate("MainWindow", "Scene Outliner"))
        self.fileMenu.setTitle(_translate("MainWindow", "&File"))
        self.storyMenu.setTitle(_translate("MainWindow", "Story"))
        self.exitAction.setText(_translate("MainWindow", "E&xit"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.insertRowAction.setText(_translate("MainWindow", "Insert Row"))
        self.insertRowAction.setShortcut(_translate("MainWindow", "Ctrl+I, R"))
        self.removeRowAction.setText(_translate("MainWindow", "Remove Row"))
        self.removeRowAction.setShortcut(_translate("MainWindow", "Ctrl+R, R"))
        self.loadDataAction.setText(_translate("MainWindow", "Load Story Data"))
        self.testAction.setText(_translate("MainWindow", "test"))
        self.loadDialogueFileAction.setText(_translate("MainWindow", "Open Dialogue File"))
        self.createDialogueFileAction.setText(_translate("MainWindow", "New Dialogue File"))
        self.saveDialogueFileAsAction.setText(_translate("MainWindow", "Save Dialogue File As..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
