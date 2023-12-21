# Как получить даты вчера, сегодня и завтра

import numpy as np
from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(today)
print(tomorrow)
print(yesterday)
