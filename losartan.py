import numpy as np

def losartan_decay(dose_start,dose_end):
    bioavailability = 0.33  # 33%
    V_d = 34  
    t_half = 2 # in hours
    C0 = (bioavailability * dose_start) / V_d
    ct = (bioavailability * dose_end) / V_d
    lambda_val = np.log(2) / t_half
    return np.log(ct/C0) /(-lambda_val)




