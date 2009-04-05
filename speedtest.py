from __future__ import division
import sys, time
sys.path.append('pytc-0.7/build/lib.linux-x86_64-2.5')
import pytc

db = pytc.HDB()
db.open("db", pytc.HDBOWRITER | pytc.HDBOCREAT)

numRecords = 100000
t1 = time.time()
for i in range(numRecords):
    s = "%08d" % i
    db.put(s, s)

db.close()
t2 = time.time()
print "%s puts at %s tps" % (numRecords, numRecords / (t2 - t1))
