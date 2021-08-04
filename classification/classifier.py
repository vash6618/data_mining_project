import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# [['STATEICP', 'SEX', 'AGE', 'RACE', 'EDUC', 'LABFORCE', 'INCWELFR', 'REGION', 'EMPSTAT', 'INCWAGE']]

def classifier_logic(df):
    X = df[['SEX', 'AGE', 'RACE', 'EDUC', 'LABFORCE', 'INCWELFR', 'EMPSTAT', 'INCWAGE']]
    y = df[['bins']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=47, test_size=0.10)
    print(X_train.shape, X_train.isnull().sum().sum())
    print(X_test.shape)
    print(y_train.shape, y_train.isnull().sum().sum())
    print(y_test.shape)

    clf = DecisionTreeClassifier(criterion='gini')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(accuracy_score(y_true=y_test, y_pred=y_pred))


def predict_income_bins(file_name_2010, file_name_2019):
    df_2010 = pd.read_csv(file_name_2010)
    df = pd.read_csv(file_name_2019)
    indexNames = df[(df['INCTOT'] == 9999999) | (df['INCTOT'] < 0)].index
    indexNames_2010 = df_2010[(df_2010['INCTOT'] == 9999999) | (df_2010['INCTOT'] < 0)].index
    df.drop(indexNames, inplace=True)
    df_2010.drop(indexNames_2010, inplace=True)

    bins = np.linspace(0, 50000, 3)
    high_bins = np.linspace(50000, 200000, 3)
    high_bins = np.delete(high_bins, 0)
    very_high_bins = np.linspace(200000, 500000, 3)
    very_high_bins = np.delete(very_high_bins, 0)
    bins = np.concatenate((bins, high_bins, very_high_bins))

    labels = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6']
    df['bins'] = pd.cut(df['INCTOT'], bins=bins, labels=labels, include_lowest=True)
    df_2010['bins'] = pd.cut(df_2010['INCTOT'], bins=bins, labels=labels, include_lowest=True)

    df.dropna(inplace=True)
    df_2010.dropna(inplace=True)

    print(df_2010.loc[0])
    df_new = df.append(df_2010)
    print(df_new.shape)
    print(df_new.shape, df_new.isnull().sum().sum())
    classifier_logic(df_new)


if __name__ == '__main__':
    file_name_2019 = '~/Downloads/2019_census_dataset.csv'
    file_name_2010 = '~/Downloads/2010_census_dataset'
    predict_income_bins(file_name_2010, file_name_2019)