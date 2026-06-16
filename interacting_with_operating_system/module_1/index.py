import shutil
import psutil

du = shutil.disk_usage("/")
print(du)


# Print the percentage of free space
print(f"Percentage of free space: {du.free/du.total*100:.2f}%")



print(psutil.cpu_percent(0.1)) 