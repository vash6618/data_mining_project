import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict


region_map = {32: 'East South', 42: 'Pacific', 41: 'Mountain', 33: 'West South', 11: 'New England', 31: 'South Atlantic',
              21: 'East North', 22: 'West North', 12: 'Middle Atlantic'}
race_map = {1: 'White', 2: 'Black/African American', 3: 'American Indian', 4: 'Chinese', 5: 'Japanese',
            6: 'Pacific Islander', 7: 'Other race', 8: 'Biracial', 9: 'Three major races'}
education_map = {0: 'N/A', 1: 'Nursery-grade 4', 2: 'Grade 5-8', 3: 'Grade 9', 4: 'Grade 10', 5: 'Grade 11',
                 6: 'Grade 12', 7: '1 yr college', 8: '2 yrs college', 9: '3 yrs college', 10: '4 yrs college',
                 11: '5+ yrs college'}

def income_vs_graph(df, attribute, attribute1):
    total_income = df[attribute1].dropna()
    attr = df[attribute].dropna()
    tot_inc = total_income.to_list()
    attr = attr.to_list()
    dp = defaultdict(list)
    # {2: 0, 1: 0, 4: 0, 8: 0, 7: 0, 6: 0, 9: 0, 3: 0, 5: 0}
    for i in range(len(tot_inc)):
        if tot_inc[i] == 9999999 or tot_inc[i] == 99999:
            continue
        dp[attr[i]].append(tot_inc[i])
    median_wage = {}
    for key in dp:
        dp[key].sort()
        median_wage[key] = dp[key][len(dp[key]) // 2] if attribute1 == 'INCTOT' else (sum(dp[key])/len(dp[key]))
    print(median_wage)

    x_values = list(median_wage.keys())
    if attribute == 'REGION':
        x_values = [region_map[val] for val in x_values]
    else:
        x_values = [race_map[val] for val in x_values]
    y_values = [median_wage[key] for key in median_wage]
    ax = sns.barplot(x=x_values, y=y_values)
    ax.set(xlabel='Race' if attribute == 'RACE' else 'Region',
           ylabel='Total Income ($)' if attribute1 == 'INCTOT' else 'Welfare Income ($)'
           )
    first_title = 'Income Earned ' if attribute1 == 'INCTOT' else 'Welfare Income Earned '
    second_title = 'vs Race' if attribute == 'RACE' else 'vs Region'
    plt.title(first_title + second_title)
    plt.show()


def income_vs_scatter_plot(df, attribute):
    total_income = df['INCTOT'].dropna()
    attr = df[attribute].dropna()
    tot_inc = total_income.to_list()
    attr = attr.to_list()
    dp = defaultdict(list)

    for i in range(len(tot_inc)):
        if tot_inc[i] == 9999999 or tot_inc[i] == 999998:
            continue
        dp[attr[i]].append(tot_inc[i])
    median_wage = {}
    for key in dp:
        dp[key].sort()
        median_wage[key] = dp[key][len(dp[key]) // 2]
    x_values = list(median_wage.keys())
    y_values = [median_wage[key] for key in median_wage]
    title = 'Income correlation with Education level'
    plt.title(title)
    plt.xlabel('Education level')
    plt.ylabel('Income ($)')
    plt.xticks([0, 2, 4, 6, 8, 10], ['N/A', 'Grade 5-8', 'Grade 10', 'Grade 12', '2 yrs of college', '4 yrs college'])
    plt.scatter(x_values, y_values)
    plt.show()


def income_inequality(df, df_prev):
    tot_inc_2020 = df['INCTOT']
    tot_inc_2010 = df_prev['INCTOT']
    tot_inc2020 = tot_inc_2020.to_list()
    tot_inc2010 = tot_inc_2010.to_list()
    tot_inc2020 = [val/1000 for val in tot_inc2020 if val != 9999999 and val != 0 and val > 0]
    tot_inc2010 = [val/1000 for val in tot_inc2010 if val != 9999999 and val != 0 and val > 0]

    df1 = pd.DataFrame({"Year 2010": tot_inc2010}).assign(Year=2010)
    df2 = pd.DataFrame({"Year 2019": tot_inc2020}).assign(Year=2019)

    cdf = pd.concat([df1, df2])  # CONCATENATE
    mdf = pd.melt(cdf, id_vars=['Year'], var_name=['Number'])
    ax = sns.boxplot(x="Year", y="value", data=mdf, showfliers=False)  # RUN PLOT
    ax.set(ylabel='Income (in 1000s of $)')
    plt.title('Income disparity observed over a decade')
    plt.show()



if __name__ == '__main__':
    file_name_2019 = '~/Downloads/2019_census_dataset.csv'
    file_name_2010 = '~/Downloads/2010_census_dataset'
    df = pd.read_csv(file_name_2019)
    df_prev = pd.read_csv(file_name_2010)
    income_vs_graph(df, 'RACE', 'INCWELFR')
    income_vs_graph(df, 'REGION', 'INCTOT')
    income_vs_graph(df, 'RACE', 'INCTOT')
    income_vs_scatter_plot(df, 'EDUC')
    income_inequality(df, df_prev)
