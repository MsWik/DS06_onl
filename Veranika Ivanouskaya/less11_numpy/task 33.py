import numpy as np
#How to get the dates of yesterday, today and tomorrow? (★☆☆)

today = np.datetime64('today', 'D')
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')

print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)