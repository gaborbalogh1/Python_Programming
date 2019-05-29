import shutil
from pathlib import Path

dirs = Path('/Users')
diskinfo = shutil.disk_usage(dirs)

drive = Path('/Users')

print(drive.stat().st_mode)
print(diskinfo)
