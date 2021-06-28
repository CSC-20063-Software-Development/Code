import pandas as pd

data = pd.read_csv(r'/Users/harryhudson/Documents/Year2/Semester2/Software Development/weather.csv')


#DROPPING UNWANTEC COLUMNS
data.drop(['Date.Month','Date.Week of', 'Date.Year', 'Station.City', 'Station.Code', 'Station.Location', 'Station.State', 'Data.Wind.Direction', 'Data.Temperature.Max Temp', 'Data.Temperature.Min Temp', 'Data.Wind.Direction', 'Data.Wind.Speed'], axis=1,  inplace=True)


#CONVERTING DATE COLUMN TO DATETIME
data['Date.Full'] = pd.to_datetime(data['Date.Full'])


#---------------------------------------------------- USER INTERFACE OPTIONS BELOW ------------------------------------------------------

#FILTER BY MONTH OPTION
data = data[data['Date.Full'].dt.month == 1]
#print(data.head)


#---------------------------------------------------- CREATING 2 NEW DATASETS FOR ABOVE AND BELOW 5 PRECPITATION ------------------------


#PRECIPITATION ABOVE 5
precip = data['Data.Precipitation'] >= 5
Precipitation_above_5 = data[precip]
#print(Precipitation_above_5)



#PRECIPITATION BELOW 5
precip2 = data['Data.Precipitation'] < 5
Precipitation_below_5 = data[precip2]
#print(Precipitation_below_5)


#---------------------------------------------------- CODE TO SUBSET THE NEW DATASETS EVEN FURTHER BY TEMPERATURE -----------------------


#AVERAGE TEMPERATURE ABOVE 60 FOR PRECIP ABOVE 5
Temp = Precipitation_above_5['Data.Temperature.Avg Temp'] >=60
Temp_above_60 = Precipitation_above_5[Temp]
#print("DATES ABOVE 5 PRECIPTATION AND ABOVE 60 DEGREES",Temp_above_60['Date.Full'])



#AVERAGE TEMPERATURE BELOW 60 FOR PRECIP ABOVE 5
Temp2 = Precipitation_above_5['Data.Temperature.Avg Temp'] < 60
Temp_below_60 = Precipitation_above_5[Temp2]
#print("DATES ABOVE 5 PRECIPTATION AND BELOW 60 DEGREES",Temp_below_60['Date.Full'])



#AVERAGE TEMPERATURE BELOW 60 FOR PRECIP BELOW 5
Temp3 = Precipitation_below_5['Data.Temperature.Avg Temp'] >=60
Temp_above_60_2 = Precipitation_below_5[Temp3]
#print("DATES BELOW 5 PRECIPTATION AND ABOVE 60 DEGREES",Temp_above_60_2['Date.Full'])



#AVERAGE TEMPERATURE ABOVE 60 FOR PRECIP BELOW 5
Temp4 = Precipitation_below_5['Data.Temperature.Avg Temp'] < 60
Temp_below_60_2 = Precipitation_below_5[Temp4]
#print("DATES BELOW 5 PRECIPTATION AND BELOW 60 DEGREES",Temp_below_60_2['Date.Full'])


