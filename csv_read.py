import pandas
import os
sex_ratio = []


def read_sex():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[0]).values.tolist()
    male = 0
    female = 0
    for i in data:
        if(i[0] == 'F'):
            female += 1
        else:
            male += 1
    sex_ratio.append(male/(male+female))
    sex_ratio.append(female/(male+female))


nation_name = []
nation_ratio = []


def read_nationality():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[1]).values.tolist()
    nation = {}
    total = 0
    for i in data:
        total += 1
        if(nation.get(i[0]) == None):
            nation[i[0]] = 1
        else:
            nation[i[0]] = nation[i[0]]+1
    for key, value in nation.items():
        nation_name.append(key)
        nation_ratio.append(value/total)


place_name = []
place_ratio = []


def read_birthplace():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[2]).values.tolist()
    place = {}
    total = 0
    for i in data:
        total += 1
        if(place.get(i[0]) == None):
            place[i[0]] = 1
        else:
            place[i[0]] = place[i[0]]+1
    for key, value in place.items():
        place_name.append(key)
        place_ratio.append(value/total)


school_level_name = []
school_level_num = []


def read_school_level():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[3]).values.tolist()
    categories = {}
    for i in data:
        if(categories.get(i[0]) == None):
            categories[i[0]] = 1
        else:
            categories[i[0]] = categories[i[0]]+1
    for key in sorted(categories):
        school_level_name.append(key)
        temp = []
        temp.append(categories[key])
        school_level_num.append(temp)


academic_name = []
academic_num = []


def read_academic():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[4]).values.tolist()
    categories = {}
    for i in data:
        if(categories.get(i[0]) == None):
            categories[i[0]] = 1
        else:
            categories[i[0]] = categories[i[0]]+1
    for key in sorted(categories):
        academic_name.append(key)
        temp = []
        temp.append(categories[key])
        academic_num.append(temp)

subject_name = []
subject_num = []


def read_subject():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[6]).values.tolist()
    categories = {}
    for i in data:
        if(categories.get(i[0]) == None):
            categories[i[0]] = 1
        else:
            categories[i[0]] = categories[i[0]]+1
    for key in sorted(categories):
        subject_name.append(key)
        temp = []
        temp.append(categories[key])
        subject_num.append(temp)


semester_name = []
semester_num = []


def read_semester():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[7]).values.tolist()
    categories = {}
    for i in data:
        if(categories.get(i[0]) == None):
            categories[i[0]] = 1
        else:
            categories[i[0]] = categories[i[0]]+1
    for key in sorted(categories):
        semester_name.append(key)
        temp = []
        temp.append(categories[key])
        semester_num.append(temp)


relation_name = []
relation_ratio = []


def read_relation():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[8]).values.tolist()
    place = {}
    total = 0
    for i in data:
        total += 1
        if(place.get(i[0]) == None):
            place[i[0]] = 1
        else:
            place[i[0]] = place[i[0]]+1
    for key, value in place.items():
        relation_name.append(key)
        relation_ratio.append(value/total)


raise_hands_name = ["students"]
raise_hands_num = []


def read_raise_hands():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[9]).values.tolist()
    temp = []
    raise_hands_num.append(temp)
    for i in data:
        raise_hands_num[0].append(i[0])


visit_resource_name = ["students"]
visit_resource_num = []


def read_visit_resource():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[10]).values.tolist()
    temp = []
    visit_resource_num.append(temp)
    for i in data:
        visit_resource_num[0].append(i[0])


announcement_name = ["students"]
announcement_num = []


def read_announcement():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[11]).values.tolist()
    temp = []
    announcement_num.append(temp)
    for i in data:
        announcement_num[0].append(i[0])


discussion_name = ["students"]
discussion_num = []


def read_discussion():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[12]).values.tolist()
    temp = []
    discussion_num.append(temp)
    for i in data:
        discussion_num[0].append(i[0])

parent_answer_name = []
parent_answer_ratio = []


def read_parent_answer():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[13]).values.tolist()
    place = {}
    total = 0
    for i in data:
        total += 1
        if(place.get(i[0]) == None):
            place[i[0]] = 1
        else:
            place[i[0]] = place[i[0]]+1
    for key, value in place.items():
        parent_answer_name.append(key)
        parent_answer_ratio.append(value/total)


parent_satisfy_name = []
parent_satisfy_ratio = []


def read_parent_satisfy():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[14]).values.tolist()
    place = {}
    total = 0
    for i in data:
        total += 1
        if(place.get(i[0]) == None):
            place[i[0]] = 1
        else:
            place[i[0]] = place[i[0]]+1
    for key, value in place.items():
        parent_satisfy_name.append(key)
        parent_satisfy_ratio.append(value/total)

absent_name = []
absent_ratio = []


def read_absent():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[15]).values.tolist()
    place = {}
    total = 0
    for i in data:
        total += 1
        if(place.get(i[0]) == None):
            place[i[0]] = 1
        else:
            place[i[0]] = place[i[0]]+1
    for key, value in place.items():
        absent_name.append(key)
        absent_ratio.append(value/total)

class_name = []
class_num = []


def read_class():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[16]).values.tolist()
    categories = {}
    for i in data:
        if(categories.get(i[0]) == None):
            categories[i[0]] = 1
        else:
            categories[i[0]] = categories[i[0]]+1
    for key in sorted(categories):
        class_name.append(str(key))
        temp = []
        temp.append(categories[key])
        class_num.append(temp)
factors = []


def read_factors():
    data = pandas.read_csv("students_data_FIX.csv").columns
    len_data = len(data)
    for i in range(len_data):
        if(i >= 8 and i < len_data-1):
            factors.append(data[i])


def read_csv():
    read_factors()
    read_sex()
    read_nationality()
    read_birthplace()
    read_academic()
    read_school_level()
    read_subject()
    read_semester()
    read_relation()
    read_raise_hands()
    read_visit_resource()
    read_announcement()
    read_discussion()
    read_parent_answer()
    read_parent_satisfy()
    read_absent()
    read_class()
