import numpy as np
CHUNK = 1000
Olah = 50
MAX_PLOT_SIZE = CHUNK*Olah
Amplifier = 1000
Offset_1 = 0
Offset_2 = 0
Offset_3 = 0
Offset_4 = 0
BP_pass_1 = 15
BP_pass_2 = 450
orde_BP = 8
BS_pass_1 = 49.5
BS_pass_2 = 50.5
orde_BS = 6
LP = 5
orde_LP = 1
Fs = 10000.0
Y_max = 60
# Definisi Plot
Data_Plot_1 = []
Data_Plot_2 = []
Data_Plot_3 = []
Data_Plot_4 = []


# Save Data Channel 1
Save_Data_BP_1 = []
Save_Data_BS_1 = []
Save_Output_1 = []
Save_Raw_Data_1 = []

# Save Data Channel 2
Save_Data_BP_2 = []
Save_Data_BS_2 = []
Save_Output_2 = []
Save_Raw_Data_2 = []

# Save Data Channel 3
Save_Data_BP_3 = []
Save_Data_BS_3 = []
Save_Output_3 = []
Save_Raw_Data_3 = []

# Save Data Channel 4
Save_Data_BP_4 = []
Save_Data_BS_4 = []
Save_Output_4 = []
Save_Raw_Data_4 = []

# Channel 1
Input_1    = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BP_1 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BS_1 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_LP_1 = np.zeros(2*CHUNK,dtype=np.float64)
Output_1   = np.zeros(CHUNK,dtype=np.float64)

# Channel 2
Input_2    = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BP_2 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BS_2 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_LP_2 = np.zeros(2*CHUNK,dtype=np.float64)
Output_2   = np.zeros(CHUNK,dtype=np.float64)

# Channel 3
Input_3    = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BP_3 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BS_3 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_LP_3 = np.zeros(2*CHUNK,dtype=np.float64)
Output_3   = np.zeros(CHUNK,dtype=np.float64)

# Channel 4
Input_4    = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BP_4 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_BS_4 = np.zeros(2*CHUNK,dtype=np.float64)
Hasil_LP_4 = np.zeros(2*CHUNK,dtype=np.float64)
Output_4   = np.zeros(CHUNK,dtype=np.float64)