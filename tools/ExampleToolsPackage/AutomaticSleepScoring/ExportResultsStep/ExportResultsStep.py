#! /usr/bin/env python3
"""
    InputFiles
    Step to open files to detect spindles.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer

#from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
from ExampleToolsPackage.AutomaticSleepScoring.ExportResultsStep.Ui_ExportResultsStep import Ui_ExportResultsStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialog import WarningDialog


class ExportResultsStep( BaseStepView,  Ui_ExportResultsStep, QtWidgets.QWidget):
    

    """
        InputFilesStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_OutputFiles"] = {"the_data_I_want_to_share":"some_data"}

        # description.json file to know the ID of the node
        node_id_writer = "75e0a878-48a8-4770-bf4e-0038cc998389" 
        self._SavedDestination_topic = f'{node_id_writer}.SavedDestination'
        self._pub_sub_manager.subscribe(self, self._SavedDestination_topic)
        node_id_string = "a6186317-b100-4fb3-9dfa-017548e519b9" 
        self._group_lut_topic = f'{node_id_string}.group_lut'
        self._pub_sub_manager.subscribe(self, self._group_lut_topic)

        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._SavedDestination_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_lut_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._SavedDestination_topic:
           self.lineEdit.setText(message)
        if topic == self._group_lut_topic:
           self.lineEdit_2.setText(str(message))        


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._SavedDestination_topic, self.lineEdit.text())
        self._pub_sub_manager.publish(self, self._group_lut_topic, self.lineEdit_2.text())


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.lineEdit.text())==0:
            WarningDialog(f"You need to define the output destination in step '4 - Output Files'.")
            return False
        return True
    

    # Called when the user clicks on the browse push button
    def browse_slot(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None, 
            'Select Directory', 
            '', 
            QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        if directory:
            self.lineEdit.setText(directory)
