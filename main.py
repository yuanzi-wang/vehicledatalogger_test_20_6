# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import folium

'''location example'''
# m = folium.Map(location=[45.5236, -122.6750])
# m.save("index.html")



#import data

# data = pd.read_csv (r'LOGGER05.csv',skiprows=1)
data = pd.read_csv (r'LOGGER06.csv',skiprows=1)
# data = pd.read_csv (r'C:\TUe\Graduation Project\preparation\vehicle data log\21_6_log\LOGGER05.csv',skiprows=1)
# print (data)
df = pd.DataFrame(data, columns= ['Lat','Lon'])
# print(df)

# select_rows = df.loc[(df['Lon'] != 526.6387)&(df['Lon'] != 0)]
"LOGGER05"
# select_rows = df.loc[(df['Lon'] != 529.2526)&(df['Lon'] != 0)]
"LOGGER06"


select_rows = df.loc[df['Lon'] != 0]
select_rows_d = select_rows.div(100)
print(select_rows_d)



# create a map
this_map = folium.Map(prefer_canvas=True)

def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    folium.CircleMarker(location=[point.Lat, point.Lon],
                        radius=2,
                        weight=0,
                        fill_color='#000000').add_to(this_map)

#use df.apply(,axis=1) to iterate through every row in your dataframe
# data.apply(plotDot, axis = 1)
select_rows_d.apply(plotDot, axis = 1)


#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())

#Save the map to an HTML file
# this_map.save('simple_dot_plot_05_1.html')
this_map.save('simple_dot_plot_06_1.html')
this_map
