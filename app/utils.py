
def get_population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  return result

def population_by_years(country_d):
  
  country_dict = {
    
    '2022': int(country_d['2022 Population']),
    '2020': int(country_d['2020 Population']),
    '2015': int(country_d['2015 Population']),
    '2010': int(country_d['2010 Population']),
    '2000': int(country_d['2000 Population']),
    '1990': int(country_d['1990 Population']),
    '1980': int(country_d['1980 Population']),
    '1970': int(country_d['1970 Population'])
  }

  labels = country_dict.keys()
  values = country_dict.values()
  return labels,values

if __name__ == '__main__':
  
  country = {'Rank': '28', 'CCA3': 'COL', 'Country/Territory': 'Colombia', 'Capital': 'Bogota', 'Continent': 'South America', '2022 Population': '51874024', '2020 Population': '50930662', '2015 Population': '47119728', '2010 Population': '44816108', '2000 Population': '39215135', '1990 Population': '32601393', '1980 Population': '26176195', '1970 Population': '20905254', 'Area (km²)': '1141748', 'Density (per km²)': '45.4339', 'Growth Rate': '1.0069', 'World Population Percentage': '0.65'}


  lab,val = population_by_years(country)
  #print(lab, val)