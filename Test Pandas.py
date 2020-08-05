import numpy as np
import pandas as pd
#fron datetime import data

#def importdict(filename):#creates a function to read the csv
#    #create data frame from csv with pandas module
#    df=pd.read_csv(filename+'.csv', names=['systemtime', 'Var1', 'var2'],sep='$
#    fileDATES=df.T.to_dict().values()#export the data frame to a python dictio$
#    return fileDATES #return the dictionary to work with it outside the functi$
#if __name__ == '__main__':#
#       fileDATES = importdict('demo') #start the function with the name of the$
#       print (fileDATES[4])
#article_read = pd.read_csv('demo.csv', delimiter=';', names = ['Coin', 'Symbol$
#ar_filtered = article_read[article_read.Symbol == 'XRP']
#article_read[article_read.Symbol == 'XRP']
#print ar_filtered['Coin']
#summemax = int(0)

df = pd.read_csv('demo.csv', delimiter=';', names = ['Coin', 'Symbol', 'Qty', '$
ar_filtered = df[df.Coin == 'summemax']
summemax = pd.to_numeric(ar_filtered['Qty'])
print (summemax)

ar_filtered = df[df.Coin == 'Ampleforth']
#summemax =  pd.to_datetime(ar_filtered['Zeit'])
summemax = pd.to_numeric(ar_filtered['Qty'])
#.dt.strftime('%m/%d/%Y')
#pd.to_datetime(article_read)
#summemax = ar_filtered.Symbol
summemax = summemax * 2
print (summemax)

for i in range(len(df)) :
        if df.loc[i,"Coin"] == "summemax":
#       if df.loc[i,"Symbol"] != " ":
#                 print(df.loc[i, "Coin"], df.loc[i, "Qty"])
                  print(df.loc[i,"Qty"])


