import pandas as pd
import ipdb


# dataset = input("Path to your dataset: ")
dataset = "kc_house_data.csv"
original_data = pd.read_csv(f'data_sets/{dataset}')

print('Q01: How many houses are available for sold?')
print(f'ANS: {original_data.shape[0]}\n')

print('Q02. How many attributes do these houses have?')
print(f'ANS: {len(original_data.columns.to_list())}\n')

print('Q03. What are these attributes?')
print(f'ANS: {", ".join(original_data.columns.to_list())}\n')

print('Q04. Which house is more expensive?')
expensive_house = original_data[['id', 'price']].sort_values(by='price', ascending=False).iloc[0]
print(f"ANS: House's id: {expensive_house['id']}, Price US$: {expensive_house['price']}\n")

print('Q05. Which house has more bedrooms?')
more_bedrooms = original_data[['id', 'bedrooms']].max()
print(f"ANS: House's id: {more_bedrooms['id']}, Amount: {more_bedrooms['bedrooms']}\n")

print("Q06. What's the total number of bedrooms in all houses?")
print(f"ANS: {original_data[['bedrooms']].sum()['bedrooms']}\n")

print("Q07. How many houses have two bathrooms?")
print(f"ANS: {original_data[['bathrooms']].loc[original_data['bathrooms'] == 2].count()['bathrooms']}\n")

print("Q08. What's the average price of all houses?")
print(f"ANS: US$ {original_data[['price']].mean()['price']:.2f}\n")

print("Q09. What's the average price of houses with two bathrooms?")
print(f"ANS: US$ {original_data[['price', 'bathrooms']].loc[original_data['bathrooms'] == 2].mean()['price']:.2f}\n")

print("Q10. What's the minimum price between houses with three bedroom?")
print(f"ANS: US$ {original_data[['price', 'bathrooms']].loc[original_data['bathrooms'] == 3].min()['price']}\n")

print("Q11. How many houses have more than 300m^2 in the living room?")
original_data['m2_living'] = original_data['sqft_living'] * 0.092903
print(f"ANS: {len(original_data.query('m2_living > 300'))}\n")

print("Q12. How many houses have more than two floors?")
print(f"ANS: {original_data[['floors']][original_data['floors'] > 2].count()['floors']}\n")

print("Q13. How many houses have a waterfront?")
print(f"ANS: {original_data[['waterfront']][original_data['waterfront'] == 1].count()['waterfront']}\n")

print("Q14. Of the houses with waterfront, how many have three bedrooms?")
waterfront_3bedrooms = len(original_data.query('waterfront == 1').query('bedrooms == 3'))
print(f"ANS: {waterfront_3bedrooms}\n")

print("Q15. Of the houses with more than 300m^2 of living room, how many have two bathrooms?")
print(f"ANS: {len(original_data.query('m2_living > 300').query('bathrooms == 2'))}\n")

print("DONE\n")
