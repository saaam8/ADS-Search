
import numpy as np
import time

# إعداد بيانات ضخمة
x, y, z = 1000, 1000, 10
data = np.zeros((x, y, z))
for i in range(x):
    for j in range(y):
        for k in range(z):
            data[i, j, k] = i - j + np.random.normal(0, 8) + k * 12

# تقسيم البيانات وتنفيذ الخوارزمية
divisions = np.array_split(data, 20, axis=0)
for idx, d in enumerate(divisions):
    mean_val = np.mean(d)
    steering = "asc-horizontal" if mean_val < 0 else "desc-vertical"
    start = time.time()
    max_val = np.max(d)
    end = time.time()
    print(f"Division {idx+1} | Steering: {steering} | Max: {max_val:.2f} | Time: {end - start:.3f}s")
