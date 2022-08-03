import pandas
import os
sex_ratio=[]
def read_sex():
    os.chdir(os.getcwd())
    data=pandas.read_csv('students_data_FIX.csv',usecols=[0]).values.tolist()
    male=0
    female=0
    for i in data:
        if(i[0]=='F'):
            female+=1
        else:
            male+=1
    sex_ratio.append(male/(male+female))
    sex_ratio.append(female/(male+female))

nation_name=[]
nation_ratio=[]
def read_nationality():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',usecols=[1]).values.tolist()
    nation={}
    total=0
    for i in data:
        total+=1
        if(nation.get(i[0])==None):
            nation[i[0]]=1
        else:
            nation[i[0]]=nation[i[0]]+1
    for key,value in nation.items():
        nation_name.append(key)
        nation_ratio.append(value/total)

place_name=[]
place_ratio=[]
def read_birthplace():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',usecols=[2]).values.tolist()
    place={}
    total=0
    for i in data:
        total+=1
        if(place.get(i[0])==None):
            place[i[0]]=1
        else:
            place[i[0]]=place[i[0]]+1
    for key,value in place.items():
        place_name.append(key)
        place_ratio.append(value/total)

academic_name=[]
academic_num=[]
def read_academic():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',usecols=[4]).values.tolist()
    categories={}
    for i in data:
        if(categories.get(i[0])==None):
            categories[i[0]]=1
        else:
            categories[i[0]]=categories[i[0]]+1
    for key in sorted(categories):
        academic_name.append(key)
        temp =[]
        temp.append(categories[key])
        academic_num.append(temp)

def read_csv():
    read_sex()
    read_nationality()
    read_birthplace()
    read_academic()