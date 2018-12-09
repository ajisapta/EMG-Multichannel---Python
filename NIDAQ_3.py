import ctypes
import numpy
import time
from time import *
import os
import pprint
import random
import csv  # for writing data into csv files
import sys
from Coefficient import *

# import matplotlib  # library used here for plotting

# matplotlib.use('WXAgg')
# from matplotlib.figure import *
# from matplotlib.backends.backend_wxagg import *
# import pylab
from scipy import *
from pylab import *
import numpy as np
# import matplotlib.pylab as plt
from scipy import signal
import sys

# this loads the dll for the NIDAQ
nidaq = ctypes.windll.nicaiu

# typedefs are setup to correspond to NIDAQmx.h
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32
written = int32()
pointsRead = uInt32()

# constants are setup to correspond to NIDAQmx.h
DAQmx_Val_Volts = 10348
DAQmx_Val_Rising = 10280
DAQmx_Val_Cfg_Default = int32(-1)
DAQmx_Val_ContSamps = 10123
DAQmx_Val_ChanForAllLines = 1
DAQmx_Val_Differential = 10106
DAQmx_Val_Volts = 10348
DAQmx_Val_GroupByScanNumber = 1
DAQmx_Val_FiniteSamps = 10178
DAQmx_Val_GroupByChannel = 0

# adapted with info from .NET and C code in
# http://zone.ni.com/devzone/cda/tut/p/id/5409#toc4


# initialize variables
taskHandle = TaskHandle(0)

# # range of the DAQ
# min1 = float64(0.0)
# max1 = float64(5.0)
# timeout = float64(10.0)
# bufferSize = uInt32(10)
# pointsToRead = bufferSize
# pointsRead = uInt32()
#
# # sampling rate
# sampleRate = float64(200.0)
# samplesPerChan = uInt64(100)
#
# # specifiy the channels
# chan = ctypes.create_string_buffer('Dev1/ai0')
# clockSource = ctypes.create_string_buffer('OnboardClock')
taskHandle = TaskHandle(0)
min1 = float64(-5)
max1 = float64(5)
timeout = float64(10.0)
bufferSize = uInt32(10)
pointsToRead = bufferSize
pointsRead = uInt32()
sampleRate = float64(Fs)
samplesPerChan = uInt64(10000)
chan = ctypes.create_string_buffer('Dev1/ai2')
clockSource = ctypes.create_string_buffer('OnboardClock')
# create a list of zeros for data
data = numpy.zeros((10000,), dtype=numpy.float64)


# set up the task in the required channel and
# fix sampling through internal clock
def SetupTask3():
    nidaq.DAQmxCreateTask("", ctypes.byref(taskHandle))
    nidaq.DAQmxCreateAIVoltageChan(taskHandle, chan, "",
                                   DAQmx_Val_Differential,
                                   min1, max1, DAQmx_Val_Volts, None)
    nidaq.DAQmxCfgSampClkTiming(taskHandle, clockSource, sampleRate,
                                DAQmx_Val_Rising, DAQmx_Val_ContSamps, samplesPerChan)
    nidaq.DAQmxCfgInputBuffer(taskHandle, 20000)


# Start Task
def StartTask3():
    nidaq.DAQmxStartTask(taskHandle)


# Read Samples
def ReadSamples3(points):
    bufferSize = uInt32(points)
    pointsToRead = bufferSize
    data = numpy.zeros((points,), dtype=numpy.float64)
    nidaq.DAQmxReadAnalogF64(taskHandle, pointsToRead, timeout,
                             DAQmx_Val_GroupByScanNumber, data.ctypes.data,
                             uInt32(2 * bufferSize.value), ctypes.byref(pointsRead), None)
    return data


# stop and clear
def StopAndClearTask3():
    if taskHandle.value != 0:
        nidaq.DAQmxStopTask(taskHandle)
        nidaq.DAQmxClearTask(taskHandle)

# On specifying the number of points to be sampled, it gets
# the voltage value and returns it as a list data


