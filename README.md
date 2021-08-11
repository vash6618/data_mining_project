## US Census Data Analysis

### Overview
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


### Plots
1. One category of the plots is related to the data visualization. These plots are stored in the visualizations folder 
   and consist of boxplots, scatter plots and bar plots.
2. The other category of plots is related to data classification and it is stored inside the classifications folder.
    This consists of a plot of the confusion matrix to give a better representation of the classification model.


### Data Preprocessing
1. **Missing values** :- IPUMS dataset contains codes for each variable which specify missing or Null values. For all the attributes combined,
the total number of null or missing data records come out to be 0.05 % of the entire dataset. Those set of data records 
   are ignored from the computation.
2. **Binning** :- INCTOT is the attribute on which the classification is performed. This variable is numerical and to
perform classification on this, it is binned based on the range of values as well the US tax brackets.
   

### Income Disparity Analysis
The disparity analysis is compared over a decade by plotting boxplots to see the differences in income gap over that 
time period. Boxplots were plotted on the INCTOT attribute since it is one of the better indicators to determine income 
inequality. Boxplots were chosen as the visualization tool because it incredibly summarizes the numerical attribute of 
INCTOT and the inequality comparison becomes much easier to interpret and understand.


### Classification and Analysis
Decision Tree is used for classification purposes for this dataset. The group of attributes considered for the decision 
tree are mentioned inside the classification folder in the **attr_config** file. Gini impurity is used as criterion for
decision tree. Decision tree model is evaluated on the confusion matrix, f1 score, precision and recall score.

### Key Results
Confusion matrix is visulized and stored as a plot in the visualizations folder.\
All the scores below are across 6 income bins and finally an aggregated view of the f1 score is shown.
**precision_score** :- [0.84396603 0.85994548 0.86360066 0.86512934 0.83649289 0.89198218] \
**recall_score** :- [0.96888706 0.68608879 0.79178101 0.66455324 0.50597229 0.61285386] \
**f1_score** :- [0.90212249 0.76324175 0.82613287 0.75169125 0.63054481 0.72653061] \
**f1_score(average = ‘micro’)** :- 0.8511112437956598
