import struct
def rdecode(r, dic):
	dataID = 0
	dataBegin = 0
	vdic = dic
	for key in list(dic):
		dataEnd = dic[key] - 1
		if not dataEnd == 0:
			vdic[dataID] = int(r[dataBegin:dataEnd].hex(), 16)
		if dataEnd == dic['Unassigned2'] - 1:
			dataID = 'Unassigned2'
			dataBegin = dataEnd
			vdic[dataID] = int(r[dataBegin:].hex(), 16)
		dataID = key
		dataBegin = dic[key] - 1
	return vdic

def r_trace(fstream, trace, sampr):
	z = []
	for i in range(trace):
		k = []
		r3 = fstream.read(240)
		for j in range(sampr):
			rbuff = fstream.read(4)
			k = struct.unpack('>f', rbuff)
		z.append(k)
	return z
	
