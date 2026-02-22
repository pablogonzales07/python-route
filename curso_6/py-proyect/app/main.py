import read_csv
import utils

import charts
import pandas as pd

def run():
    '''
    data = read_csv.read_csv("./data.csv")
    data = list(filter(lambda item: item["Continent"] == "South America", data))

    result = utils.get_porcentage(data)

    labels, values = result
    charts.generate_pie_chart(labels, values)
    '''
    df = pd.read_csv('./data.csv')
    df = df[df['Continent'] == "Africa"]

    countries = df['Country/Territory'].values
    percentages= df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)
    data = read_csv.read_csv("./data.csv")

    country = input("Type country ==> ").title()

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == "__main__":
    run()
