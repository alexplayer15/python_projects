import pandas as pd
import numpy as np
import tkinter as tk 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, MetaData
import seaborn as sns

engine = create_engine('postgresql://postgres:password@winhost:5432/gladiator_data')
connection = engine.connect()
query = "SELECT * FROM gladiator_data LIMIT 10000;"
gladiator_data = pd.read_sql(query,connection)

metadata = MetaData()
metadata.reflect(bind=engine)

# Get the table(s) from the metadata
# for table_name, table in metadata.tables.items():
#     print(f"Table: {table_name}")
#     # Access columns for each table
#     for column in table.columns:
#         print(column.name)
def eda(db,column):
    
    print(f'The mean {column} is {np.mean(db[column])}')
    print(f'The std of {column} is {np.std(db[column])}')
    print(f'The median {column} is {np.median(db[column])}')
    print(f'The minimum {column} is {np.min(db[column])}')
    print(f'The maximum {column} is {np.max(db[column])}')

eda(gladiator_data,'age')

query_histogram = "SELECT * FROM gladiator_data LIMIT 100;"
gladiator_data_histogram = pd.read_sql(query_histogram,connection)

# def histogram(db,xaxis,yaxis,title):

#     column_names = [column.name.lower() for table_name, table in metadata.tables.items() for column in table.columns]

#     if xaxis in column_names:
#         if pd.api.types.is_numeric_dtype(db[xaxis]):
#             bin_calculator = (np.max(db[xaxis])-np.min(db[xaxis]))+1
#         else:
#             bin_calculator = db[xaxis].nunique()

#         plt.hist(db[xaxis],bins=bin_calculator,edgecolor='black')
#         plt.xlabel(xaxis)
#         plt.ylabel(yaxis)
#         plt.title(title)
#         plt.grid = True
#         plt.show()
#     else:
#         print(f'{xaxis} column not found in database. Please refer to the list above.')

# histogram(gladiator_data_histogram,'age','Number of Gladiators at Height','Distribution of Gladiator Height')

query_x_y_plot = "SELECT age, COUNT(*) AS count_survived FROM ( SELECT * FROM gladiator_data	WHERE survived = TRUE LIMIT 100000) AS subquery GROUP BY age ORDER BY age"
gladiator_data_x_y_plot = pd.read_sql(query_x_y_plot,connection)

def x_y_plot(db,xaxis,yaxis):

    if xaxis == "weapon_of_choice":
        db['weapon_of_choice'] = db['weapon_of_choice'].apply(lambda x: x.strip("()"))

    xaxis = db[xaxis]
    yaxis = db[yaxis]

    plt.plot(xaxis,yaxis)
    plt.xlabel('Weapon of Choice')
    plt.ylabel('number survived with weapon')
    plt.title('Number of Gladiators Who Survived Using Different Weapons')
    plt.legend()
    plt.show()

x_y_plot(gladiator_data_x_y_plot,'age','count_survived')

# query_pair_plot = "SELECT * FROM gladiator_data LIMIT 10000;"
# gladiator_data_pair_plot = pd.read_sql(query_pair_plot,connection)
# def pair_plot(db):
    
#     variables = ['age','battle_experience','survived']
#     numerical_data = db[variables]


#     # Create a pair plot using Seaborn
#     sns.pairplot(data= numerical_data, hue='survived')
#     plt.show()

# pair_plot(gladiator_data_pair_plot)

# query_heat_map = "SELECT * FROM gladiator_data LIMIT 1000;"
# gladiator_heat_map = pd.read_sql(query_heat_map,connection)

# def heat_map(db):

#     variables = ['age','battle_experience','survived']
#     numerical_data = db[variables]

#     # Compute the correlation matrix
#     corr_matrix = numerical_data.corr()

#     # Plot a heatmap
#     plt.figure(figsize=(10, 8))
#     sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
#     plt.title('Correlation Heatmap of Numerical Variables against Survival')
#     plt.show()

# heat_map(gladiator_heat_map)