# Как получить все даты, соответствующие июлю месяцу 2016

import numpy as np

june_2016 = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(june_2016)