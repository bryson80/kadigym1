import pandas as pd
import numpy as np
from metpy.calc import lcl, parcel_profile, cape_cin, mixing_ratio
import matplotlib.pyplot as plt
from metpy.plots import SkewT
from metpy.units import units

file_path = pd.read_csv(
    "/Users/mac/Documents/Documents/KADI GYM/Daily-rainfall-data-plot/tephi 3.csv", encoding='latin1')

temp = (file_path.columns[3])
dew = (file_path.columns[4])

p = np.linspace(1000, 100, 37) * units.hPa

fig = plt.figure(figsize=(9, 9))
skew = SkewT(fig)

u = np.linspace(10, 50, 37) * units.knots  # u-component of wind
v = np.linspace(5, 25, 37) * units.knots   # v-component of wind

skew.plot(file_path['P(hPa)'].values * units.hPa,
          file_path[temp].values * units.degC, 'r', label='T(°C)')

skew.plot(file_path['P(hPa)'].values * units.hPa,
          file_path[dew].values * units.degC, 'g', label='DP(°C)')

skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

skew.plot_barbs(p, u, v)

plt.title('Tephigram for Nairobi upper air')
plt.legend()
