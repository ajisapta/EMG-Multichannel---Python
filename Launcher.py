import sys
import EMG
from PyQt4 import QtGui,QtCore

from Filter import Filter_BP_1,Filter_BS_1,Filter_LP_1,Filter_BP_2,Filter_BS_2,Filter_LP_2\
    ,Filter_BP_3,Filter_BS_3,Filter_LP_3,Filter_BP_4,Filter_BS_4,Filter_LP_4
from Coefficient import *
from Data import Chan_1,Chan_2,Chan_3,Chan_4
import csv
import threading
from NIDAQ_1 import SetupTask1,StartTask1,ReadSamples1,StopAndClearTask1
from NIDAQ_2 import SetupTask2,StartTask2,ReadSamples2,StopAndClearTask2
from NIDAQ_3 import SetupTask3,StartTask3,ReadSamples3,StopAndClearTask3
from NIDAQ_4 import SetupTask4,StartTask4,ReadSamples4,StopAndClearTask4
if __name__=="__main__":

    app = QtGui.QApplication(sys.argv)
    form = EMG.QtGui.QMainWindow()
    gui_plot = EMG.Ui_MainWindow()
    gui_plot.setupUi(form)

    # Channel awal
    data1_plot = gui_plot.win_1.addPlot(title='Channel 1')
    data1_plot.setXRange(0, MAX_PLOT_SIZE)
    # data1_plot.enableAutoRange('y', True)
    data1_plot.setYRange(0, Y_max)
    data1_plot.showGrid(True, True)
    data1_curve = data1_plot.plot(pen='y')
    gui_plot.win_1.nextRow()
    data3_plot = gui_plot.win_1.addPlot(title='Channel 3')
    data3_plot.setXRange(0, MAX_PLOT_SIZE)
    # data3_plot.enableAutoRange('y', True)
    data3_plot.setYRange(0, Y_max)
    # data2_plot.enableAutoRange('y', True)
    data3_plot.showGrid(True, True)
    data3_curve = data3_plot.plot(pen='y')
    # Channel Ganjil
    data2_plot = gui_plot.win_2.addPlot(title='Channel 2')
    data2_plot.setXRange(0, MAX_PLOT_SIZE)
    # data2_plot.enableAutoRange('y', True)
    data2_plot.setYRange(0, Y_max)
    data2_plot.showGrid(True, True)
    data2_curve = data2_plot.plot(pen='y')
    gui_plot.win_2.nextRow()
    data4_plot = gui_plot.win_2.addPlot(title='Channel 4')
    data4_plot.setXRange(0, MAX_PLOT_SIZE)
    # data4_plot.enableAutoRange('y', True)
    data4_plot.setYRange(0, Y_max)
    # data2_plot.enableAutoRange('y', True)
    data4_plot.showGrid(True, True)
    data4_curve = data4_plot.plot(pen='y')

    def Plot():
        global Data_Plot_1, Save_Data_BP_1, Save_Data_BS_1, Save_Output_1 \
            , Input_1, Hasil_BP_1, Hasil_BS_1, Hasil_LP_1, Output_1, Save_Raw_Data_1\
            ,Data_Plot_2, Save_Data_BP_2, Save_Data_BS_2, Save_Output_2 \
            , Input_2, Hasil_BP_2, Hasil_BS_2, Hasil_LP_2, Output_2, Save_Raw_Data_2\
            ,Data_Plot_3, Save_Data_BP_3, Save_Data_BS_3, Save_Output_3 \
            , Input_3, Hasil_BP_3, Hasil_BS_3, Hasil_LP_3, Output_3, Save_Raw_Data_3\
            ,Data_Plot_4, Save_Data_BP_4, Save_Data_BS_4, Save_Output_4 \
            , Input_4, Hasil_BP_4, Hasil_BS_4, Hasil_LP_4, Output_4, Save_Raw_Data_4
        # Definisi Awal
        Input_1[CHUNK:] = Chan_1()
        Input_2[CHUNK:] = Chan_2()
        Input_3[CHUNK:] = Chan_3()
        Input_4[CHUNK:] = Chan_4()

        # Variabel
        start = CHUNK
        end = 2*CHUNK

        # Filter
        for n in range(start, end):
            Hasil_BP_1[n] = abs(Amplifier * (Filter_BP_1.filter(Input_1[n])))
            Hasil_BP_2[n] = abs(Amplifier * (Filter_BP_2.filter(Input_2[n])))
            Hasil_BP_3[n] = abs(Amplifier * (Filter_BP_3.filter(Input_3[n])))
            Hasil_BP_4[n] = abs(Amplifier * (Filter_BP_4.filter(Input_4[n])))
        for n in range(start, end):
            Hasil_BS_1[n] = Filter_BS_1.filter(Hasil_BP_1[n])
            Hasil_BS_2[n] = Filter_BS_2.filter(Hasil_BP_2[n])
            Hasil_BS_3[n] = Filter_BS_3.filter(Hasil_BP_3[n])
            Hasil_BS_4[n] = Filter_BS_4.filter(Hasil_BP_4[n])
        for n in range(start, end):
            Hasil_LP_1[n] = Filter_LP_1.filter((Hasil_BS_1[n]) - Offset_1)
            Hasil_LP_2[n] = Filter_LP_2.filter((Hasil_BS_2[n]) - Offset_2)
            Hasil_LP_3[n] = Filter_LP_3.filter((Hasil_BS_3[n]) - Offset_3)
            Hasil_LP_4[n] = Filter_LP_4.filter((Hasil_BS_4[n]) - Offset_4)


        # Shift Data
        Input_1 = np.roll(Input_1, CHUNK)
        Input_2 = np.roll(Input_2, CHUNK)
        Input_3 = np.roll(Input_3, CHUNK)
        Input_4 = np.roll(Input_4, CHUNK)
        Hasil_BP_1 = np.roll(Hasil_BP_1, CHUNK)
        Hasil_BP_2 = np.roll(Hasil_BP_2, CHUNK)
        Hasil_BP_3 = np.roll(Hasil_BP_3, CHUNK)
        Hasil_BP_4 = np.roll(Hasil_BP_4, CHUNK)
        Hasil_BS_1 = np.roll(Hasil_BS_1, CHUNK)
        Hasil_BS_2 = np.roll(Hasil_BS_2, CHUNK)
        Hasil_BS_3 = np.roll(Hasil_BS_3, CHUNK)
        Hasil_BS_4 = np.roll(Hasil_BS_4, CHUNK)
        Hasil_LP_1 = np.roll(Hasil_LP_1, CHUNK)
        Hasil_LP_2 = np.roll(Hasil_LP_2, CHUNK)
        Hasil_LP_3 = np.roll(Hasil_LP_3, CHUNK)
        Hasil_LP_4 = np.roll(Hasil_LP_4, CHUNK)
        Output_1 = Hasil_LP_1[:CHUNK]
        Output_2 = Hasil_LP_2[:CHUNK]
        Output_3 = Hasil_LP_3[:CHUNK]
        Output_4 = Hasil_LP_4[:CHUNK]

        #  Preparation Plot
        Data_Plot_1 = np.concatenate([Data_Plot_1, Output_1])
        Data_Plot_2 = np.concatenate([Data_Plot_2, Output_2])
        Data_Plot_3 = np.concatenate([Data_Plot_3, Output_3])
        Data_Plot_4 = np.concatenate([Data_Plot_4, Output_4])
        # Remove Old Data
        if len(Data_Plot_1) > MAX_PLOT_SIZE:
            Data_Plot_1 = Data_Plot_1[CHUNK:]
        if len(Data_Plot_2) > MAX_PLOT_SIZE:
            Data_Plot_2 = Data_Plot_2[CHUNK:]
        if len(Data_Plot_3) > MAX_PLOT_SIZE:
            Data_Plot_3 = Data_Plot_3[CHUNK:]
        if len(Data_Plot_4) > MAX_PLOT_SIZE:
            Data_Plot_4 = Data_Plot_4[CHUNK:]

        # Plot Data
        data1_curve.setData(Data_Plot_1)
        data2_curve.setData(Data_Plot_2)
        data3_curve.setData(Data_Plot_3)
        data4_curve.setData(Data_Plot_4)

        # Save Data
        Save_Raw_Data_1 = np.concatenate([Save_Raw_Data_1, Input_1[:CHUNK]])
        Save_Raw_Data_2 = np.concatenate([Save_Raw_Data_2, Input_2[:CHUNK]])
        Save_Raw_Data_3 = np.concatenate([Save_Raw_Data_3, Input_3[:CHUNK]])
        Save_Raw_Data_4 = np.concatenate([Save_Raw_Data_4, Input_4[:CHUNK]])
        Save_Data_BP_1 = np.concatenate([Save_Data_BP_1, Hasil_BP_1[:CHUNK]])
        Save_Data_BP_2 = np.concatenate([Save_Data_BP_2, Hasil_BP_2[:CHUNK]])
        Save_Data_BP_3 = np.concatenate([Save_Data_BP_3, Hasil_BP_3[:CHUNK]])
        Save_Data_BP_4 = np.concatenate([Save_Data_BP_4, Hasil_BP_4[:CHUNK]])
        Save_Data_BS_1 = np.concatenate([Save_Data_BS_1, Hasil_BS_1[:CHUNK]])
        Save_Data_BS_2 = np.concatenate([Save_Data_BS_2, Hasil_BS_2[:CHUNK]])
        Save_Data_BS_3 = np.concatenate([Save_Data_BS_3, Hasil_BS_3[:CHUNK]])
        Save_Data_BS_4 = np.concatenate([Save_Data_BS_4, Hasil_BS_4[:CHUNK]])
        Save_Output_1 = np.concatenate([Save_Output_1, Output_1])
        Save_Output_2 = np.concatenate([Save_Output_2, Output_2])
        Save_Output_3 = np.concatenate([Save_Output_3, Output_3])
        Save_Output_4 = np.concatenate([Save_Output_4, Output_4])
    def Start_Plot():
        global timer
        timer.start()
    def Stop_Plot():
        global timer
        timer.stop()
    def Writer():
        global Data_Plot_1, Save_Data_BP_1, Save_Data_BS_1, Save_Output_1 \
            , Input_1, Hasil_BP_1, Hasil_BS_1, Hasil_LP_1, Output_1, Save_Raw_Data_1\
            ,Data_Plot_2, Save_Data_BP_2, Save_Data_BS_2, Save_Output_2 \
            , Input_2, Hasil_BP_2, Hasil_BS_2, Hasil_LP_2, Output_2, Save_Raw_Data_2\
            ,Data_Plot_3, Save_Data_BP_3, Save_Data_BS_3, Save_Output_3 \
            , Input_3, Hasil_BP_3, Hasil_BS_3, Hasil_LP_3, Output_3, Save_Raw_Data_3\
            ,Data_Plot_4, Save_Data_BP_4, Save_Data_BS_4, Save_Output_4 \
            , Input_4, Hasil_BP_4, Hasil_BS_4, Hasil_LP_4, Output_4, Save_Raw_Data_4
        import csv
        import os
        from itertools import izip



        nama = str(gui_plot.nama.text())
        usia = str(gui_plot.usia.value())
        kelamin = str(gui_plot.kelamin.currentText())
        Channel1 = str(gui_plot.Channel_1.currentText())
        Channel2 = str(gui_plot.Channel_2.currentText())
        Channel3 = str(gui_plot.Channel_3.currentText())
        Channel4 = str(gui_plot.Channel_4.currentText())
        # Sinyal Akhir
        CSV_Output_1 = 'EMG_Channel_1' + '_' + Channel1 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Output_2 = 'EMG_Channel_2' + '_' + Channel2 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Output_3 = 'EMG_Channel_3' + '_' + Channel3 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Output_4 = 'EMG_Channel_4' + '_' + Channel4 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'

        ofile_Output_1 = open(CSV_Output_1, 'wb')
        writer_Output_1 = csv.writer(ofile_Output_1, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        ofile_Output_2 = open(CSV_Output_2, 'wb')
        writer_Output_2 = csv.writer(ofile_Output_2, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        ofile_Output_3 = open(CSV_Output_3, 'wb')
        writer_Output_3 = csv.writer(ofile_Output_3, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        ofile_Output_4 = open(CSV_Output_4, 'wb')
        writer_Output_4 = csv.writer(ofile_Output_4, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)

        writer_Output_1.writerow(Save_Output_1)
        writer_Output_2.writerow(Save_Output_2)
        writer_Output_3.writerow(Save_Output_3)
        writer_Output_4.writerow(Save_Output_4)

        ofile_Output_1.close()
        ofile_Output_2.close()
        ofile_Output_3.close()
        ofile_Output_4.close()

        # Sinyal Awal
        CSV_Raw_Data_1 = 'Raw_Channel_1' + '_' + Channel1 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Raw_Data_2 = 'Raw_Channel_2' + '_' + Channel2 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Raw_Data_3 = 'Raw_Channel_3' + '_' + Channel3 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Raw_Data_4 = 'Raw_Channel_4' + '_' + Channel4 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'

        ofile_Raw_Data_1 = open(CSV_Raw_Data_1, 'wb')
        writer_Raw_Data_1 = csv.writer(ofile_Raw_Data_1, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        ofile_Raw_Data_2 = open(CSV_Raw_Data_2, 'wb')
        writer_Raw_Data_2 = csv.writer(ofile_Raw_Data_2, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        ofile_Raw_Data_3 = open(CSV_Raw_Data_3, 'wb')
        writer_Raw_Data_3 = csv.writer(ofile_Raw_Data_3, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        ofile_Raw_Data_4 = open(CSV_Raw_Data_4, 'wb')
        writer_Raw_Data_4 = csv.writer(ofile_Raw_Data_4, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)

        writer_Raw_Data_1.writerow(Save_Raw_Data_1)
        writer_Raw_Data_2.writerow(Save_Raw_Data_2)
        writer_Raw_Data_3.writerow(Save_Raw_Data_3)
        writer_Raw_Data_4.writerow(Save_Raw_Data_4)

        ofile_Raw_Data_1.close()
        ofile_Raw_Data_2.close()
        ofile_Raw_Data_3.close()
        ofile_Raw_Data_4.close()

        # Sinyal Bandpass
        CSV_Bandpass_1 = 'Bandpass_Channel_1' + '_' + Channel1 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Bandpass_2 = 'Bandpass_Channel_2' + '_' + Channel2 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Bandpass_3 = 'Bandpass_Channel_3' + '_' + Channel3 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Bandpass_4 = 'Bandpass_Channel_4' + '_' + Channel4 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'

        ofile_Bandpass_1 = open(CSV_Bandpass_1, 'wb')
        writer_Bandpass_1 = csv.writer(ofile_Bandpass_1, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
        ofile_Bandpass_2 = open(CSV_Bandpass_2, 'wb')
        writer_Bandpass_2 = csv.writer(ofile_Bandpass_2, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
        ofile_Bandpass_3 = open(CSV_Bandpass_3, 'wb')
        writer_Bandpass_3 = csv.writer(ofile_Bandpass_3, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
        ofile_Bandpass_4 = open(CSV_Bandpass_4, 'wb')
        writer_Bandpass_4 = csv.writer(ofile_Bandpass_4, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)

        writer_Bandpass_1.writerow(Save_Data_BP_1)
        writer_Bandpass_2.writerow(Save_Data_BP_2)
        writer_Bandpass_3.writerow(Save_Data_BP_3)
        writer_Bandpass_4.writerow(Save_Data_BP_4)

        ofile_Bandpass_1.close()
        ofile_Bandpass_2.close()
        ofile_Bandpass_3.close()
        ofile_Bandpass_4.close()

        # Sinyal Bandstop
        CSV_Bandstop_1 = 'Bandstop_Channel_1' + '_' + Channel1 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Bandstop_2 = 'Bandstop_Channel_2' + '_' + Channel2 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Bandstop_3 = 'Bandstop_Channel_3' + '_' + Channel3 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'
        CSV_Bandstop_4 = 'Bandstop_Channel_4' + '_' + Channel4 + '_' + nama + '_' + usia + '_' + kelamin + '.csv'

        ofile_Bandstop_1 = open(CSV_Bandstop_1, 'wb')
        writer_Bandstop_1 = csv.writer(ofile_Bandstop_1, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_ALL)
        ofile_Bandstop_2 = open(CSV_Bandstop_2, 'wb')
        writer_Bandstop_2 = csv.writer(ofile_Bandstop_2, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_ALL)
        ofile_Bandstop_3 = open(CSV_Bandstop_3, 'wb')
        writer_Bandstop_3 = csv.writer(ofile_Bandstop_3, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_ALL)
        ofile_Bandstop_4 = open(CSV_Bandstop_4, 'wb')
        writer_Bandstop_4 = csv.writer(ofile_Bandstop_4, delimiter=',', quotechar='"',
                                       quoting=csv.QUOTE_ALL)

        writer_Bandstop_1.writerow(Save_Data_BS_1)
        writer_Bandstop_2.writerow(Save_Data_BS_2)
        writer_Bandstop_3.writerow(Save_Data_BS_3)
        writer_Bandstop_4.writerow(Save_Data_BS_4)

        ofile_Bandstop_1.close()
        ofile_Bandstop_2.close()
        ofile_Bandstop_3.close()
        ofile_Bandstop_4.close()


        src = "D:\OneDrive\Documents\Skripsi\Program EMG"
        direct = "D:\OneDrive\Documents\Skripsi\Program EMG\Record Data"

        # EMG Akhir
        src_Output_1 = os.path.join(src, CSV_Output_1)
        direct_Output_1 = os.path.join(direct, CSV_Output_1)
        src_Output_2 = os.path.join(src, CSV_Output_2)
        direct_Output_2 = os.path.join(direct, CSV_Output_2)
        src_Output_3 = os.path.join(src, CSV_Output_3)
        direct_Output_3 = os.path.join(direct, CSV_Output_3)
        src_Output_4 = os.path.join(src, CSV_Output_4)
        direct_Output_4 = os.path.join(direct, CSV_Output_4)
        csv.writer(open(direct_Output_1, "wb")).writerows(izip(*csv.reader(open(src_Output_1, "rb"))))
        csv.writer(open(direct_Output_2, "wb")).writerows(izip(*csv.reader(open(src_Output_2, "rb"))))
        csv.writer(open(direct_Output_3, "wb")).writerows(izip(*csv.reader(open(src_Output_3, "rb"))))
        csv.writer(open(direct_Output_4, "wb")).writerows(izip(*csv.reader(open(src_Output_4, "rb"))))

        os.remove(src_Output_1)
        os.remove(src_Output_2)
        os.remove(src_Output_3)
        os.remove(src_Output_4)

        # Raw Data
        src_Raw_Data_1 = os.path.join(src, CSV_Raw_Data_1)
        direct_Raw_Data_1 = os.path.join(direct, CSV_Raw_Data_1)
        src_Raw_Data_2 = os.path.join(src, CSV_Raw_Data_2)
        direct_Raw_Data_2 = os.path.join(direct, CSV_Raw_Data_2)
        src_Raw_Data_3 = os.path.join(src, CSV_Raw_Data_3)
        direct_Raw_Data_3 = os.path.join(direct, CSV_Raw_Data_3)
        src_Raw_Data_4 = os.path.join(src, CSV_Raw_Data_4)
        direct_Raw_Data_4 = os.path.join(direct, CSV_Raw_Data_4)
        csv.writer(open(direct_Raw_Data_1, "wb")).writerows(izip(*csv.reader(open(src_Raw_Data_1, "rb"))))
        csv.writer(open(direct_Raw_Data_2, "wb")).writerows(izip(*csv.reader(open(src_Raw_Data_2, "rb"))))
        csv.writer(open(direct_Raw_Data_3, "wb")).writerows(izip(*csv.reader(open(src_Raw_Data_3, "rb"))))
        csv.writer(open(direct_Raw_Data_4, "wb")).writerows(izip(*csv.reader(open(src_Raw_Data_4, "rb"))))

        os.remove(src_Raw_Data_1)
        os.remove(src_Raw_Data_2)
        os.remove(src_Raw_Data_3)
        os.remove(src_Raw_Data_4)

        # Bandpass
        src_Bandpass_1 = os.path.join(src, CSV_Bandpass_1)
        direct_Bandpass_1 = os.path.join(direct, CSV_Bandpass_1)
        src_Bandpass_2 = os.path.join(src, CSV_Bandpass_2)
        direct_Bandpass_2 = os.path.join(direct, CSV_Bandpass_2)
        src_Bandpass_3 = os.path.join(src, CSV_Bandpass_3)
        direct_Bandpass_3 = os.path.join(direct, CSV_Bandpass_3)
        src_Bandpass_4 = os.path.join(src, CSV_Bandpass_4)
        direct_Bandpass_4 = os.path.join(direct, CSV_Bandpass_4)
        csv.writer(open(direct_Bandpass_1, "wb")).writerows(izip(*csv.reader(open(src_Bandpass_1, "rb"))))
        csv.writer(open(direct_Bandpass_2, "wb")).writerows(izip(*csv.reader(open(src_Bandpass_2, "rb"))))
        csv.writer(open(direct_Bandpass_3, "wb")).writerows(izip(*csv.reader(open(src_Bandpass_3, "rb"))))
        csv.writer(open(direct_Bandpass_4, "wb")).writerows(izip(*csv.reader(open(src_Bandpass_4, "rb"))))

        os.remove(src_Bandpass_1)
        os.remove(src_Bandpass_2)
        os.remove(src_Bandpass_3)
        os.remove(src_Bandpass_4)

        # Bandstop
        src_Bandstop_1 = os.path.join(src, CSV_Bandstop_1)
        direct_Bandstop_1 = os.path.join(direct, CSV_Bandstop_1)
        src_Bandstop_2 = os.path.join(src, CSV_Bandstop_2)
        direct_Bandstop_2 = os.path.join(direct, CSV_Bandstop_2)
        src_Bandstop_3 = os.path.join(src, CSV_Bandstop_3)
        direct_Bandstop_3 = os.path.join(direct, CSV_Bandstop_3)
        src_Bandstop_4 = os.path.join(src, CSV_Bandstop_4)
        direct_Bandstop_4 = os.path.join(direct, CSV_Bandstop_4)
        csv.writer(open(direct_Bandstop_1, "wb")).writerows(izip(*csv.reader(open(src_Bandstop_1, "rb"))))
        csv.writer(open(direct_Bandstop_2, "wb")).writerows(izip(*csv.reader(open(src_Bandstop_2, "rb"))))
        csv.writer(open(direct_Bandstop_3, "wb")).writerows(izip(*csv.reader(open(src_Bandstop_3, "rb"))))
        csv.writer(open(direct_Bandstop_4, "wb")).writerows(izip(*csv.reader(open(src_Bandstop_4, "rb"))))

        os.remove(src_Bandstop_1)
        os.remove(src_Bandstop_2)
        os.remove(src_Bandstop_3)
        os.remove(src_Bandstop_4)

    timer = QtCore.QTimer()
    timer.timeout.connect(Plot)
    gui_plot.Start.clicked.connect(Start_Plot)
    gui_plot.STOP.clicked.connect(Stop_Plot)
    gui_plot.RECORD.clicked.connect(Writer)
    form.showMaximized()
    form.show()
    form.update()
    app.exec_()