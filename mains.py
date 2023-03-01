from datetime import date
from tkinter.ttk import Style

import numpy as np
import math
import pandas as pd
import plotly.express as px
import streamlit as st
from IPython.display import display
from PIL import Image
# importing the modules
from tabulate import tabulate
import re

st.set_page_config(page_title='CONSOLIDATED DEPARTMENT WISE')
st.header('Consolidated Guided Research Scholar Count')
import os
import pandas as pd

#gets your current directory
dirname = os.path.dirname(__file__)

#concatenates your current directory with your desired subdirectory
bme_path = os.path.join(dirname, r'Dept.wise\BME\Research Scholars\ONGOING RESEARCH SCHOLARS DETAILS(3).xlsx')

#reads the excel file in a dataframe
main_dicz={}
mm=[]

df = pd.read_excel(bme_path, usecols="A:V", skiprows=3 )
print(df.columns.values.tolist())
mi = df['Full time/\n Part time']
ci = df['Name of Ph.D. guide']
print(mi)

ni_c= 0
for i in mi:
    if str(i).lower() =='full time':
        ni_c += 1
mm.append(ni_c)



ni_cs= 0
for i in mi:
    if str(i).lower() =='part time':
        ni_cs += 1
mm.append(ni_cs)

main_dicz['BME']=mm


chemistry_path = os.path.join(dirname,r'Dept.wise\Chemistry\ONGOING RESEARCH SCHOLARS DETAILS(7).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_chemistry = pd.read_excel(chemistry_path, usecols="A:V", skiprows=3)
print(df_chemistry.columns.values.tolist())
mi = df_chemistry['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time':
        ni_c += 1
mm.append(ni_c)


ni_cs= 0
for i in mi:
    if str(i).lower() =='part time':
        ni_cs += 1
mm.append(ni_cs)

main_dicz['Chemistry']=mm

civil_path = os.path.join(dirname,r'Dept.wise\Civil\Research Scholars\ONGOING RESEARCH SCHOLARS DETAILS(4).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_civil = pd.read_excel(civil_path, usecols="A:V", skiprows=3)
print(df_civil.columns.values.tolist())
mi = df_civil['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)


ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or str(i).lower() =='part':
        ni_cs += 1
mm.append(ni_cs)
main_dicz['Civil']=mm

cse_path = os.path.join(dirname,r'Dept.wise\CSE\ONGOING RESEARCH SCHOLARS DETAILS(2).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_cse = pd.read_excel(cse_path, usecols="A:V", skiprows=3)
print(df_cse.columns.values.tolist())
mi = df_cse['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time':
        ni_c += 1
mm.append(ni_c)


ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part' or str(i).lower() =='pt':
        ni_cs += 1
mm.append(ni_cs)

main_dicz['CSE']=mm

ece_path = os.path.join(dirname,r'Dept.wise\ECE\AS ON 21-07-2022 RESEARCH SCHOLARS DETAILS (1).xlsx')

    # reads the excel file in a dataframe
mm=[]
    # reads the excel file in a dataframe
df_ece = pd.read_excel(ece_path, usecols="A:V", skiprows=3)
print(df_ece.columns.values.tolist())
mi = df_ece['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)

ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part' or str(i).lower() =='pt':
        ni_cs += 1
mm.append(ni_cs)

main_dicz['ECE']=mm

eee_path = os.path.join(dirname,r'Dept.wise\EEE\Researh Scholars\ONGOING RESEARCH SCHOLARS DETAILS(8).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_eee = pd.read_excel(eee_path, usecols="A:V", skiprows=3)
print(df_eee.columns.values.tolist())
mi = df_eee['Full Time / Part Time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)



ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part' or str(i).lower() =='pt' :
        ni_cs += 1
mm.append(ni_cs)

main_dicz['EEE']=mm

eng_path = os.path.join(dirname,r'Dept.wise\English\ONGOING RESEARCH SCHOLARS DETAILS(11).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_eng = pd.read_excel(eng_path, usecols="A:V", skiprows=3)
print(df_eng.columns.values.tolist())
mi = df_eng['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)



ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part' or str(i).lower() =='pt' :
        ni_cs += 1
mm.append(ni_cs)

main_dicz['English']=mm

it_path = os.path.join(dirname,r'Dept.wise\IT\Research Scholars\ONGOING RESEARCH SCHOLARS DETAILS.xlsx')

mm=[]
    # reads the excel file in a dataframe
df_it = pd.read_excel(it_path, usecols="A:V", skiprows=3)
print(df_it.columns.values.tolist())
mi = df_it['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)


ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part'  or str(i).lower() =='pt' :
        ni_cs += 1
mm.append(ni_cs)

main_dicz['IT']=mm

math_path = os.path.join(dirname,r'Dept.wise\Maths\ONGOING RESEARCH SCHOLARS DETAILS(5).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_maths = pd.read_excel(math_path, usecols="A:V", skiprows=3)
print(df_maths.columns.values.tolist())
mi = df_maths['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time':
        ni_c += 1
mm.append(ni_c)



ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part' or str(i).lower() =='pt' :
        ni_cs += 1
mm.append(ni_cs)

main_dicz['Maths']=mm

mech_path = os.path.join(dirname,r'Dept.wise\MECH\Research Scholars\ONGOING RESEARCH SCHOLARS DETAILS(9).xlsx')

mm=[]
    # reads the excel file in a dataframe
df_mech = pd.read_excel(mech_path, usecols="A:V", skiprows=3)
print(df_mech.columns.values.tolist())
mi = df_mech['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)


ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part'  or str(i).lower() =='pt' :
        ni_cs += 1
mm.append(ni_cs)

main_dicz['Mech']=mm


phy_path = os.path.join(dirname,r'Dept.wise\Physics\ONGOING RESEARCH SCHOLARS DETAILS(6).xlsx')
mm=[]
    # reads the excel file in a dataframe
df_phy = pd.read_excel(phy_path, usecols="A:V", skiprows=3)
print(df_phy.columns.values.tolist())
mi = df_phy['Full time/\n Part time']

ni_c = 0
for i in mi:
    if str(i).lower() =='ft' or str(i).lower() =='full time' :
        ni_c += 1
mm.append(ni_c)



ni_cs= 0
for i in mi:
    if str(i).lower() =='part time' or i =='Part' or str(i).lower() =='pt' :
        ni_cs += 1
mm.append(ni_cs)

main_dicz['Physics']=mm

rc_path = os.path.join(dirname,r'Dept.wise\RC\Research Sch\RC PhD guided & guiding by the Supervisors - 16-6-202.xlsx')

mm=[]
    # reads the excel file in a dataframe
df_rc = pd.read_excel(phy_path, usecols="A:V", skiprows=3)
print(df_rc.columns.values.tolist())


ni_c = 0

mm.append(ni_c)


ni_cs= 0

mm.append(ni_cs)

main_dicz['RC']=mm

print(main_dicz)
full_time=[]
part_time=[]
dept=[]
for key,value in main_dicz.items():
    dept.append(key)
    full_time.append(value[0])
    part_time.append(value[1])


ft=pd.DataFrame(full_time)
pt=pd.DataFrame(part_time)
department=pd.DataFrame(dept)
dc = pd.concat([department,ft,pt], axis=1)
dc.columns=['DEPARTMENT','FULL TIME COUNT','PART TIME COUNT']
dc.columns=['DEPARTMENT','FULL TIME COUNT','PART TIME COUNT']
st.table(dc)



