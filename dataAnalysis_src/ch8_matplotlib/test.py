import matplotlib.pyplot as plt
import numpy as np
from __builtin__ import range
#plt.plot(np.arange(10))

fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
#ax4=fig.add_subplot(2,2,4)

plt.plot(np.random.randn(50).cumsum(),'k--')

ax1.hist(np.random.randn(30),bins=20,color='k',alpha=0.3)

ax2.scatter(np.arange(30),np.arange(30) + 3 * np.random.randn(30))

fig,axes=plt.subplots(2,3)

fig,axes=plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
    
plt.subplots_adjust(wspace=0,hspace=0)



data=np.random.randn(30).cumsum()
plt.plot(data,'k--',label='Default')
plt.plot(data,'k--',drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')


fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
ticks=ax.set_xticks([0,250,500,750,1000])
labels=ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
ax.set_ylabel('data length')


fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(),'k',label='one')
ax.plot(np.random.randn(1000).cumsum(),'g',label='two')
ax.plot(np.random.randn(1000).cumsum(),'r',label='three')
ax.legend(loc='best')


fig=plt.figure()
ax=fig.add_subplot(1,1,1)
rect=plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)
circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)
pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

plt.savefig('figpath.svg')
plt.savefig('figpath.pdf')
plt.savefig('figpath.png',dpi=400,bbox_inches='tight')

from io import StringIO
buffer1=StringIO()
plt.savefig(buffer1)
plot_data=buffer.getvalue()
















