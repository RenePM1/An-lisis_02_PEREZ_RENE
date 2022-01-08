# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

y = True #Condición para que el menú siga funcionando
#Menu Principal
print("\t\t\tSynergy Logistics\n")
while y == True:
  print("\n\t\t\t\tMenu\n\n1- Rutas de importación y exportación\n\n2- Medio de transporte utilizado\n\n3- Valor total de importaciones y exportaciones\n")
  opcion = int(input("Seleccione una opción:"))
  if opcion == 1: #Se puede escoger entre 3 opciones
    print("\n\n\n▓ Rutas de importación y exportación\n*10 Rutas más demandadas:\n\n")
    #10 rutas con mayor demanda (Flujos)
#Destino------------------------------
    synergy_dataframe = pd.read_csv('synergy_logistics_database.csv', encoding='utf-8', 
                                    parse_dates=[4, 5])

    combinaciones = synergy_dataframe.groupby(by=['origin','destination'])
    descripcion = combinaciones.count()['register_id']
    converter = descripcion.to_frame().reset_index()
    #print(converter)
    converter.sort_values(by='register_id' , ascending=False, inplace=True)
    print(converter.head(10))
    df=converter
    df[('% Acumulado')] = df[('register_id')].cumsum()/df[('register_id')].sum()*100
    #print('\n\n',df.head(10))
    g = sns.barplot(x='origin', y='register_id', data=converter.head(7))
    plt.show()
# Siguiente opcion en el menú  
  elif opcion == 2:
    print("\n\n\n▓ Medio de transporte utilizado\n\n")
# 3 Medios de transporte más importantes (Valor)-------------------
    synergy_dataframe = pd.read_csv('synergy_logistics_database.csv', index_col=0,
                                encoding='utf-8', 
                                parse_dates=[4, 5])

    leer = synergy_dataframe.groupby(by=['transport_mode'])
    Valor_total = leer.sum()['total_value']
    sort = Valor_total.sort_values(ascending=False)
    print(sort)
    sort = sort.to_frame().reset_index()
    g = sns.barplot(x='transport_mode', y='total_value', data=sort.head(), hue='transport_mode')
    plt.show()
#-------------------------------
  elif opcion == 3:
    synergy_dataframe = pd.read_csv('synergy_logistics_database.csv', index_col=0,
                                encoding='utf-8', 
                                parse_dates=[4, 5])

    combinaciones = synergy_dataframe.groupby(by=['origin'])
    descripcion = combinaciones.sum()['total_value']
    sort = descripcion.sort_values(ascending=False)
    sort = sort.to_frame().reset_index()
    df=sort
    df[('% Acumulado')] = df[('total_value')].cumsum()/df[('total_value')].sum()*100
    print('\n\n',df.head(9))
    g = sns.barplot(x='origin', y='total_value', data=sort.head(9), hue='origin')
    plt.show()

    data = synergy_dataframe.groupby(by=['origin','destination'])
    descripcion = data.sum()['total_value']
    sort = descripcion.sort_values(ascending=False)
    sort = sort.to_frame().reset_index()
    df=sort
    df[('% Acumulado')] = df[('total_value')].cumsum()/df[('total_value')].sum()*100
    print('\n\n',df.head(55))

#Selección incorrecta en el menú    
  else: 
    print("\n\n***Opción incorrecta, Intente nuevamente!!***")