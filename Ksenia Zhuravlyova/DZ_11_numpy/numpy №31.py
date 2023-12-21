#Как игнорировать все предупреждения о numpy (не рекомендуется)

import numpy as np

np.seterr(all='ignore')
a = np.arange(3) / 0

# np.seterr(all='warn')
print(a)

