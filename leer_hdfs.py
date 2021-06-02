import subprocess
cat = subprocess.Popen(["hadoop", "fs", "-cat", "/excel/excel.xlsx"], stdout=subprocess.PIPE)
for line in cat.stdout: print(line)
