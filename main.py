import numpy as np

import sy_dict
import sy_read
import sy_draw

f0URL = "F:\\work\\dat\\test.sgy"
fstream = open(f0URL, 'rb')
head_keys = sy_dict.init_hdic()
r1 = fstream.read(3600)
head_vals = sy_read.rdecode(r1, head_keys)
print("Traces")
print(head_vals['Traces'])
print("Samples")
print(head_vals['Samples'])
trace = head_vals['Traces']
sampr = head_vals['Samples']

z = sy_read.r_trace(fstream, trace, sampr)
print(z)



