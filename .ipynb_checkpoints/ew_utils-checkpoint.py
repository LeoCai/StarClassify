
def intervalEWFeature(d, start=0, end=-1, filterThrehold=1):
    cp = d.copy()
    cp[abs(cp)<filterThrehold] = 0
    rd = cp.iloc[:,start:end]
    ew_absorb = rd[rd<0].sum(axis=1)
    ew_fs = rd[rd>0].sum(axis=1)
    return pd.concat([ew_absorb, ew_fs], axis=1)

def EWByRangeList(d, rangeList):
    ewfAll = pd.DataFrame()
    for r in rangeList:
        start, end = r
        ewf = intervalEWFeature(d, start, end)
        newNames = ['ew_' + str(start) + '_' + str(end) + '_' + str(v) for v in ewf.columns.values]
        ewf.columns = newNames
        ewfAll = pd.concat([ewfAll,ewf], axis=1)
    return ewfAll