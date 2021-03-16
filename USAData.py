### reading data in
"""
import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)
###this just gets rid of scientific notation in the pandas display and replaces it with a float to 3 decimals
pd.set_option('display.float_format', lambda x: '%.3f' % x)
#this just turns off an error I kept getting... hahaha
pd.options.mode.chained_assignment = None  # default='warn'
df.head()

### initialize dict to store data
USADict = {}
countyData = {}

### pulled state list to get all state names 
states = pd.read_csv('https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv')
states = states['State'].to_list()

for state in states: 
    stateData = df.loc[df['state'] == state]
    countyList = stateData.county.unique()
    groupedStateData = stateData.groupby(stateData.county)
    
    ### build a dictionary for county to data 
    for county in countyList:
        countyData[county] = groupedStateData.get_group(county)
    print(countyData)
    ### Key = state value = dictionary{county:data}
    USADict[state] = countyData
print(USADict)
"""
import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)

df["Location"] = df["county"] +", "+ df["state"]

datasetGroup = df.groupby(df.Location)

UtUt = datasetGroup.get_group('Utah, Utah')

print(UtUt)