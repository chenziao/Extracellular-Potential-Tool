import numpy as np
import pandas as pd
import cell_inference.config.paths as paths

# GENERAL PARAMETERS USED ACROSS RUNS
TSTOP = 15.  # ms
DT = 0.025  # ms. Change with h.steps_per_ms = 1/h.dt

# ELECTRODE_POSITION = np.column_stack((np.zeros(96),np.linspace(-1900,1900,96),np.zeros(96)))
ELECTRODE_POSITION = pd.read_csv(paths.ELECTRODES).to_numpy()

# LFP PROCESSING
MIN_DISTANCE = 10.0

BUTTERWORTH_ORDER = 2  # 2nd order
FILTER_CRITICAL_FREQUENCY = 100.  # 100 Hz
BANDFILTER_TYPE = 'hp'  # highpass
FILTER_SAMPLING_RATE = 1000. / DT  # 40 kHz
