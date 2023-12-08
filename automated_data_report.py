import pandas as pd
import numpy as np
import tkinter as tk 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, MetaData
import os

engine = create_engine('postgresql://postgres:password@winhost:5432/gladiator_data')
connection = engine.connect()

metadata = MetaData()
metadata.reflect(bind=engine)

query_x_y_plot = "SELECT age, COUNT(*) AS count_survived FROM ( SELECT * FROM gladiator_data	WHERE survived = TRUE LIMIT 100000) AS subquery GROUP BY age ORDER BY age"
gladiator_data_x_y_plot = pd.read_sql(query_x_y_plot,connection)

def x_y_plot(db,xaxis,yaxis):

    if xaxis == "weapon_of_choice":
        db['weapon_of_choice'] = db['weapon_of_choice'].apply(lambda x: x.strip("()"))

    xaxis = db[xaxis]
    yaxis = db[yaxis]

    plt.plot(xaxis,yaxis)
    plt.xlabel('Age of Gladiators')
    plt.ylabel('Number of Gladiators Who Survived at Age')
    plt.title('Number of Gladiatos Who Survived at Different Ages')
    plt.legend()
    plt.savefig('x_y_plots/age_vs_survived')
    plt.close()

x_y_plot(gladiator_data_x_y_plot,'age','count_survived')

query = "SELECT * FROM gladiator_data LIMIT 10000;"
gladiator_data = pd.read_sql(query,connection)

def eda(db,column):
    
    mean = np.mean(db[column])
    standard_deviation = np.std(db[column])
    median = np.median(db[column])
    max = np.min(db[column])
    min = np.max(db[column])

    print(f'The mean {column} is {mean}')
    print(f'The std of {column} is {standard_deviation}')
    print(f'The median {column} is {median}')
    print(f'The minimum {column} is {max}')
    print(f'The maximum {column} is {min}')

    return mean, standard_deviation, median, max, min

eda(gladiator_data,'age')

def generate_report(db,column):

    mean, standard_deviation, median, min, max = eda(db,column)
    
    report_content = f"""
    Automated Report
    ----------------

    Key Numeric Information for '{column}':
    - Mean: {mean}
    - Standard Deviation: {standard_deviation}
    - Median: {median}
    - Minimum: {min}
    - Maximum: {max}
    """
    return report_content

# Write the report to a text file
folder_path = '/home/alex_player/Python/reports/'
file_name = 'automated_report.txt'
file_path = os.path.join(folder_path,file_name)

with open(file_path, 'w') as file:
    file.write(generate_report(gladiator_data,'age'))