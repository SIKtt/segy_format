import numpy as np

import sy_dict
import sy_read
import sy_draw
import sy_output

f0URL = './dat/dat_test/timodel_vp.segy'
f1URL = '/marmousi/marmousi/shots.segy'
f2URL = '/2d_vibroseis/Line_001.sgy'
f3URL = '/elastic-marmousi-model/model/MODEL_DENSITY_1.25m.segy'

fstream = open(f3URL, 'rb')
head_keys = sy_dict.init_hdic()
r0 = fstream.read(3200)
r1 = fstream.read(400)
head_vals = sy_read.rdecode(r1, head_keys)
print("Traces")
print(head_vals['Traces'])
print("Samples")
print(head_vals['Samples'])
trace = head_vals['Traces']
sampr = head_vals['Samples']


z = sy_read.r_trace(fstream, trace, sampr)
sy_draw.trace_show_all_axes(z, 150)
# sy_draw.trace_show_single(z, 150)
sy_read.close_test(fstream)

# sy_output.save_as('z.txt',z)
# sy_output.save_head_as('head.txt',head_vals)
# sy_output.save_vol_as('vol.txt', sy_read.rdecode_vol(r0))

