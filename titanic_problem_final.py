# data analysis and wrangling
import pandas as pd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv('data/train.csv')
data = pd.read_csv('data/train.csv')
to_drop = ['Ticket']
#Next we will clean the data, by inserting the mean value for any missing data for age
print(train_df.loc[:,"Age"].mean())
data["Age"].fillna("30", inplace = True) 
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)
print((data))
#Looking at the data we observe that sex, pc class, number of siblings and number of spouses are not missing any data, therefore we can plot this in order to determine which gender and class were the most likely to survive or perish. We also dropped ticket # as it had no impact on survival rate. 

grid = sns.FacetGrid(train_df, col = "Sex")
grid.map(plt.hist, "Survived")
#Based on the histogram above survived at 1 and dead at 0, we notice that males 20-30 were most likely to perish from the Titanic accidents with female deaths being much lower overall.

grid = sns.FacetGrid(train_df, col = "Pclass")
grid.map(plt.hist, "Survived")
#Based on the histogram above, we notice that those with 1st class seats were more likely to survive vs those from second that had roughly equal survival/death rates and 3rd class which had significantly more people dead than alive

grid = sns.FacetGrid(train_df, col = "SibSp")
grid.map(plt.hist, "Survived")
#Based on the histogram above, we notice that unless you had only 1 sibing or spouse, you were more likely to perish than survive. That may also indicate that married couples with 1 spouse were more likely to survie

grid = sns.FacetGrid(train_df, col = "Parch")
grid.map(plt.hist, "Survived")
#Based on the histogram above, we notice that unless you had only 1 child or parent, you were more likely to perish than survive. That may also indicate that married couples with 1 spouse were more likely to survie

grid = sns.FacetGrid(train_df, col = "Age")
grid.map(plt.hist, "Survived")
#Based on the histogram above survived at 1 and dead at 0, we notice that males 20-30 were most likely to perish from the Titanic accidents with female deaths being much lower overall.


