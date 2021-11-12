import pandas as pd
import csv

df=pd.read_csv('final.csv')

star_radiuses=df['radius'].to_list()
star_masses=df['mass'].to_list()
    
def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30     
convert_to_si(star_radiuses,star_masses)

star_gravity=[]
def gravity_calculation(radius,mass):
    G = 6.674e-11 
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2) 
        star_gravity.append(g) 
gravity_calculation(star_radiuses,star_masses)

df['radius']=star_radiuses
df['mass']=star_masses
df['gravity']=star_gravity

df.to_csv('real_final.csv')
