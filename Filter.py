import BP_1
import BP_2
import BP_3
import BP_4
import BS_1
import BS_2
import BS_3
import BS_4
import LP_1
import LP_2
import LP_3
import LP_4
from Coefficient import *


Filter_BP_1 = BP_1.IIR2Filter()
Filter_BP_2 = BP_2.IIR2Filter()
Filter_BP_3 = BP_3.IIR2Filter()
Filter_BP_4 = BP_4.IIR2Filter()
Filter_BS_1 = BS_1.IIR2Filter()
Filter_BS_2 = BS_2.IIR2Filter()
Filter_BS_3 = BS_3.IIR2Filter()
Filter_BS_4 = BS_4.IIR2Filter()
Filter_LP_1 = LP_1.IIR2Filter()
Filter_LP_2 = LP_2.IIR2Filter()
Filter_LP_3 = LP_3.IIR2Filter()
Filter_LP_4 = LP_4.IIR2Filter()

BP_pass_1_prewarp = float(BP_pass_1) / float(Fs*0.5)
BS_pass_1_prewarp = float(BS_pass_1) / float(Fs*0.5)
BP_pass_2_prewarp = float(BP_pass_2) / float(Fs*0.5)
BS_pass_2_prewarp = float(BS_pass_2) / float(Fs*0.5)
LP_prewarp = float(LP) / float(Fs*0.5)
Filter_BP_1.bandPass(orde_BP,BP_pass_1_prewarp,BP_pass_2_prewarp)
Filter_BS_1.bandStop(orde_BS,BS_pass_1_prewarp,BS_pass_2_prewarp)
Filter_LP_1.lowPass(orde_LP,LP_prewarp)
Filter_BP_2.bandPass(orde_BP,BP_pass_1_prewarp,BP_pass_2_prewarp)
Filter_BS_2.bandStop(orde_BS,BS_pass_1_prewarp,BS_pass_2_prewarp)
Filter_LP_2.lowPass(orde_LP,LP_prewarp)
Filter_BP_3.bandPass(orde_BP,BP_pass_1_prewarp,BP_pass_2_prewarp)
Filter_BS_3.bandStop(orde_BS,BS_pass_1_prewarp,BS_pass_2_prewarp)
Filter_LP_3.lowPass(orde_LP,LP_prewarp)
Filter_BP_4.bandPass(orde_BP,BP_pass_1_prewarp,BP_pass_2_prewarp)
Filter_BS_4.bandStop(orde_BS,BS_pass_1_prewarp,BS_pass_2_prewarp)
Filter_LP_4.lowPass(orde_LP,LP_prewarp)



