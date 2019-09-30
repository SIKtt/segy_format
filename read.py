import binascii
import struct
import ebcdic
import os
from matplotlib import pyplot as plt

f0URL = "E:\marmousi\stack.segy"
f1URL = "E:\marmousi\Density.segy"
f2URL = "E:\\marmousi\\viking_small.segy"

def r2decode(r2, head):
    dataID = 0
    dataBegin = 0
    for key in head_keys:
        dataEnd = head_keys[key] - 3200 - 1
        if not dataEnd == 0:
            # print(dataID)
            # print(int(r2[dataBegin:dataEnd].hex(), 16))
            head[dataID] = int(r2[dataBegin:dataEnd].hex(), 16)
            # hex(r1[dataBegin:dataEnd])
        if dataEnd == head_keys['Unassigned2'] - 1:
            dataID = 'Unassigned2'
            dataBegin = dataEnd
            print(dataID)
            print(r2[dataBegin:].hex())
        dataID = key
        dataBegin = head_keys[key] - 3200 - 1
 
def r3decode(r3):
    dataID = 0
    dataBegin = 0
    for key in trace_keys:
        dataEnd = trace_keys[key] - 1
        if not dataEnd == 0:
            print(dataID)
            print(int(r3[dataBegin:dataEnd].hex(), 16))
        if dataEnd == trace_keys['UnassignedInt2'] - 1:
            dataID = 'Unassigned2'
            dataBegin = dataEnd
            print(dataID)
            print(int(r3[dataBegin:].hex()))
        dataID = key
        dataBegin = trace_keys[key] - 1

def hex2dec(r):
    for i in range(int(len(r)/2)):
        print(r[2*i:2*(i+1)].hex())
    return k
head_keys = {
    'JobID'                 : 3201,
    'LineNumber'            : 3205,
    'ReelNumber'            : 3209,
    'Traces'                : 3213,
    'AuxTraces'             : 3215,
    'Interval'              : 3217,
    'IntervalOriginal'      : 3219,
    'Samples'               : 3221,
    'SamplesOriginal'       : 3223,
    'Format'                : 3225,
    'EnsembleFold'          : 3227,
    'SortingCode'           : 3229,
    'VerticalSum'           : 3231,
    'SweepFrequencyStart'   : 3233,
    'SweepFrequencyEnd'     : 3235,
    'SweepLength'           : 3237,
    'Sweep'                 : 3239,
    'SweepChannel'          : 3241,
    'SweepTaperStart'       : 3243,
    'SweepTaperEnd'         : 3245,
    'Taper'                 : 3247,
    'CorrelatedTraces'      : 3249,
    'BinaryGainRecovery'    : 3251,
    'AmplitudeRecovery'     : 3253,
    'MeasurementSystem'     : 3255,
    'ImpulseSignalPolarity' : 3257,
    'VibratoryPolarity'     : 3259,
    'Unassigned1'           : 3261,
    'SEGYRevision'          : 3501,
    'TraceFlag'             : 3503,
    'ExtendedHeaders'       : 3505,
    'Unassigned2'           : 3507,
}

