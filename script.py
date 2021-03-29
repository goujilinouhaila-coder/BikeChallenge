import Prediction
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


##importation of the data:
__file__ = 'script.py'
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv'
target_bike = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Prediction","data", "bike.csv")
 
bike= Prediction.Load_data(url, target_bike).save_as_df(target_bike) 
##We will call the instructions below from the bike_format function:

#bike.columns=['Date','Heure','Grandtotal','Todaystotal', 'Unnamed','Remark']
#bike.drop(0,0,inplace=True)
#bike.drop(1,0,inplace=True)
#bike['Date'] = pd.to_datetime(bike['Date'])

#bike['Heure'].fillna(0, inplace = True) 

bike = Prediction.bike_format(bike) 

##we peel the date

bike['Day of Week'] = bike['Date'].apply(lambda time: time.dayofweek)
bike['Year'] = bike['Date'].apply(lambda t: t.year)
bike.columns=['Date','Heure','Todaystotal','DayOfWeek','Year']


##New dataframe


bike['Heure'] = bike['Heure'].str.replace(':','-')

list1 = bike.DayOfWeek
list2 = bike.Heure
list3 = bike.Todaystotal
list4 = bike.Date
list5 = bike.Year

df = pd.DataFrame(list(zip(list1,list2,list3,list4,list5)), columns = ['DayOfWeek','Heure',"Todaystotal","Date","Year"])


T = df[(df.Heure > '00:01') & (df.Heure < '08:00')].tail(10)

print(T)

#we will apply the median and the mean method for our prediction model

T0 = df[(df.Heure > '23:59') & (df.Heure < '00:01')].tail(10)
print(T0)

T1 = df[(df.Heure > '00:01') & (df.Heure < '01:00')].tail(10)
print(T1)

T2 = df[(df.Heure > '01:00') & (df.Heure < '02:00')].tail(10)
print(T2)

T3 = df[(df.Heure > '02:00') & (df.Heure < '03:00')].tail(10)
print(T3)

T4 = df[(df.Heure > '03:00') & (df.Heure < '04:00')].tail(10)
print(T4)

T5 = df[(df.Heure > '04:00') & (df.Heure < '05:00')].tail(10)
print(T5)

T6 = df[(df.Heure > '05:00') & (df.Heure < '06:00')].tail(10)
print(T6)

T7 = df[(df.Heure > '06:00') & (df.Heure < '07:00')].tail(10)
print(T7)

T8 = df[(df.Heure > '07:00') & (df.Heure < '08:00')].tail(10)
print(T8)

#The mean of T1
moyenneBike1 = T1['Todaystotal']
moyenne1 = np.mean(moyenneBike1)

print (round(moyenne1, 2))


#The median of T1
mediane1 = np.median(moyenneBike1)
print (round(mediane1, 2))

#T2'mean
moyenneBike2 = T2['Todaystotal']
moyenne2 = np.mean(moyenneBike2)

print ( round(moyenne2, 2))


# T2'median 
mediane2 = np.median(moyenneBike2)
print ( round(mediane2, 2))

# T4'mean 
moyenneBike4 = T4['Todaystotal']
moyenne4 = np.mean(moyenneBike4)

print ( round(moyenne4, 2))


#The median of T4
mediane4 = np.median(moyenneBike4)
print ( round(mediane4, 2))

# The mean of T5
moyenneBike5 = T5['Todaystotal']
moyenne5 = np.mean(moyenneBike5)

print ( round(moyenne5, 2))


#Médiane de P5
mediane5 = np.median(moyenneBike5)
print (round(mediane5, 2))

#Moyenne de P6
moyenneBike6 = T6['Todaystotal']
moyenne6 = np.mean(moyenneBike6)

print (round(moyenne6, 2))


#Médiane de P6
mediane6 = np.median(moyenneBike6)
print (round(mediane6, 2))

#Moyenne de P7

moyenneBike7 = T7['Todaystotal']
moyenne7 = np.mean(moyenneBike7)

print ( round(moyenne7, 2))


#Médiane de P7
mediane7 = np.median(moyenneBike7)
print (round(mediane7, 2))

#Moyenne de P8
moyenneBike8 = T8['Todaystotal']
moyenne8 = np.mean(moyenneBike8)

print ( round(moyenne8, 2))


#Médiane de P8
mediane8 = np.median(moyenneBike8)
print ( round(mediane8, 2))

##We add all the mean and median values that we have calculated :

print(moyenne1+moyenne2+moyenne4+moyenne5+moyenne6+moyenne7+moyenne8)

print(mediane1+mediane2+mediane4+mediane5+mediane6+mediane7+mediane8)



#Since The first of January 2021: 

filtre = df.query('Year > 2020 ')
T6New = filtre[(filtre.Heure > '05:00') & (filtre.Heure < '06:00')].tail(10)
print(T6)


filtre = df.query('Year > 2020 ')
T7New = filtre[(filtre.Heure > '06:00') & (filtre.Heure < '07:00')].tail(10)
print(T7New)


filtre = df.query('Year > 2020 ')
T8New = filtre[(filtre.Heure > '07:00') & (filtre.Heure < '08:00')].tail(10)
print(T8New)



#Mean of  P6New
moyenneBike6New = T6New['Todaystotal']
moyenne6New = np.mean(moyenneBike6New)

print (round(moyenne6New, 2))


#Median of P6New
mediane6New = np.median(moyenneBike6New)
print (round(mediane6New, 2))



#Mean of  P7New
moyenneBike7New = T7New['Todaystotal']
moyenne7New = np.mean(moyenneBike7New)

print ( round(moyenne7New, 2))


#Median of P7New
mediane7New = np.median(moyenneBike7New)
print ( round(mediane7New, 2))


#Mean of  P8New
moyenneBike8New = T8New['Todaystotal']
moyenne8New = np.mean(moyenneBike8New)

print (round(moyenne8New, 2))

#Median of P8New
mediane8New = np.median(moyenneBike8New)
print ( round(mediane8New, 2))


#We add the mean values tat we calcuated for our new  data:
 
print(moyenne6New + moyenne7New + moyenne8New)

##Same thing with median values:

print(mediane6New + mediane7New + mediane8New)