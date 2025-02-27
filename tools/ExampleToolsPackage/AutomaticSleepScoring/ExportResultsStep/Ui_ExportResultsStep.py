# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ExportResultsStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_ExportResultsStep(object):
    def setupUi(self, ExportResultsStep):
        if not ExportResultsStep.objectName():
            ExportResultsStep.setObjectName(u"ExportResultsStep")
        ExportResultsStep.resize(1269, 585)
        ExportResultsStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(ExportResultsStep)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ExportResultsStep)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(ExportResultsStep)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(ExportResultsStep)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ExportResultsStep)
        self.pushButton.clicked.connect(ExportResultsStep.browse_slot)
        QMetaObject.connectSlotsByName(ExportResultsStep)
    # setupUi

    def retranslateUi(self, ExportResultsStep):
        ExportResultsStep.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Export Results</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p>The results of the YASA sleep staging algorithm will be exported.<br/>It includes, the expert annotated hypnogram, the predicted hypnogram, confusion matrix, accuracy, and the average confidence.</p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("ExportResultsStep", u"Select the folder where the exported files are supposed to be saved", None))
        self.pushButton.setText(QCoreApplication.translate("ExportResultsStep", u"Choose", None))
        self.label_2.setText(QCoreApplication.translate("ExportResultsStep", u"<html><head/><body><p><span style=\" font-size:11pt;\">Define a new group name to modify the predicted sleep stages in the .tsv file. (If empty, it would overwrite on the &quot;stage&quot; group)</span></p></body></html>", None))
        self.lineEdit_2.setText("")
    # retranslateUi

