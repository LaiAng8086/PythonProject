import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate, GridSearchCV
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

CSV_FILE_PATH = './students_data_FIX.csv'
CSV_OUTPUT_PATH = './output.csv'

# Part 1 - data processing

def target_encoding(name, dataframe, m=1):
    overall = dataframe['Class'].mean()
    dataframe['freq'] = dataframe.groupby(name)[name].transform('count')
    dataframe[name + '_encoded'] = dataframe.groupby(name)['Class'].transform('mean')
    dataframe['weight'] = dataframe['freq'] / (dataframe['freq'] + m)
    dataframe[name + '_encoded'] = dataframe['weight'] * dataframe[name + '_encoded'] + (
                1 - dataframe['weight']) * overall
    return dataframe


df = pd.read_csv(filepath_or_buffer=CSV_FILE_PATH)

df_new = df.copy()
# gender
gender = df_new['gender'].value_counts()
gender_map = dict((v, i) for i, v in enumerate(gender.index))
df_new['gender'] = df_new.replace({'gender': gender_map})['gender']
target_encoding('gender', df_new)
# Nationality
nationality = df_new['Nationality'].value_counts()
nationality_map = dict((v, i) for i, v in enumerate(nationality.index))
df_new['Nationality'] = df_new.replace({'Nationality': nationality_map})['Nationality']
target_encoding('Nationality', df_new)
# PlaceofBirth
placeofBirth = df_new['PlaceofBirth'].value_counts()
placeofBirth_map = dict((v, i) for i, v in enumerate(placeofBirth.index))
df_new['PlaceofBirth'] = df_new.replace({'PlaceofBirth': placeofBirth_map})['PlaceofBirth']
target_encoding('PlaceofBirth', df_new)
# StageID
stageID = df_new['StageID'].value_counts()
stageID_map = {'lowerlevel': 0, 'MiddleSchool': 1, 'HighSchool': 2}
df_new['StageID'] = df_new.replace({'StageID': stageID_map})['StageID']
target_encoding('StageID', df_new)
# GradeID
gradeID = df_new['GradeID'].value_counts()
gradeID_map = {'G-02': 2, 'G-03': 3, 'G-04': 4, 'G-05': 5, 'G-06': 6, 'G-07': 7, 'G-08': 8,
               'G-09': 9, 'G-10': 10, 'G-11': 11, 'G-12': 12}
df_new['GradeID'] = df_new.replace({'GradeID': gradeID_map})['GradeID']
target_encoding('GradeID', df_new)
# SectionID
sectionID = df_new['SectionID'].value_counts()
sectionID_map = {'A': 0, 'B': 1, 'C': 2}
df_new['SectionID'] = df_new.replace({'SectionID': sectionID_map})['SectionID']
target_encoding('SectionID', df_new)
# Topic
topic = df_new['Topic'].value_counts()
topic_map = dict((v, i) for i, v in enumerate(topic.index))
df_new['Topic'] = df_new.replace({'Topic': topic_map})['Topic']
target_encoding('Topic', df_new)
# Semester
semester = df_new['Semester'].value_counts()
semester_map = dict((v, i) for i, v in enumerate(semester.index))
df_new['Semester'] = df_new.replace({'Semester': semester_map})['Semester']
target_encoding('Semester', df_new)
# Relation
relation = df_new['Relation'].value_counts()
relation_map = dict((v, i) for i, v in enumerate(relation.index))
df_new['Relation'] = df_new.replace({'Relation': relation_map})['Relation']
target_encoding('Relation', df_new)
# raisedhands
# VisitedResources
# AnnouncementsView
# Discussion
# ParentAnsweringSurvey
parentAnsweringSurvey = df_new['ParentAnsweringSurvey'].value_counts()
parentAnsweringSurvey_map = {'Yes': 1, 'No': 0}
df_new['ParentAnsweringSurvey'] = \
    df_new.replace({'ParentAnsweringSurvey': parentAnsweringSurvey_map})['ParentAnsweringSurvey']
