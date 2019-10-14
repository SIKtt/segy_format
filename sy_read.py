import struct
import ebcdic

def rdecode_vol(r):
    return r.decode("cp1148")

def rdecode(r, dic):
	dataID = 0
	dataBegin = 0
	vdic = dic
	for key in list(dic):
		dataEnd = dic[key] - 3200 - 1
		if not dataEnd == 0:
			vdic[dataID] = int(r[dataBegin:dataEnd].hex(), 16)
		if dataEnd == dic['Unassigned2'] - 3200 - 1:
			dataID = 'Unassigned2'
			dataBegin = dataEnd
			vdic[dataID] = int(r[dataBegin:].hex(), 16)
		dataID = key
		dataBegin = dic[key] - 3200 - 1
	return vdic

def r_trace(fstream, trace, sampr):
	z = []
	for i in range(trace):
		k = []
		r3 = fstream.read(240)
		for j in range(sampr):
			rbuff = fstream.read(4)
			seg = struct.unpack('>f', rbuff) 
			k.append(seg[0])      
		z.append(k)
	return z

def r_shot(fstream, trace, sampr):
	r_m = fstream.tell()
	r = fstream.read()
	fstream.seek(r_m)
	single_dsize = trace * sampr * 4 + trace * 240
	shot_num = int(len(r)/single_dsize)
	return shot_num
	
def close_test(fstream):
    rf1=fstream.read()
    if not rf1 == 0:
        print("data left")
        fstream.close()
        print(len(rf1))
    else:
        fstream.close()
        print("over")