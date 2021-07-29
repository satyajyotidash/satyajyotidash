import filecmp

f1="logfile.txt"
f2="somefile.txt"
# shallow comparison
result = filecmp.cmp(f1,f2,shallow=True)
print("shallow comp :: ",result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print("Deep comp :: ",result)
