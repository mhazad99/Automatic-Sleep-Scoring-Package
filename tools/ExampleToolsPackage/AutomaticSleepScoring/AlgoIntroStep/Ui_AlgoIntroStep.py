# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AlgoIntroStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#import intro_res_rc_rc
import themes_rc

class Ui_AlgoIntroStep(object):
    def setupUi(self, AlgoIntroStep):
        if not AlgoIntroStep.objectName():
            AlgoIntroStep.setObjectName(u"AlgoIntroStep")
        AlgoIntroStep.resize(1099, 858)
        AlgoIntroStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_7 = QVBoxLayout(AlgoIntroStep)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter_2 = QSplitter(AlgoIntroStep)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.layoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1052, 245))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSpacing(24)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.scrollArea_2 = QScrollArea(self.layoutWidget1)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 2069, 408))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.scrollArea_3 = QScrollArea(self.layoutWidget2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1052, 89))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_7)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_6.addWidget(self.splitter)

        self.splitter_2.addWidget(self.layoutWidget)

        self.verticalLayout_7.addWidget(self.splitter_2)


        self.retranslateUi(AlgoIntroStep)

        QMetaObject.connectSlotsByName(AlgoIntroStep)
    # setupUi

    def retranslateUi(self, AlgoIntroStep):
        AlgoIntroStep.setWindowTitle(QCoreApplication.translate("AlgoIntroStep", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Score Sleep Stages YASA</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p>This tool detects <span style=\" font-weight:600;\">sleep stages</span> from PSG files.</p><p>Detection is performed on the entire recording with 30 second epochs corresponding to each sleep stage.<br/>The tool can detect sleep stages based on only one EEG electrode, prefered centreal ones (C3, C4).</p><p>To enhance the perforamance of the algorithm, you can use one EOG and one EMG channel that can increase<br/>classification accuracy.<br/>You can also select 4 high-priority EEG channels as input, allowing the tool to determine the result with <br/>the highest confidence for each channel.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Algorithm Details</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p>The sleep staging algorithm, YASA, is an open-source tool that has been trained, using over 30,000 hours of polysomnographic (PSG) sleep data across diverse populations.</p><p>-&gt;<span style=\" font-weight:600;\"> Data processing:</span> The algorithm uses a central EEG channel, along with EOG, and EMG channels. These signals are downsampled to 100 Hz and bandpassed-filtered between 0.4 Hz and 30 Hz.</p><p>-&gt; <span style=\" font-weight:600;\">Feature Extraction:</span> The algorithm extracts a set of time and frequency domain features from the EEG signal, and optionaly from the EOG and EMG signals. These features are calculated for each 30-second epoch of raw data.</p><p>-&gt; <span style=\" font-weight:600;\">Smoothing and Normalization:</span> The algorithm uses a smoothing approach across all the aformentioned features to incorporate contextual infromation. All the smoothed features are then z-scored across each night.</p><p>-&gt; <span style=\" font-weight:600;\">Machine Learning"
                        " Classification:</span> A lightGBM classifier, a tree-based gradient-boosting classifier, is used.</p><p>-&gt; <span style=\" font-weight:600;\">Performance Evaluation:</span> The algorithm's performance is evaluated using standardized guidelines, including accuracy, Cohen's kappa, Matthews correlation coefficient, confusion matrices, and F1-scores.<br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p>The YASA sleep scoring tool is compatible with different input files including, EDF, NATUS, and STS.</p><p>The output of the automatic scoring algorithm is a .tsv file that saves the predicted sleep stages.</p></body></html>", None))
    # retranslateUi

