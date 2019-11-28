# test sqlite operation
import sqlite3
import time
import numpy as np

no = 1000000

conn0 = sqlite3.connect("pinyin.db")
conn = sqlite3.connect("ts.db")

begin = time.time()
cursor0 = conn0.execute("SELECT unicode, chara from pinyin")
a0 = np.array(cursor0.fetchall())

cursor = conn.execute("SELECT sim_char from mt_s")
a = np.array(cursor.fetchall())

c = 0
c0 = 0
codes = []
for chars in a[:,0]:
      for char0 in a0[:,1]:
            c0 += 1
            if(char0 == chars):
                  print(a0[c0-1,0])
                  codes.append(a0[c0-1,0])
                  c += 1
      c0 = 0
print(len(codes))
for i in range(len(codes)):
      sql = "UPDATE mt_s set sim_unicode = '%s' where sim_char = '%s'" % (codes[i], a[i,0])
      conn.execute(sql)
      conn.commit()
#print(a[:,0])

end = time.time()

print(end - begin)
