import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import glob

all_pep=sorted(glob.glob('Seq*/'))
print(all_pep)
modified_list = [s[:-1] for s in all_pep]
print(modified_list)
sorted_pep = sorted(modified_list, key=lambda x: int(x[3:]))
print(sorted_pep)
f=open('count.dat').readlines()
clean=[]
for i in f:
    i=i.strip()
    clean.append(i)

D1=[]
D2=[]
for i in range(len(sorted_pep)):
    seg=clean[i*len(sorted_pep):(i+1)*len(sorted_pep)]
    for j in seg:
        D1.append(float(j.split()[2]))
    D2.append(D1)
    D1=[]
table=np.array(D2)

aa=table/10.
aa= np.where(aa<0.5, aa-1, aa)
np.fill_diagonal(aa, 0)
plt.figure(figsize=(10,10))
plt.imshow(aa, cmap="coolwarm", interpolation="nearest", origin="upper",alpha=0.7,vmin=-1, vmax=1)
#plt.imshow(aa, cmap="GnBu", interpolation="nearest", origin="upper",alpha=0.7,vmin=-1, vmax=1)


x_ticks = np.arange(1, aa.shape[1]+1, 1)
x_label=sorted_pep
plt.yticks(x_ticks-1, x_label)
plt.xticks(x_ticks-1, x_label,rotation=90)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

rows, cols = aa.shape

# Draw cell borders inside each cell
for i in range(rows):
    for j in range(cols):
        plt.gca().add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, edgecolor='white',alpha=1.0))
colorbar=plt.colorbar(shrink=0.82, norm = mpl.colors.Normalize(vmin=-1, vmax=1))
colorbar.ax.tick_params(labelsize=11) 
plt.savefig('top.pdf')
#plt.show()
