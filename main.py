"""
This is my first project with python
"""

# Percabangan if
jumlah_susu = 0
jumlah_telur = 7
print(f"Jumlah susu {jumlah_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")
if jumlah_susu >1:
    #print("Anak membeli 1 botol susu")
    if jumlah_telur >6:
        print("Anak membeli 1 botol susu dan 6 butir telur")
    else:
        print("Anak membeli 1 botol susu saja")
else:
    print("anak tidak membeli susu dan telur")
