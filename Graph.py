import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 10))

# ===================
# 1. Scatter Plot
# ===================
plt.subplot(3,3,1)
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y, c=y, cmap='viridis')
plt.colorbar()
plt.title("My First Chart")
plt.xlabel("X")
plt.ylabel("Y")

# ------------------
# 2 Bubble Plot
# ------------------
plt.subplot(3,3,2)

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(
    x,
    y,
    c=colors,
    s=sizes,
    alpha=0.5,
    cmap='nipy_spectral'
)

plt.colorbar()

plt.title("My First Chart")
plt.xlabel("X")
plt.ylabel("Y")

# ===================
# 3. Horizontal Line
# ===================
plt.subplot(3,3,3)
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.title("My First Chart")
plt.xlabel("X")
plt.ylabel("Y")

# ===================
# 4. Line Plot
# ===================
plt.subplot(3,3,4)
x = [0,2,4,6,8,10]
y = [0,2,4,6,8,10]

plt.plot(x, y)
plt.grid()
plt.title("My First Chart")
plt.xlabel("X")
plt.ylabel("Y")

# ===================
# 5. Multiple Line
# ===================
# ------------------
# 5 Multiple Line Plot
# ------------------
plt.subplot(3,3,5)

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.title("My First Chart")
plt.xlabel("X")
plt.ylabel("Y")


# ===================
# 6. Line with Marker
# ===================
# ------------------
# 6 Line Plot with Marker
# ------------------
plt.subplot(3,3,6)

x = [0,1,2,3]
y = [3,8,1,10]

plt.plot(
    x,
    y,
    marker='o',
    ms=20,          # ขนาดจุด
    mfc='hotpink',  # สีด้านในจุด
    mec='hotpink'   # สีขอบจุด
)

plt.title("My First Chart")
plt.xlabel("X")
plt.ylabel("Y")

# ===================
# 7. Histogram
# ===================
plt.subplot(3,3,7)

x = np.random.normal(170, 10, 250)

plt.hist(x)

plt.title("My First Chart")
plt.xlabel("Value")
plt.ylabel("Frequency")

# ===================
# 8. Pie Chart Explode
# ===================
plt.subplot(3,3,8)

sizes = [35,25,25,15]
labels = ['Apple','Orange',
          'Grapes','Banana']

explode = (0.1,0,0,0)

plt.pie(
    sizes,
    labels=labels,
    explode=explode,
    autopct='%1.1f%%'
)

plt.title("My First Chart")

# ===================
# 9. Pie Chart Legend
# ===================
plt.subplot(3,3,9)

sizes = [30,25,25,20]
labels = ['Apple','Orange',
          'Grapes','Banana']

plt.pie(sizes, autopct='%1.1f%%')
plt.legend(labels)

plt.title("My First Chart")

plt.tight_layout()
plt.show()