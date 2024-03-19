import os
import glob
import pandas as pd

#Analysis after reading and writing to new csv
def analyze (file):
    df = pd.read_csv(file)

    #Find winner for point diff, win percentage, and Total wins
        #Iterate through the column, find the biggest, that team is the winner
    #Then check winners for each, count how may each winner showed up
        #Create an array of the winners, Go through each and count number of wins
    #Team with most occurances of wins is overall winner
    #write the winners onto new CSV
    winner = ""
    print('---THIS IS WINNER CSV---')
    
    pDIFFwin = ''
    GPwin = ''
    winPerc = ''
    pDIFFscr = 0
    GPscr = 0
    winscr = 0
    for i in range(len(df)):
        #This is each row
        for j in header:
            value = getattr(df, j)[i]
            if j == 'TEAM':
                pass
            
            elif j == 'pDIFF':
                if value > pDIFFscr:
                    pDIFFscr = value
                    pDIFFwin = getattr(df, 'TEAM')[i]
                elif value == pDIFFscr:
                    pDIFFwin = pDIFFwin + ", " + getattr(df, 'TEAM')[i]
            
            elif j == 'GP':
                if value > GPscr:
                    GPscr = value
                    GPwin = getattr(df, 'TEAM')[i]
                elif value == GPscr:
                    GPwin = GPwin + ", " + getattr(df, 'TEAM')[i]
            
            elif j == 'W':
                if value > winscr:
                    winscr = value
                    winPerc = getattr(df, 'TEAM')[i]
                elif value == winscr:
                    winPerc = winPerc + ", " + getattr(df, 'TEAM')[i]
    
                
                    
            
            
        

        

#reading the csv files in the same folder
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

analyze('NEW.csv')
    

