import numpy as np
import matplotlib.pyplot as plt 
#from matplotlib import rcParams
#rcParams.update({'figure.autolayout': True})

column0 = []
column1 = []
column2 = []
for line in open("pulse.txt", 'r'):
    try:
        a, b, c, d, e = line.split()
        column0.append(a)
        column1.append(int(c))
        column2.append(int(d))
        print(a+' # '+b+' # '+c+' # '+d+' # '+e)
    except ValueError:
        pass

fig, ax = plt.subplots() 
 
plt.gcf().subplots_adjust(left = 0.25, bottom = 0.2)
#plt.tight_layout()
 

for i in range(len(column1)):
    ax.hlines(i, [0], -1*column2[i], color='cyan', linewidth=3.0)
    ax.hlines(i, [0], column1[i], color='green', linewidth=3.0)

y_pos = np.arange(len(column0))

ax.set_yticks(y_pos)
ax.set_yticklabels(column0)
ax.set_xlabel('Blutdruck')
ax.set_ylabel('Datum', loc=('top'),rotation=0)
ax.set_title('Blutdruck über Zeit')


plt.figtext(0.35, 0.1, "DIA", ha="center", 
            fontsize=12, bbox={"facecolor":"cyan", "alpha":0.5, "pad":5})
plt.figtext(0.7, 0.1, "SYS", ha="center", 
            fontsize=12, bbox={"facecolor":"green", "alpha":0.5, "pad":5})


plt.xticks(np.arange(-100,150,20))
ax.grid(True)
#plt.xlim(-100, 150)

plt.show() 

#cmd /K cd "$(CURRENT_DIRECTORY)"&python "$(FULL_CURRENT_PATH)"&pause&exit
