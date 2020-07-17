import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
output_file = open('/Users/Eoin/OneDrive/Cambridge/IB/General/UROP/CrunchTope-InstallMac/Projects/EoinInput/output.out', 'r')
headerLine = output_file.readline()
columnHeaders = headerLine[11:]
columnHeaders = columnHeaders.replace("'", "")
columnHeaders = columnHeaders.replace('"', "")
columnHeaders = columnHeaders.replace('(yrs)', "")
columnHeaders = columnHeaders.replace(' ', "")
columnHeaders = columnHeaders.rstrip()
columnHeaders = columnHeaders.rstrip(',')
columnHeaders = columnHeaders.split(',')  
df = pd.read_csv(output_file, engine='python', sep='\s+', skiprows=[0,1], names=columnHeaders)
print(df)
print(columnHeaders)
#data = pd.read_csv('/Users/Eoin/OneDrive/Cambridge/IB/General/UROP/CrunchTope-InstallMac/Projects/EoinInput/output.out', sep='\t')
for i in df:
    x=[]
    y=[]
    x.append(df[0])
    y.append(df[i])
print(x, y)
    #plt.plot(x,y)
plt.xlabel('Time (years)')
    #plt.show()


#output_file.close()