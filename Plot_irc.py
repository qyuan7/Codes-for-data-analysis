import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
def plot_irc(coord, energy):
    
    """
    Args:
        coord (1d-array) - reaction coordinates (float)
        energy - energy for the reaction coordinates(float)
    Returns:
        matplotlib scatter plot of IRC
    """
    s = 75
    lw = 0
    alpha = 0.5
    coord_color = 'orange'
    coord_marker = 's'
    axis_width = 1.5
    maj_tick_len = 6
    fontsize = 16
    label = '__nolegend__'
    ax = plt.scatter(coord, energy,
                     marker=coord_marker, color=coord_color, s=s, 
                     lw=lw, alpha=alpha,label=None)

    ax = plt.legend(frameon=False, fontsize=fontsize, handletextpad=0.4)    
    xmin = np.min(coord)-0.2
    xmax = np.max(coord)+0.2
    ymin = np.min(energy)-0.001
    ymax = np.max(energy)+0.001    
    ax = plt.xlim([xmin, xmax])
    ax = plt.ylim([ymin, ymax])
    ax = plt.plot(coord,energy, 
                  lw=axis_width, color='black', ls='--', 
                  label='__nolegend__')
    ax = plt.xlabel('Reaction Coordinate', fontsize=fontsize)
    ax = plt.ylabel('Energy', fontsize=fontsize)
    ax = plt.xticks(fontsize=fontsize)
    ax = plt.yticks(fontsize=fontsize)
    ax = plt.tick_params('both', length=maj_tick_len, width=axis_width, 
                         which='major', right=True, top=True)
    return ax  
    
ts_1st = pd.read_csv('1st_ts_irc.csv')
ts_scan2 = pd.read_csv('scan2_ts_irc.csv')
ts_re = pd.read_csv('reshape_16_ts_irc.csv')
coord_1st = ts_1st['X']
eng_1st = ts_1st['Y']
coord_2nd, eng_2nd = ts_scan2['X'], ts_scan2['Y']
coord_3rd, eng_3rd = ts_re['X'], ts_re['Y']
ax = plot_irc(coord_3rd, eng_3rd)
plt.title('TS for pathway 3')
plt.show()
