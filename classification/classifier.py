import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, f1_score, precision_score, \
    recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import attr_config


def classifier_logic(df):
    X = df[attr_config.attributes]
    y = df[['bins']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=47, test_size=0.10)

    clf = DecisionTreeClassifier(criterion='gini')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    ax = sns.heatmap(cm, annot=True, fmt='g')
    ax.set_title('Confusion Matrix with labels')
    ax.set_xlabel('Predicted Income bins')
    ax.set_ylabel('Actual Income bins')

    ax.xaxis.set_ticklabels(['i1', 'i2', 'i3', 'i4', 'i5', 'i6'])
    ax.yaxis.set_ticklabels(['i1', 'i2', 'i3', 'i4', 'i5', 'i6'])

    plt.show()
    print(cm)
    print(precision_score(y_true=y_test, y_pred=y_pred, average=None))
    print(recall_score(y_true=y_test, y_pred=y_pred, average=None))
    print(f1_score(y_true=y_test, y_pred=y_pred, average=None))
    print(f1_score(y_true=y_test, y_pred=y_pred, average='micro'))


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

    df_new = df.append(df_2010)
    classifier_logic(df_new)


if __name__ == '__main__':
    file_name_2019 = '~/Downloads/2019_census_dataset.csv'
    file_name_2010 = '~/Downloads/2010_census_dataset'
    predict_income_bins(file_name_2010, file_name_2019)