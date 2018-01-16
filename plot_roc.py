#! usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt
result_file = pd.read_csv('strobi_iso_ap_valili.csv')
y = result_file.Col2
score = result_file.Score2
y = y.as_matrix()
roc_x = []
roc_y = []
#thr = np.linspace(min_score, max_score, 70)
FP=0
TP=0
P = sum(y)
N = len(y) - P

for (i, T) in enumerate(score):
    for i in range(0, len(score)):
        if (score[i] > T):
            if (y[i]==1):
                TP = TP + 1
            if (y[i]==0):
                FP = FP + 1
    roc_x.append(FP/float(N))
    roc_y.append(TP/float(P))
    FP=0
    TP=0
roc_x.append(1); roc_y.append(1)
a = [0,1]; b=[0,1]
plt.xlim(-0.001,1)
plt.ylim(0,1)
plt.plot(a, b,'--')
#plt.scatter(roc_x, roc_y)
plt.plot(roc_x, roc_y, c='red')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.savefig('bayesian_roc.png', bbox_inches='tight', transparent=True)
plt.show()
