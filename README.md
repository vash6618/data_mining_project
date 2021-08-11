## Group 7 : US Census Data Analysis
### Team Members 
Vasu Sharma, Yan Zhan, Sutianjie Zhou
### Project Overview
Our aim was to identify certain socio-economic trends by analysing a person's 
educational background and their identity group to predict their earning potential, factors correlating to higher 
income, change in rate of return on education and income inequality over the past few decades. We were successfully 
able to achieve those objectives using data visualization, data cleaning and integration and classification algorithms.

### Dataset
Link to the dataset :- https://usa.ipums.org/usa-action/variables/group \
The dataset is collected from the organization IPUMS which provides consistent data with documentation. 
We are using the U.S. Census Person-Level data for our project. The 2019 sample is used for the visualization as 
well as for building the classification model. The size of this sample is around 806 MB and it has 3239553 rows and 
23 columns. Some of these columns contain important person-level information like race, age, gender, income, education, 
marital status and labor force participation.

### Questions sought to answer
1. What is the rate of change in income inequality in the U.S. over the past decade?
2. What factors are generally found to correlate with higher income?
3. What is the relation among a person’s educational     background, their identity group and earning potential?

### Knowledge gained
1. **Income Disparity Analysis** :- Through the use of visualizations like boxplots we were able to learn that the income gap has increased significantly 
over a decade. We used the dataset of 2019 and 2010 which have the same set of variables to do this comparison. We see 
that the **median income** has seen just a slight increase while upper middle class to rich population has seen a 
significant increase in prosperity. 
   
2. **Correlation** :-We also gained significant information about the correlation of different type of attributes with 
   earning potential. This was achieved through visualizations such as scatter plots and bar charts. Some of the 
   attributes that were found to directly correlate with income are education, region, welfare status, employee status, 
   labor force participation, marital status, race and sex.
3. **Classification** :- Decision Tree is used for classification purposes for this dataset. The group of attributes considered for the decision 
tree are mentioned inside the classification folder in the **attr_config** file. Gini impurity is used as criterion for
decision tree. Decision tree model is evaluated on the confusion matrix, f1 score, precision and recall score.


### Applications of the gained knowledge
Through our project we aimed to see various socio economic trends which are quite important to consider when evaluating the quality of life led by the individuals of that country.
1. **Federal and State governments** :- Governments need to constantly monitor and analyze the trends using the census data to make effective policy decisions for the citizens of the country. Currently, governments at the state and federal level do rely on census data analysis to come up with social and welfare programs as well as for designing policies when it comes to minority and underrepresented groups. Assessing economic well being, creating specialized programs for elderly and veterans are all reliant on the accuracy of the census data and its analytics.
2. **Business use cases** :- Businesses need to keep track of the trends using census data to market their products and services. For ex, businesses that manufacture household items like home furnishings and washing machines would benefit from analysing household trends across the country and businesses in the real estate domain would significantly benefit from knowing the composition of households and region as well as the rate at which people are selling their homes.
3. **Academic Research** :- Census data is the main source of truth when it comes to researching on topics like income inequality, increasing homelessness as well as identifying certain trends over a period of time. 

### Link to the video 
https://github.com/vash6618/data_mining_project/blob/main/07_USCensusDataAnalysis_Part6_Video.mp4
### Link to the presentation :-
https://github.com/vash6618/data_mining_project/blob/main/07_USCensusDataAnalysis_Part6.pdf

### Plots
1. One category of the plots is related to the data visualization. These plots are stored in the visualizations folder 
   and consist of boxplots, scatter plots and bar plots.
2. The other category of plots is related to data classification and it is stored inside the classifications folder.
    This consists of a plot of the confusion matrix to give a better representation of the classification model.
   


### Key Results
Confusion matrix is visulized and stored as a plot in the visualizations folder.\
All the scores below are across 6 income bins and finally an aggregated view of the f1 score is shown.
**precision_score** :- [0.84396603 0.85994548 0.86360066 0.86512934 0.83649289 0.89198218] \
**recall_score** :- [0.96888706 0.68608879 0.79178101 0.66455324 0.50597229 0.61285386] \
**f1_score** :- [0.90212249 0.76324175 0.82613287 0.75169125 0.63054481 0.72653061] \
**f1_score(average = ‘micro’)** :- 0.8511112437956598



