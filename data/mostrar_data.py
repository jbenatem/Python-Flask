import matplotlib.pyplot as plt
import pandas as pd

def Guardar_Distribucion_Clases():
    #cargar excel
    df = pd.read_excel('data/dataset_training_test.xlsx')
    #mostrar distribucion de las clases en el dataset
    df['Apendicitis'].value_counts()
    df['Apendicitis'].value_counts().plot(kind='bar', title='Distribución de clases')
    plt.savefig('static/images/distribucion_clases.png')