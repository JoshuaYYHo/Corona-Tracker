#https://pypi.org/project/covid/
from covid import Covid

covid = Covid()
bruh = covid.get_data()

#Potential Problem: the data may not be the actual country's data and it could be another country's

country_list = []
for country in bruh:
    country_list.append(country['country'])

#print(country_list)

active_list = []
for active in bruh:
    active_list.append(active['active'])

#print(active_list)

confirmed_list = []
for confirm in bruh:
    confirmed_list.append(confirm['confirmed'])

#print(confirmed_list)

death_list = []
for death in bruh:
    death_list.append(death['deaths'])

#print(death_list)

recovered_list = []
for recover in bruh:
    recovered_list.append(recover['recovered'])

#print(recovered_list)

