import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate
import xgboost as xgb

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
               'selfStudyRatio', 'raisedhands', 'Discussion', 'VisitedResources']
X = df_new[select_cols]
y = df_new['Class']

param = {
    "max_depth": 5,
    "learning_rate": 0.1,
    "n_estimators": 60,
}

estimator = xgb.sklearn.XGBRegressor(**param)
scores = cross_validate(estimator, X=X, y=y, cv=5,
                        return_train_score=True, return_estimator=True)

print(scores['train_score'].mean())
print(scores['test_score'].mean())

for idx, estimator in enumerate(scores['estimator']):
    print("Features sorted by their score for estimator {}:".format(idx))
    feature_importances = pd.DataFrame(estimator.feature_importances_,
                                       index=select_cols,
                                       columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)