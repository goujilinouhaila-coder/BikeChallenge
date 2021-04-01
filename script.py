import prediction
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


##importation of the data:
__file__ = 'script.py'
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv'
target_bike = os.path.join(os.path.dirname(os.path.realpath(__file__)), "prediction","data", "bike.csv")
 
bike= prediction.Load_data(url, target_bike).save_as_df(target_bike) 
##We will call the instructions below from the bike_format function:

#bike.columns=['Date','Heure','Grandtotal','Todaystotal', 'Unnamed','Remark']
#bike.drop(0,0,inplace=True)
#bike.drop(1,0,inplace=True)
#bike['Date'] = pd.to_datetime(bike['Date'])

#bike['Heure'].fillna(0, inplace = True) 

bike = prediction.bike_format(bike) 

##we peel the date

bike['Day_Week'] = bike['Date'].apply(lambda time: time.dayofweek)
bike['Year'] = bike['Date'].apply(lambda t: t.year)
bike.columns=['Date','Heure','Todaystotal','Day_Week','Year']


##New dataframe


bike['Heure'] = bike['Heure'].str.replace(':','-')

df1 = bike.Day_Week
df2 = bike.Heure
df3 = bike.Todaystotal
df4 = bike.Date
df5 = bike.Year

df = pd.DataFrame(list(zip(df1,df2,df3,df4,df5)), columns = ['Day_Week','Heure',"Todaystotal","Date","Year"])


T = df[(df.Heure > '00:01') & (df.Heure < '08:00')].tail(10)

#we will apply the median and the mean method for our prediction model
##We will make some  filters for the data between 23:59  and 08:00 : 

T0 = df[(df.Heure > '23:59') & (df.Heure < '00:01')].tail(10)

T1 = df[(df.Heure > '00:01') & (df.Heure < '01:00')].tail(10)

T2 = df[(df.Heure > '01:00') & (df.Heure < '02:00')].tail(10)

T3 = df[(df.Heure > '02:00') & (df.Heure < '03:00')].tail(10)

T4 = df[(df.Heure > '03:00') & (df.Heure < '04:00')].tail(10)

T5 = df[(df.Heure > '04:00') & (df.Heure < '05:00')].tail(10)

T6 = df[(df.Heure > '05:00') & (df.Heure < '06:00')].tail(10)

T7 = df[(df.Heure > '06:00') & (df.Heure < '07:00')].tail(10)

T8 = df[(df.Heure > '07:00') & (df.Heure < '08:00')].tail(10)

#T9= df[(df.Heure > '08:00') & (df.Heure < '09:00')].tail(10)


#The mean of T1
moyenneBike1 = T1['Todaystotal']
moyenne1 = np.mean(moyenneBike1)

#The median of T1
mediane1 = np.median(moyenneBike1)


#T2'mean
moyenneBike2 = T2['Todaystotal']
moyenne2 = np.mean(moyenneBike2)

# T2'median 
mediane2 = np.median(moyenneBike2)


# T4'mean 
moyenneBike4 = T4['Todaystotal']
moyenne4 = np.mean(moyenneBike4)

#The median of T4
mediane4 = np.median(moyenneBike4)

# The mean of T5
moyenneBike5 = T5['Todaystotal']
moyenne5 = np.mean(moyenneBike5)

#Median of P5
mediane5 = np.median(moyenneBike5)

#Moyenne de P6
moyenneBike6 = T6['Todaystotal']
moyenne6 = np.mean(moyenneBike6)

#Median of P6
mediane6 = np.median(moyenneBike6)

#Moyenne de P7

moyenneBike7 = T7['Todaystotal']
moyenne7 = np.mean(moyenneBike7)

#Median of  P7
mediane7 = np.median(moyenneBike7)

#Mean of P8
moyenneBike8 = T8['Todaystotal']
moyenne8 = np.mean(moyenneBike8)

#Median of P8
mediane8 = np.median(moyenneBike8) 

#The mean of T9 
#moyenneBike9 = T9['Todaystotal']
#moyenne9 = np.mean(moyenneBike9)

#The median of T9
#mediane9 = np.median(moyenneBike9) 

##We add all the mean and median values that we have calculated :

print(moyenne1+moyenne2+moyenne4+moyenne5+moyenne6+moyenne7+moyenne8)

print(mediane1+mediane2+mediane4+mediane5+mediane6+mediane7+mediane8)


#We will calculate the mean and the median for the data since 1st January 2021:
#For that we will manipulate another filter since the first January:
##It is more interesting to visualize the data since the start of the curfew at 6pm-6am.

filtre = df.query('Year > 2020 ')
T6New = filtre[(filtre.Heure > '05:00') & (filtre.Heure < '06:00')].tail(10)

T7New = filtre[(filtre.Heure > '06:00') & (filtre.Heure < '07:00')].tail(10)

T8New = filtre[(filtre.Heure > '07:00') & (filtre.Heure < '08:00')].tail(10)

##T9New = filtre[(filtre.Heure > '08:00') & (filtre.Heure < '09:00')].tail(10)



#Mean of  T6New
moyenneBike6New = T6New['Todaystotal']
moyenne6New = np.mean(moyenneBike6New)

#Median of T6New
mediane6New = np.median(moyenneBike6New)

#Mean of  T7New
moyenneBike7New = T7New['Todaystotal']
moyenne7New = np.mean(moyenneBike7New)

#Median of T7New
mediane7New = np.median(moyenneBike7New)

#Mean of  T8New
moyenneBike8New = T8New['Todaystotal']
moyenne8New = np.mean(moyenneBike8New)

#Median of T8New
mediane8New = np.median(moyenneBike8New)

#T9New 'mean 
#moyenneBike9New = T9New['Todaystotal']
#moyenne9New = np.mean(moyenneBike9New)

#Median of T9New:
#mediane9New = np.median(moyenneBike9New)

#We add the mean values tat we calcuated for our new  data:
 
print(moyenne6New + moyenne7New + moyenne8New)

##Same thing with median values:

print(mediane6New + mediane7New + mediane8New)