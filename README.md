# Titanic Survival Analysis

Exploratory data analysis of the Titanic passenger list: who survived, and why.

✅ **Completed by Ketan Khanna** · Foundations of Data Science (SCS 3250), University of Toronto · Winter 2020

## What's Inside
| File | Description |
|---|---|
| `titanic_survival.ipynb` | The full analysis with charts |
| `titanic_problem_final.py` | The submitted script version |

## Approach
- Filled missing ages with the mean age (about 30) and dropped the ticket number, which has no bearing on survival
- Compared survival across sex, passenger class, siblings/spouses aboard, parents/children aboard, age and port of embarkation with faceted histograms

## Key Findings
- **Sex was the strongest signal:** most women survived while most men did not ("women and children first")
- **Class mattered:** first class mostly survived, second class was roughly even and third class mostly perished
- Passengers travelling with exactly one sibling/spouse or one parent/child did better than those alone or in large families
- Adults aged 20-40 made up most survivors, while elderly passengers were the most likely to perish

## Data
Kaggle [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data). Download `train.csv` into `data/` to run the notebook.

## Tools
Python · pandas · seaborn · matplotlib
