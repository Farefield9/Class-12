a = pd.DataFrame({'eng':[52,48,69,70],'ip':[98,85,94,81],'geo':[85,88,78,91],'total':[235,221,241,242]}, index = ['k','n','p','t'])
b = a[a['total']>240]
print(b.loc[:,['eng','geo']])
a['AT']=90/100*a['total']
print(a)
print(a.loc[['k','t'],['eng','geo']])
print(a.loc[:,['eng','ip']].max())
print(a.loc['p':'t',:])
print(a.iloc[:,0:2])
print(a.loc[['k','p'],['ip','geo']])
a.iloc[1:2,0:1] = 55
print(a)
a.rename({'t':'tt'}, axis = 0, inplace =    True)
print(a)
a.rename(columns = {'eng':'e'},index = {'n':'nn'},  inplace = True)
print(a)
print(len(a))
