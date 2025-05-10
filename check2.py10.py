import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('fp1.csv')
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.feature_selection import mutual_info_classif as MIC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import StackingClassifier
# Splitting the data into features and target
x=df.drop(['CLASS_LABEL','id'],axis=1)
y=df['CLASS_LABEL']
# Splitting the data into training and testing sets
mi_score = MIC(x,y,random_state=1)
l=[]
c=0
l1=list(x.columns.values.tolist())
print(len(mi_score))
l2=[]
for i in mi_score:
  if(i>0.11):
    l.append(c)
    l2.append(l1[c])
  c=c+1
#arr = np.where(mi_score>7)[0]
print(c)
print(l2)
print(mi_score)
#X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)