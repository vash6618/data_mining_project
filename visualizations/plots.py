import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict


region_map = {32: 'East South', 42: 'Pacific', 41: 'Mountain', 33: 'West South', 11: 'New England', 31: 'South Atlantic',
              21: 'East North', 22: 'West North', 12: 'Middle Atlantic'}

def income_vs_region(df):
    print("vs")
    wage_income = df['INCTOT'].dropna()
    region = df['REGION'].dropna()
    tot_inc = wage_income.to_list()
    reg = region.to_list()
    dp = defaultdict(list)

    for i in range(len(tot_inc)):
        if tot_inc[i] == 999999 or tot_inc[i] == 999998:
            continue
        dp[reg[i]].append(tot_inc[i])
    median_wage = {}
    for key in dp:
        dp[key].sort()
        median_wage[key] = dp[key][len(dp[key]) // 2]
    print(median_wage)

    x_values = list(median_wage.keys())
    x_values = [region_map[val] for val in x_values]
    y_values = [median_wage[key] for key in median_wage]
    ax = sns.barplot(x=x_values, y=y_values)
    ax.set(xlabel='Region', ylabel='income ($)')
    plt.title('Yearly Income vs Region')
    plt.show()


if __name__ == '__main__':
    file_name = '~/Downloads/2019_census_dataset.csv'
    df = pd.read_csv(file_name)
    print(df.loc[0])
    income_vs_region(df)


