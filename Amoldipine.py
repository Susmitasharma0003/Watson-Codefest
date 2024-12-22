import numpy as np
# Define the decay equation function
def amlodipine_decay(dose_start,dose_end): 
    bioavailability = 0.70  # 70%
    V_d = 21  
    t_half = 45  
    C0 = (bioavailability * dose_start) / V_d
    ct = (bioavailability * dose_end) / V_d
    lambda_val = np.log(2) / t_half

    return np.log(ct/C0) /(-lambda_val)