target_encoding('ParentAnsweringSurvey', df_new)
# ParentschoolSatisfaction
parentschoolSatisfaction = df_new['ParentschoolSatisfaction'].value_counts()
parentschoolSatisfaction_map = {'Bad': 0, 'Good': 1}
df_new['ParentschoolSatisfaction'] = \
    df_new.replace({'ParentschoolSatisfaction': parentschoolSatisfaction_map})['ParentschoolSatisfaction']
target_encoding('ParentschoolSatisfaction', df_new)
# StudentAbsenceDays
studentAbsenceDays = df_new['StudentAbsenceDays'].value_counts()
studentAbsenceDays_map = {'Under-7': 0, 'Above-7': 1}
df_new['StudentAbsenceDays'] = \
    df_new.replace({'StudentAbsenceDays': studentAbsenceDays_map})['StudentAbsenceDays']
target_encoding('StudentAbsenceDays', df_new)
# Class
df_new['Class'] = df_new['Class'] * 20 + 40

del df_new['freq'], df_new['weight']


df_new.to_csv(CSV_OUTPUT_PATH)


# Part 2 - add new features
# df_new['Positivity'] = df_new['raisedhands'] + df_new['Discussion'] + df_new['VisitedResources']
df_new['selfStudyRatio'] = df_new['VisitedResources'] / (df_new['raisedhands'] + df_new['Discussion'])
df_new = df_new[['gender_encoded', 'Nationality_encoded', 'PlaceofBirth_encoded',
                 'StageID_encoded', 'GradeID_encoded', 'SectionID_encoded',
                 'Topic_encoded', 'Semester_encoded', 'Relation_encoded', 'VisitedResources',
                 'AnnouncementsView', 'Discussion', 'ParentAnsweringSurvey_encoded',
                 'ParentschoolSatisfaction_encoded', 'StudentAbsenceDays_encoded',
                 'selfStudyRatio', 'Class'
                 , 'raisedhands', 'Discussion', 'VisitedResources']]
df_new.to_csv('./new_students_data_FIX.csv')


# Part 3 - train models
#TODO: grid search
df_new = pd.read_csv(filepath_or_buffer='./new_students_data_FIX.csv')
select_cols = ['Relation_encoded', 'AnnouncementsView', 'ParentAnsweringSurvey_encoded',
               'ParentschoolSatisfaction_encoded', 'StudentAbsenceDays_encoded',
               'selfStudyRatio', 'raisedhands', 'Discussion', 'VisitedResources',
               'Topic_encoded', 'GradeID_encoded']
X = df_new[select_cols]
y = df_new['Class']

params = {"n_estimators": [50, 100, 150, 200, 300], "max_depth": [2, 3, 4, 5, 6],
          'min_child_weight': [1, 3, 5]}

# reg = xgb.sklearn.XGBRegressor(learning_rate=0.05)
# clf = GridSearchCV(reg, params, cv=5, verbose=1, n_jobs=-1, error_score='raise')

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                random_state=0)
my_model = xgb.sklearn.XGBRegressor(random_state=0, n_estimators=100, learning_rate=0.05) # Your code here
my_model.fit(X_train, y_train)
predictions = my_model.predict(X_valid)

# clf.fit(X_train, y_train)
# predictions = clf.predict(X_valid)
# print(clf.best_params_)
error_num = 0

print(y_valid.head())
print(type(y_valid))
print(type(predictions))
y_valid = list(y_valid)
print(y_valid[:5])
predictions = list(predictions)


for i in range(len(predictions)):
    if predictions[i] > 90:
        predictions[i] = 100
    elif predictions[i] > 70:
        predictions[i] = 80
    else:
        predictions[i] = 60
    if predictions[i] != y_valid[i]:
        error_num += 1

print(error_num / len(predictions))

mae = mean_absolute_error(predictions, y_valid)
print(mae)




