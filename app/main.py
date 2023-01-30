import utils
import read_csv
import charts


def run():  
  data = read_csv.read_csv('data.csv')
  country = input('Digite el país ==> ')
  print(country)
  result = utils.get_population_by_country(data,country)
  
  if len(result)>0:
   country_ls = result[0]
   print(country_ls)
   labels,values = utils.population_by_years(country_ls)
   charts.generate_bar_chart(country,labels,values)

    #Filtrado de % poblacion en sur America
  data = list(filter(lambda item:item['Continent']=='South America',data))
  labels = [dict['Country/Territory'] for dict in data]
  values = [dict['World Population Percentage'] for dict in data]

  #labels = list(map(lambda item: item['Country/Territory'],data))
  #values = list(map(lambda item: item['World Population Percentage'],data))
  charts.generate_pie_chart(labels,values)
  
  
  
if __name__=='__main__':
  run()