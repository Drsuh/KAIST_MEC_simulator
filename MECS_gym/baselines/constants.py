
# Env params
NUM_EDGE_CORES = 10
NUM_EDGE_SINGLE = 4
NUM_CLOUD_CORES = 54
NUM_CLOUD_SINGLE = 4

# COST_TYPE=1e4
# COST_TYPE=5e4
# COST_TYPE=1e5
# COST_TYPE=1.2e5
# COST_TYPE=1.4e5
# COST_TYPE=1.6e5
# COST_TYPE=1.8e5
# COST_TYPE=2e5
# COST_TYPE=2.2e5
# COST_TYPE=2.4e5
# COST_TYPE=2.6e5
# COST_TYPE=2.8e5
# COST_TYPE=3e5
# COST_TYPE=3.2e5
# COST_TYPE=3.4e5
# COST_TYPE=3.6e5
# COST_TYPE=3.8e5
# COST_TYPE=4e5
# COST_TYPE=5e5
#
#
# disc
# COST_TYPE=1e4
# COST_TYPE=5e4
# COST_TYPE=1e5
# COST_TYPE=1.5e5
# COST_TYPE=2e5
# COST_TYPE=2.5e5
# COST_TYPE=3e5
# COST_TYPE=4e5
#COST_TYPE=5e5
#
# COST_TYPE=1e6
# COST_TYPE=1e7
# COST_TYPE=1e8

# Channels
LTE = 1
WIFI = 2
BT = 3
NFC = 4
WIRED = 5

# Applications
SPEECH_RECOGNITION = 1
NLP = 2
FACE_RECOGNITION = 3
SEARCH_REQ = 4
LANGUAGE_TRANSLATION = 5
PROC_3D_GAME = 6
VR = 7
AR = 8

# Data size scales
BYTE = 8
KB = 1024*BYTE
MB = 1024*KB
GB = 1024*MB
TB = 1024*GB
PB = 1024*TB

# CPU clock frequency scales
KHZ = 1e3
MHZ = KHZ*1e3
GHZ = MHZ*1e3

# Data transmission rate scales
KBPS = 1e3
MBPS = KBPS*1e3
GBPS = MBPS*1e3

# Time scales
MS = 1e-3


'''
arrival rate            Mbps
arrival data size       Mbps
time slot interval      sec (TBD)
Edge computation cap.   3.3*10^2~10^4
'''

def main():
    import numpy as np
    # result =[]
    # for i in range(1,9):
    #     result.append(app_info[i]['workload']*app_info[i]['popularity']*arrival_bits(i, dist='deterministic'))
    # result = np.array(result)/GHZ
    import pdb; pdb.set_trace()

if __name__=='__main__':
    main()
