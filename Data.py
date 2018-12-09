from NIDAQ_1 import *
from NIDAQ_2 import *
from NIDAQ_3 import *
from NIDAQ_4 import *
from Coefficient import *

def Chan_1(points=CHUNK):
    SetupTask1()
    StartTask1()
    data = ReadSamples1(points)
    StopAndClearTask1()
    return data
def Chan_2(points=CHUNK):
    SetupTask2()
    StartTask2()
    data = ReadSamples2(points)
    StopAndClearTask2()
    return data
def Chan_3(points=CHUNK):
    SetupTask3()
    StartTask3()
    data = ReadSamples3(points)
    StopAndClearTask3()
    return data
def Chan_4(points=CHUNK):
    SetupTask4()
    StartTask4()
    data = ReadSamples4(points)
    StopAndClearTask4()
    return data