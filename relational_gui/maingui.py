# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relational_gui/maingui.ui'
#
# Created: Thu Jun  4 22:17:58 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cmdAbout = QtWidgets.QPushButton(self.groupBox_3)
        self.cmdAbout.setObjectName("cmdAbout")
        self.verticalLayout_5.addWidget(self.cmdAbout)
        self.cmdSurvey = QtWidgets.QPushButton(self.groupBox_3)
        self.cmdSurvey.setObjectName("cmdSurvey")
        self.verticalLayout_5.addWidget(self.cmdSurvey)
        self.verticalLayout_11.addWidget(self.groupBox_3)
        self.groupOperators = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupOperators.setObjectName("groupOperators")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupOperators)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cmdProduct = QtWidgets.QPushButton(self.groupOperators)
        self.cmdProduct.setText("*")
        self.cmdProduct.setObjectName("cmdProduct")
        self.verticalLayout_10.addWidget(self.cmdProduct)
        self.cmdDifference = QtWidgets.QPushButton(self.groupOperators)
        self.cmdDifference.setText("-")
        self.cmdDifference.setObjectName("cmdDifference")
        self.verticalLayout_10.addWidget(self.cmdDifference)
        self.cmdUnion = QtWidgets.QPushButton(self.groupOperators)
        self.cmdUnion.setText("∪")
        self.cmdUnion.setObjectName("cmdUnion")
        self.verticalLayout_10.addWidget(self.cmdUnion)
        self.cmdIntersection = QtWidgets.QPushButton(self.groupOperators)
        self.cmdIntersection.setText("∩")
        self.cmdIntersection.setObjectName("cmdIntersection")
        self.verticalLayout_10.addWidget(self.cmdIntersection)
        self.cmdDivision = QtWidgets.QPushButton(self.groupOperators)
        self.cmdDivision.setText("÷")
        self.cmdDivision.setObjectName("cmdDivision")
        self.verticalLayout_10.addWidget(self.cmdDivision)
        self.cmdJoin = QtWidgets.QPushButton(self.groupOperators)
        self.cmdJoin.setText("⋈")
        self.cmdJoin.setObjectName("cmdJoin")
        self.verticalLayout_10.addWidget(self.cmdJoin)
        self.cmdOuterLeft = QtWidgets.QPushButton(self.groupOperators)
        self.cmdOuterLeft.setText("⧑")
        self.cmdOuterLeft.setObjectName("cmdOuterLeft")
        self.verticalLayout_10.addWidget(self.cmdOuterLeft)
        self.cmdOuterRight = QtWidgets.QPushButton(self.groupOperators)
        self.cmdOuterRight.setText("⧒")
        self.cmdOuterRight.setObjectName("cmdOuterRight")
        self.verticalLayout_10.addWidget(self.cmdOuterRight)
        self.cmdOuter = QtWidgets.QPushButton(self.groupOperators)
        self.cmdOuter.setText("⧓")
        self.cmdOuter.setObjectName("cmdOuter")
        self.verticalLayout_10.addWidget(self.cmdOuter)
        self.cmdProjection = QtWidgets.QPushButton(self.groupOperators)
        self.cmdProjection.setText("π")
        self.cmdProjection.setObjectName("cmdProjection")
        self.verticalLayout_10.addWidget(self.cmdProjection)
        self.cmdSelection = QtWidgets.QPushButton(self.groupOperators)
        self.cmdSelection.setText("σ")
        self.cmdSelection.setObjectName("cmdSelection")
        self.verticalLayout_10.addWidget(self.cmdSelection)
        self.cmdRename = QtWidgets.QPushButton(self.groupOperators)
        self.cmdRename.setText("ρ")
        self.cmdRename.setObjectName("cmdRename")
        self.verticalLayout_10.addWidget(self.cmdRename)
        self.cmdArrow = QtWidgets.QPushButton(self.groupOperators)
        self.cmdArrow.setText("➡")
        self.cmdArrow.setObjectName("cmdArrow")
        self.verticalLayout_10.addWidget(self.cmdArrow)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_11.addWidget(self.groupOperators)
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.table = QtWidgets.QTreeWidget(self.splitter_2)
        self.table.setMinimumSize(QtCore.QSize(450, 400))
        self.table.setSizeIncrement(QtCore.QSize(0, 0))
        self.table.setRootIsDecorated(False)
        self.table.setObjectName("table")
        self.table.headerItem().setText(0, "Empty relation")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frmOptimizations = QtWidgets.QFrame(self.layoutWidget1)
        self.frmOptimizations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmOptimizations.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmOptimizations.setLineWidth(0)
        self.frmOptimizations.setObjectName("frmOptimizations")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmOptimizations)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstHistory = QtWidgets.QListWidget(self.frmOptimizations)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstHistory.sizePolicy().hasHeightForWidth())
        self.lstHistory.setSizePolicy(sizePolicy)
        self.lstHistory.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lstHistory.setBaseSize(QtCore.QSize(0, 0))
        self.lstHistory.setObjectName("lstHistory")
        self.verticalLayout_2.addWidget(self.lstHistory)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmdOptimize = QtWidgets.QPushButton(self.frmOptimizations)
        self.cmdOptimize.setObjectName("cmdOptimize")
        self.horizontalLayout_3.addWidget(self.cmdOptimize)
        self.cmdUndoOptimize = QtWidgets.QPushButton(self.frmOptimizations)
        self.cmdUndoOptimize.setObjectName("cmdUndoOptimize")
        self.horizontalLayout_3.addWidget(self.cmdUndoOptimize)
        self.cmdClearHistory = QtWidgets.QPushButton(self.frmOptimizations)
        self.cmdClearHistory.setObjectName("cmdClearHistory")
        self.horizontalLayout_3.addWidget(self.cmdClearHistory)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addWidget(self.frmOptimizations)
        self.frmMultiLine = QtWidgets.QFrame(self.layoutWidget1)
        self.frmMultiLine.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmMultiLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmMultiLine.setLineWidth(0)
        self.frmMultiLine.setObjectName("frmMultiLine")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmMultiLine)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtMultiQuery = QtWidgets.QPlainTextEdit(self.frmMultiLine)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.txtMultiQuery.setFont(font)
        self.txtMultiQuery.setPlainText("")
        self.txtMultiQuery.setObjectName("txtMultiQuery")
        self.horizontalLayout_2.addWidget(self.txtMultiQuery)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cmdClearMultilineQuery = QtWidgets.QPushButton(self.frmMultiLine)
        self.cmdClearMultilineQuery.setObjectName("cmdClearMultilineQuery")
        self.verticalLayout_4.addWidget(self.cmdClearMultilineQuery)
        self.cmdExecuteMultiline = QtWidgets.QPushButton(self.frmMultiLine)
        self.cmdExecuteMultiline.setAutoDefault(False)
        self.cmdExecuteMultiline.setDefault(False)
        self.cmdExecuteMultiline.setObjectName("cmdExecuteMultiline")
        self.verticalLayout_4.addWidget(self.cmdExecuteMultiline)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.frmMultiLine)
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lstRelations = QtWidgets.QListWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstRelations.sizePolicy().hasHeightForWidth())
        self.lstRelations.setSizePolicy(sizePolicy)
        self.lstRelations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lstRelations.setObjectName("lstRelations")
        self.verticalLayout.addWidget(self.lstRelations)
        self.cmdNew = QtWidgets.QPushButton(self.groupBox)
        self.cmdNew.setObjectName("cmdNew")
        self.verticalLayout.addWidget(self.cmdNew)
        self.cmdLoad = QtWidgets.QPushButton(self.groupBox)
        self.cmdLoad.setObjectName("cmdLoad")
        self.verticalLayout.addWidget(self.cmdLoad)
        self.cmdSave = QtWidgets.QPushButton(self.groupBox)
        self.cmdSave.setObjectName("cmdSave")
        self.verticalLayout.addWidget(self.cmdSave)
        self.cmdEdit = QtWidgets.QPushButton(self.groupBox)
        self.cmdEdit.setObjectName("cmdEdit")
        self.verticalLayout.addWidget(self.cmdEdit)
        self.cmdUnload = QtWidgets.QPushButton(self.groupBox)
        self.cmdUnload.setObjectName("cmdUnload")
        self.verticalLayout.addWidget(self.cmdUnload)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lstAttributes = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstAttributes.sizePolicy().hasHeightForWidth())
        self.lstAttributes.setSizePolicy(sizePolicy)
        self.lstAttributes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lstAttributes.setObjectName("lstAttributes")
        self.verticalLayout_3.addWidget(self.lstAttributes)
        self.verticalLayout_7.addWidget(self.splitter_4)
        self.lineExpressionFrame = QtWidgets.QFrame(self.centralwidget)
        self.lineExpressionFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lineExpressionFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lineExpressionFrame.setLineWidth(0)
        self.lineExpressionFrame.setObjectName("lineExpressionFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.lineExpressionFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtResult = QtWidgets.QLineEdit(self.lineExpressionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtResult.sizePolicy().hasHeightForWidth())
        self.txtResult.setSizePolicy(sizePolicy)
        self.txtResult.setObjectName("txtResult")
        self.horizontalLayout.addWidget(self.txtResult)
        self.label = QtWidgets.QLabel(self.lineExpressionFrame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtQuery = QtWidgets.QLineEdit(self.lineExpressionFrame)
        self.txtQuery.setObjectName("txtQuery")
        self.horizontalLayout.addWidget(self.txtQuery)
        self.cmdClearQuery = QtWidgets.QPushButton(self.lineExpressionFrame)
        self.cmdClearQuery.setObjectName("cmdClearQuery")
        self.horizontalLayout.addWidget(self.cmdClearQuery)
        self.cmdExecute = QtWidgets.QPushButton(self.lineExpressionFrame)
        self.cmdExecute.setAutoDefault(True)
        self.cmdExecute.setDefault(True)
        self.cmdExecute.setObjectName("cmdExecute")
        self.horizontalLayout.addWidget(self.cmdExecute)
        self.verticalLayout_7.addWidget(self.lineExpressionFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuRelations = QtWidgets.QMenu(self.menubar)
        self.menuRelations.setObjectName("menuRelations")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.action_Load_relation = QtWidgets.QAction(MainWindow)
        self.action_Load_relation.setObjectName("action_Load_relation")
        self.action_Save_relation = QtWidgets.QAction(MainWindow)
        self.action_Save_relation.setObjectName("action_Save_relation")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.action_Quit.setObjectName("action_Quit")
        self.actionCheck_for_new_versions = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_new_versions.setObjectName("actionCheck_for_new_versions")
        self.actionNew_relation = QtWidgets.QAction(MainWindow)
        self.actionNew_relation.setObjectName("actionNew_relation")
        self.actionEdit_relation = QtWidgets.QAction(MainWindow)
        self.actionEdit_relation.setObjectName("actionEdit_relation")
        self.actionNew_session = QtWidgets.QAction(MainWindow)
        self.actionNew_session.setObjectName("actionNew_session")
        self.actionSave_session_as = QtWidgets.QAction(MainWindow)
        self.actionSave_session_as.setObjectName("actionSave_session_as")
        self.actionManage_sessions = QtWidgets.QAction(MainWindow)
        self.actionManage_sessions.setObjectName("actionManage_sessions")
        self.actionUnload_relation = QtWidgets.QAction(MainWindow)
        self.actionUnload_relation.setObjectName("actionUnload_relation")
        self.actionMulti_line_mode = QtWidgets.QAction(MainWindow)
        self.actionMulti_line_mode.setCheckable(True)
        self.actionMulti_line_mode.setObjectName("actionMulti_line_mode")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionCheck_for_new_versions)
        self.menuRelations.addAction(self.actionNew_relation)
        self.menuRelations.addAction(self.action_Load_relation)
        self.menuRelations.addAction(self.action_Save_relation)
        self.menuRelations.addAction(self.actionEdit_relation)
        self.menuRelations.addAction(self.actionUnload_relation)
        self.menuSettings.addAction(self.actionMulti_line_mode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRelations.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.txtQuery)

        self.retranslateUi(MainWindow)
        self.cmdAbout.clicked.connect(MainWindow.showAbout)
        self.cmdSurvey.clicked.connect(MainWindow.showSurvey)
        self.cmdProduct.clicked.connect(MainWindow.addProduct)
        self.cmdDifference.clicked.connect(MainWindow.addDifference)
        self.cmdArrow.clicked.connect(MainWindow.addArrow)
        self.cmdRename.clicked.connect(MainWindow.addRename)
        self.cmdSelection.clicked.connect(MainWindow.addSelection)
        self.cmdProjection.clicked.connect(MainWindow.addProjection)
        self.cmdUnload.clicked.connect(MainWindow.unloadRelation)
        self.cmdSave.clicked.connect(MainWindow.saveRelation)
        self.cmdLoad.clicked.connect(MainWindow.loadRelation)
        self.cmdOuterRight.clicked.connect(MainWindow.addORight)
        self.cmdOuter.clicked.connect(MainWindow.addOuter)
        self.cmdOuterLeft.clicked.connect(MainWindow.addOLeft)
        self.cmdJoin.clicked.connect(MainWindow.addJoin)
        self.cmdDivision.clicked.connect(MainWindow.addDivision)
        self.cmdIntersection.clicked.connect(MainWindow.addIntersection)
        self.cmdUnion.clicked.connect(MainWindow.addUnion)
        self.lstRelations.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.printRelation)
        self.lstRelations.itemClicked['QListWidgetItem*'].connect(MainWindow.showAttributes)
        self.actionAbout.triggered.connect(MainWindow.showAbout)
        self.action_Load_relation.triggered.connect(MainWindow.loadRelation)
        self.action_Save_relation.triggered.connect(MainWindow.saveRelation)
        self.action_Quit.triggered.connect(MainWindow.close)
        self.actionCheck_for_new_versions.triggered.connect(MainWindow.checkVersion)
        self.cmdEdit.clicked.connect(MainWindow.editRelation)
        self.actionEdit_relation.triggered.connect(MainWindow.editRelation)
        self.cmdNew.clicked.connect(MainWindow.newRelation)
        self.actionNew_relation.triggered.connect(MainWindow.newRelation)
        self.actionUnload_relation.triggered.connect(MainWindow.unloadRelation)
        self.actionMulti_line_mode.toggled['bool'].connect(MainWindow.setMultiline)
        self.cmdClearMultilineQuery.clicked.connect(self.txtMultiQuery.clear)
        self.cmdExecuteMultiline.clicked.connect(MainWindow.execute)
        self.cmdClearQuery.clicked.connect(self.txtQuery.clear)
        self.cmdClearHistory.clicked.connect(self.lstHistory.clear)
        self.cmdOptimize.clicked.connect(MainWindow.optimize)
        self.cmdUndoOptimize.clicked.connect(MainWindow.undoOptimize)
        self.cmdExecute.clicked.connect(MainWindow.execute)
        self.txtQuery.returnPressed.connect(MainWindow.execute)
        self.lstHistory.itemDoubleClicked['QListWidgetItem*'].connect(MainWindow.resumeHistory)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cmdAbout, self.cmdSurvey)
        MainWindow.setTabOrder(self.cmdSurvey, self.cmdProduct)
        MainWindow.setTabOrder(self.cmdProduct, self.cmdDifference)
        MainWindow.setTabOrder(self.cmdDifference, self.cmdUnion)
        MainWindow.setTabOrder(self.cmdUnion, self.cmdIntersection)
        MainWindow.setTabOrder(self.cmdIntersection, self.cmdDivision)
        MainWindow.setTabOrder(self.cmdDivision, self.cmdJoin)
        MainWindow.setTabOrder(self.cmdJoin, self.cmdOuterLeft)
        MainWindow.setTabOrder(self.cmdOuterLeft, self.cmdOuterRight)
        MainWindow.setTabOrder(self.cmdOuterRight, self.cmdOuter)
        MainWindow.setTabOrder(self.cmdOuter, self.cmdProjection)
        MainWindow.setTabOrder(self.cmdProjection, self.cmdSelection)
        MainWindow.setTabOrder(self.cmdSelection, self.cmdRename)
        MainWindow.setTabOrder(self.cmdRename, self.cmdArrow)
        MainWindow.setTabOrder(self.cmdArrow, self.table)
        MainWindow.setTabOrder(self.table, self.lstHistory)
        MainWindow.setTabOrder(self.lstHistory, self.cmdOptimize)
        MainWindow.setTabOrder(self.cmdOptimize, self.cmdUndoOptimize)
        MainWindow.setTabOrder(self.cmdUndoOptimize, self.cmdClearHistory)
        MainWindow.setTabOrder(self.cmdClearHistory, self.txtMultiQuery)
        MainWindow.setTabOrder(self.txtMultiQuery, self.cmdClearMultilineQuery)
        MainWindow.setTabOrder(self.cmdClearMultilineQuery, self.cmdExecuteMultiline)
        MainWindow.setTabOrder(self.cmdExecuteMultiline, self.lstRelations)
        MainWindow.setTabOrder(self.lstRelations, self.cmdNew)
        MainWindow.setTabOrder(self.cmdNew, self.cmdLoad)
        MainWindow.setTabOrder(self.cmdLoad, self.cmdSave)
        MainWindow.setTabOrder(self.cmdSave, self.cmdEdit)
        MainWindow.setTabOrder(self.cmdEdit, self.cmdUnload)
        MainWindow.setTabOrder(self.cmdUnload, self.lstAttributes)
        MainWindow.setTabOrder(self.lstAttributes, self.txtResult)
        MainWindow.setTabOrder(self.txtResult, self.txtQuery)
        MainWindow.setTabOrder(self.txtQuery, self.cmdClearQuery)
        MainWindow.setTabOrder(self.cmdClearQuery, self.cmdExecute)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Relational"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Menu"))
        self.cmdAbout.setText(_translate("MainWindow", "About"))
        self.cmdSurvey.setText(_translate("MainWindow", "Survey"))
        self.groupOperators.setTitle(_translate("MainWindow", "Operators"))
        self.cmdProduct.setToolTip(_translate("MainWindow", "Product"))
        self.cmdDifference.setToolTip(_translate("MainWindow", "Difference"))
        self.cmdUnion.setToolTip(_translate("MainWindow", "Union"))
        self.cmdIntersection.setToolTip(_translate("MainWindow", "Intersection"))
        self.cmdDivision.setToolTip(_translate("MainWindow", "Division"))
        self.cmdJoin.setToolTip(_translate("MainWindow", "Natural join"))
        self.cmdOuterLeft.setToolTip(_translate("MainWindow", "Left outer join"))
        self.cmdOuterRight.setToolTip(_translate("MainWindow", "Right outer join"))
        self.cmdOuter.setToolTip(_translate("MainWindow", "Full outer join"))
        self.cmdProjection.setToolTip(_translate("MainWindow", "Projection"))
        self.cmdSelection.setToolTip(_translate("MainWindow", "Selection"))
        self.cmdRename.setToolTip(_translate("MainWindow", "Rename"))
        self.cmdOptimize.setText(_translate("MainWindow", "Optimize"))
        self.cmdUndoOptimize.setText(_translate("MainWindow", "Undo optimize"))
        self.cmdClearHistory.setText(_translate("MainWindow", "Clear history"))
        self.cmdClearMultilineQuery.setText(_translate("MainWindow", "⌫"))
        self.cmdExecuteMultiline.setText(_translate("MainWindow", "Execute"))
        self.groupBox.setTitle(_translate("MainWindow", "Relations"))
        self.lstRelations.setSortingEnabled(True)
        self.cmdNew.setText(_translate("MainWindow", "New relation"))
        self.cmdLoad.setText(_translate("MainWindow", "Load relation"))
        self.cmdSave.setText(_translate("MainWindow", "Save relation"))
        self.cmdEdit.setText(_translate("MainWindow", "Edit relation"))
        self.cmdUnload.setText(_translate("MainWindow", "Unload relation"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Attributes"))
        self.txtResult.setText(_translate("MainWindow", "_last1"))
        self.label.setText(_translate("MainWindow", "="))
        self.cmdClearQuery.setText(_translate("MainWindow", "⌫"))
        self.cmdExecute.setText(_translate("MainWindow", "Execute"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuAbout.setTitle(_translate("MainWindow", "&Help"))
        self.menuRelations.setTitle(_translate("MainWindow", "Relations"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.action_Load_relation.setText(_translate("MainWindow", "&Load relation"))
        self.action_Load_relation.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Save_relation.setText(_translate("MainWindow", "&Save relation"))
        self.action_Save_relation.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCheck_for_new_versions.setText(_translate("MainWindow", "Check for new versions"))
        self.actionNew_relation.setText(_translate("MainWindow", "New relation"))
        self.actionNew_relation.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionEdit_relation.setText(_translate("MainWindow", "Edit relation"))
        self.actionEdit_relation.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionNew_session.setText(_translate("MainWindow", "New session"))
        self.actionSave_session_as.setText(_translate("MainWindow", "Save session as"))
        self.actionSave_session_as.setToolTip(_translate("MainWindow", "Save session as"))
        self.actionManage_sessions.setText(_translate("MainWindow", "Manage sessions"))
        self.actionUnload_relation.setText(_translate("MainWindow", "Unload relation"))
        self.actionMulti_line_mode.setText(_translate("MainWindow", "Multi-line mode"))
        self.actionMulti_line_mode.setShortcut(_translate("MainWindow", "Ctrl+L"))

