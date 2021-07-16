#Generates ISO codes for each country
import pycountry
#Map the data for visualization
import plotly.express as px
#Store and organize data
import pandas as pd

#Step 1
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)

list_countries = df1['Country'].unique().tolist()
d_country_code = {}

#Step 2
for country in list_countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)
        country_code = country_data[0].alpha_3
        d_country_code.update({country: country_code})
    except:
        print('could not add ISO 3 code for ->', country)
        #If a country could not be added, add a space in place of the ISO code
        d_country_code.update({country: ' '})

#Create a new column, iso_alpha, in the dataframe
#Fill the column with appropriate iso 3 codes
for k, v in d_country_code.items():
    df1.loc[(df1.Country == k), 'iso_alpha'] = v

#Step 3
fig = px.choropleth(data_frame = df1, locations = "iso_alpha", color = "Confirmed", hover_name = "Country", color_continuous_scale = 'RdYlGn_r', animation_frame = "Date")

fig.show()