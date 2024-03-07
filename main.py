import os
import glob
import pandas as pd

#reading the csv files for last 10 years
csv_files = glob.glob('*.{}'.format('csv'))
#For every csv file
for file in csv_files:
    df = pd.read_csv(file)

    #First iteration NEW.csv is a copy
    if file == csv_files[0]:
        newdf = df.to_csv('NEW.csv')
    elif file == 'NEW.csv':
        pass
    else:
        newdf = pd.read_csv('NEW.csv')
        #This is what will be writting to NEW.csv
        lineLen = len(df)
        header = ['TEAM','pDIFF', 'GP', 'L', 'W']
        data = []
        for i in range(lineLen):
            dataRow = []
            for j in header:
                if j == 'TEAM':
                    newValue = getattr(df, j)[i]
                #if it's the last iteration, it should find the average, not just the sum. 
                elif file == csv_files[len(csv_files)-1]:
                    value = getattr(df, j)[i]
                    newValue = getattr(newdf, j)[i]
                    newValue = (value + newValue) / len(csv_files)
                else:
                    value = getattr(df, j)[i]
                    newValue = getattr(newdf, j)[i]
                    newValue = value + newValue
                
                
                
                dataRow.append(newValue)
                # print('this is dataRow', dataRow)
            
            data.append(dataRow)
        print('This is data', data)
        data = pd.DataFrame(data, columns=header)
        data.to_csv('NEW.csv', index=False)
    

