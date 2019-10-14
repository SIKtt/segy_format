import numpy as np

import sy_dict
import sy_read
import sy_draw
import sy_output

f0URL = './dat/dat_test/timodel_vp.segy'
f1URL = '/marmousi/marmousi/shots.segy'
f2URL = '/2d_vibroseis/Line_001.sgy'
f3URL = '/elastic-marmousi-model/model/MODEL_DENSITY_1.25m.segy'
salt_URL0 = '/small_salt_MDG/model.segy'
salt_URL1 = '/small_salt_MDG/shots.segy'
marmousi_URL0 = '/marmousi_MDG/model.segy'
marmousi_URL1 = '/marmousi_MDG/shots.segy'
marmousi_URL2 = '/marmousi_MDG/stack.segy'
fstream = open(marmousi_URL1, 'rb')
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

shot = sy_read.r_shot(fstream, trace, sampr)
print("Shots")
print(shot)
for i in range(shot):
	z = sy_read.r_trace(fstream, trace, sampr)
	savURL = '/marmousi_MDG/shot/shot_'+ str(i) +'.txt'
	sav1URL = '/marmousi_MDG/shot_pic/shot_'+ str(i)
	sy_draw.trace_show_all_axes(z, 300, sav1URL)
	sy_output.save_as(savURL,z)
	print(i)

# sy_draw.trace_show_all_surf(z)
# sy_draw.trace_show_all_axes(z, 300, 0)
sy_read.close_test(fstream)

# sy_output.save_as('/marmousi_MDG/shots.txt',z)
# sy_output.save_head_as('/marmousi_MDG/head.txt',head_vals)
# sy_output.save_vol_as('/marmousi_MDG/vol.txt', sy_read.rdecode_vol(r0))

