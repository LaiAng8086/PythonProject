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
    for i in data:
        global raise_hands_num
        raise_hands_num.append(i[0])

    raise_hands_num = sorted(raise_hands_num)


visit_resource_name = ["students"]
visit_resource_num = []


def read_visit_resource():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[10]).values.tolist()
    for i in data:
        global visit_resource_num
        visit_resource_num.append(i[0])
    visit_resource_num = sorted(visit_resource_num)


announcement_name = ["students"]
announcement_num = []


def read_announcement():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[11]).values.tolist()
    for i in data:
        global announcement_num
        announcement_num.append(i[0])
    announcement_num = sorted(announcement_num)


discussion_name = ["students"]
discussion_num = []


def read_discussion():
    os.chdir(os.getcwd())
    data = pandas.read_csv('students_data_FIX.csv',
                           usecols=[12]).values.tolist()
    for i in data:
        global discussion_num
        discussion_num.append(i[0])
    discussion_num = sorted(discussion_num)


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


factor_col = {
    "Relation": 8,
    "raisedhands": 9,
    "VisitedResources": 10,
    "AnnouncementsView": 11,
    "Discussion": 12,
    "ParentAnsweringSurvey": 13,
    "ParentschoolSatisfaction": 14,
    "StudentAbsenceDays": 15
}

selected_name = []
selected_num = []
selected_num_class = [[], [], []]
gender_dict = {
    "Boys": "M",
    "Girls": "F"
}


def select_data(academic_year, class_, nationality, gender, factor):
    print(factor_col[factor])
    data = pandas.read_csv("students_data_FIX.csv", usecols=[
                           0, 1, 4, 16, factor_col[factor]])
    total = 0
    selected_name.clear()
    selected_num.clear()
    selected_num_class[0].clear()
    selected_num_class[1].clear()
    selected_num_class[2].clear()
    temp_num = {}
    temp_num_class = [{}, {}, {}]
    for i in data.values:
        if(academic_year != '------' and i[2] != academic_year):
            continue
        if(class_ != '------' and str(i[-1]) != class_):
            continue
        if(nationality != '------' and i[1] != nationality):
            continue
        if(gender != '------' and i[0] != gender_dict[gender]):
            continue
        total += 1
        if(temp_num.get(i[-2]) == None):
            temp_num[i[-2]] = 1
        else:
            temp_num[i[-2]] = temp_num[i[-2]]+1
        if(class_ == "------"):
            if(temp_num_class[i[-1]-1].get(i[-2]) == None):
                temp_num_class[i[-1]-1][i[-2]] = 1
            else:
                temp_num_class[i[-1]-1][i[-2]
                                        ] = temp_num_class[i[-1]-1][i[-2]]+1
    for key, value in temp_num.items():
        selected_name.append(key)
        selected_num.append(value)
    for i in range(3):
        for value in temp_num_class[i].values():
            selected_num_class[i].append(value)
    return total


# select_data("G-04", "1", "Kuwait", "M", "Relation")