trace_keys = {
    'TRACE_SEQUENCE_LINE'                   : 1,
    'TRACE_SEQUENCE_FILE'                   : 5,
    'FieldRecord'                           : 9,
    'TraceNumber'                           : 13,
    'EnergySourcePoint'                     : 17,
    'CDP'                                   : 21,
    'CDP_TRACE'                             : 25,
    'TraceIdentificationCode'               : 29,
    'NSummedTraces'                         : 31,
    'NStackedTraces'                        : 33,
    'DataUse'                               : 35,
    'offset'                                : 37,
    'ReceiverGroupElevation'                : 41,
    'SourceSurfaceElevation'                : 45,
    'SourceDepth'                           : 49,
    'ReceiverDatumElevation'                : 53,
    'SourceDatumElevation'                  : 57,
    'SourceWaterDepth'                      : 61,
    'GroupWaterDepth'                       : 65,
    'ElevationScalar'                       : 69,
    'SourceGroupScalar'                     : 71,
    'SourceX'                               : 73,
    'SourceY'                               : 77,
    'GroupX'                                : 81,
    'GroupY'                                : 85,
    'CoordinateUnits'                       : 89,
    'WeatheringVelocity'                    : 91,
    'SubWeatheringVelocity'                 : 93,
    'SourceUpholeTime'                      : 95,
    'GroupUpholeTime'                       : 97,
    'SourceStaticCorrection'                : 99,
    'GroupStaticCorrection'                 : 101,
    'TotalStaticApplied'                    : 103,
    'LagTimeA'                              : 105,
    'LagTimeB'                              : 107,
    'DelayRecordingTime'                    : 109,
    'MuteTimeStart'                         : 111,
    'MuteTimeEND'                           : 113,
    'TRACE_SAMPLE_COUNT'                    : 115,
    'TRACE_SAMPLE_INTERVAL'                 : 117,
    'GainType'                              : 119,
    'InstrumentGainConstant'                : 121,
    'InstrumentInitialGain'                 : 123,
    'Correlated'                            : 125,
    'SweepFrequencyStart'                   : 127,
    'SweepFrequencyEnd'                     : 129,
    'SweepLength'                           : 131,
    'SweepType'                             : 133,
    'SweepTraceTaperLengthStart'            : 135,
    'SweepTraceTaperLengthEnd'              : 137,
    'TaperType'                             : 139,
    'AliasFilterFrequency'                  : 141,
    'AliasFilterSlope'                      : 143,
    'NotchFilterFrequency'                  : 145,
    'NotchFilterSlope'                      : 147,
    'LowCutFrequency'                       : 149,
    'HighCutFrequency'                      : 151,
    'LowCutSlope'                           : 153,
    'HighCutSlope'                          : 155,
    'YearDataRecorded'                      : 157,
    'DayOfYear'                             : 159,
    'HourOfDay'                             : 161,
    'MinuteOfHour'                          : 163,
    'SecondOfMinute'                        : 165,
    'TimeBaseCode'                          : 167,
    'TraceWeightingFactor'                  : 169,
    'GeophoneGroupNumberRoll1'              : 171,
    'GeophoneGroupNumberFirstTraceOrigField': 173,
    'GeophoneGroupNumberLastTraceOrigField' : 175,
    'GapSize'                               : 177,
    'OverTravel'                            : 179,
    'CDP_X'                                 : 181,
    'CDP_Y'                                 : 185,
    'INLINE_3D'                             : 189,
    'CROSSLINE_3D'                          : 193,
    'ShotPoint'                             : 197,
    'ShotPointScalar'                       : 201,
    'TraceValueMeasurementUnit'             : 203,
    'TransductionConstantMantissa'          : 205,
    'TransductionConstantPower'             : 209,
    'TransductionUnit'                      : 211,
    'TraceIdentifier'                       : 213,
    'ScalarTraceHeader'                     : 215,
    'SourceType'                            : 217,
    'SourceEnergyDirectionMantissa'         : 219,
    'SourceEnergyDirectionExponent'         : 223,
    'SourceMeasurementMantissa'             : 225,
    'SourceMeasurementExponent'             : 229,
    'SourceMeasurementUnit'                 : 231,
    'UnassignedInt1'                        : 233,
    'UnassignedInt2'                        : 237,
}
fstream = open(f2URL, 'rb')
# r0 = fstream.readlines()

# print(fstream.tell())
# fstream.seek(0)

# 40 record x 80 bytes ASCII
r1 = fstream.read(3200)
# 400 bytes bin
r2 = fstream.read(400)
r3 = fstream.read(240)
r4 = fstream.read(240)



# print(r1.decode("cp1148"))
# print(r1)
# print(type(r1))
# print(hex(fstream.readline(1)))
# print(float(r0[1]))
# print(struct.unpack("f", r0[1]))
# print(len(r2))
# print(r3)

head_val = head_keys
r2decode(r2, head_val)

print(head_val['Traces'])
print(head_val['Samples'])
trace = head_val['Traces']
sampr = head_val['Samples']

all = trace * sampr
# print(single)
r5 = fstream.read(sampr)
k = []
k = hex2dec(r5)


trace_val = trace_keys
# for i in range(trace):
    # subbegin = i * sampr
    # subend = (i + 1) * sampr
    # plot(r5[subbegin, subend])
# plt.figure()
# plt.plot(r5)
# plt.show()
# print(r4)

