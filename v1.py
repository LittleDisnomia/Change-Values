from re import S
from gnuradio import gr,analog,blocks,qtgui
from PyQt5 import QtWidgets
import sys,sip
import time

class myBlock(gr.top_block,QtWidgets.QWidget):

    def __init__(self):
        gr.top_block.__init__(self)
        QtWidgets.QWidget.__init__(self)

        # Variable to change the amplitude
        self.amp = 1

        # Set the window and layout
        self.MainLayout = QtWidgets.QGridLayout()
        self.setLayout(self.MainLayout)
        self.setMinimumSize(600,600)
        
        # Defined blocks
        self.source = analog.sig_source_c(48e3,analog.GR_COS_WAVE,3000,self.amp)
        self.guiSink = qtgui.time_sink_c(1024,48e3,"",1)
        self.guiSink.set_update_time(0.1)

        # Connection
        self.connect(self.source,self.guiSink)

        # Create qt time widget and added to my window
        self.guiSink_Win = sip.wrapinstance(self.guiSink.pyqwidget(),QtWidgets.QWidget)
        self.MainLayout.addWidget(self.guiSink_Win)
        
    def set_amp(self,amp):
        self.amp = amp
    def get_amp(self):
        return self.amp

def main():
    
    app = QtWidgets.QApplication(sys.argv)
    tb = myBlock()
    
    print(tb.get_amp())   
    tb.set_amp(3)
    print(tb.get_amp())

    tb.start()
    tb.show()

    
    
    app.exec_()
if __name__ == '__main__':
    main()