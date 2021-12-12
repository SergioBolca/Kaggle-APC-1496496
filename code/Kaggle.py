#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import seaborn as sns
import copy
import collections

from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score, precision_score, recall_score, plot_roc_curve
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, precision_recall_curve

from sklearn.model_selection import train_test_split

def dictionarize(data):
    valors_unics = data.unique()
    return { j: i + 1 for i, j in enumerate(valors_unics) }


# ## Introducció a la base de dades

# In[2]:


train = pd.read_csv('train.csv')
train.shape


# In[3]:


train.head()


# In[4]:


train.describe()


# ## Data Mining

# In[5]:


train_m = train.copy()
train_m.isnull().sum()


# In[6]:


train_m.dropna(inplace = True)


# In[7]:


print(train.shape)
print(train_m.shape)


# In[8]:


train_m.rename(columns = {'income_>50K':'target'}, inplace = True)

categorical_columns = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 
                       'race', 'gender', 'native-country']
categorical_columns


# In[9]:


train_m.drop(columns = {'educational-num'}, inplace = True)


# In[10]:


print(train_m['workclass'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "workclass")


# In[11]:


train_m.drop(train_m[train_m.workclass == 'Without-pay'].index, inplace = True)

train_m['workclass'].replace(['Self-emp-not-inc', 'Self-emp-inc'], 'Self-emp', inplace = True)
train_m['workclass'].replace(['Local-gov', 'State-gov', 'Federal-gov'], 'Government', inplace = True)

print(train_m['workclass'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "workclass")


# In[12]:


print(train_m['education'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "education")


# In[13]:


train_m['education'].replace(['Preschool', '1st-4th', '5th-6th'], 'Elementary-School', inplace = True)
train_m['education'].replace(['7th-8th'], 'Middle-School', inplace = True)
train_m['education'].replace(['9th', '10th', '11th', '12th'], 'High-School', inplace = True)
train_m['education'].replace(['HS-grad', 'Bachelors', 'Some-college', 'Assoc-voc', 'Assoc-acdm'], 'College', inplace = True)
train_m['education'].replace(['Prof-school', 'Masters', 'Doctorate',], 'Postgraduate', inplace = True)

print(train_m['education'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "education")


# In[14]:


print(train_m['marital-status'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "marital-status")


# In[15]:


train_m['marital-status'].replace(['Married-civ-spouse', 'Married-spouse-absent', 
                                   'Married-AF-spouse'], 'Married', inplace = True)

print(train_m['marital-status'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "marital-status")


# In[16]:


print(train_m['occupation'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "occupation")


# In[17]:


print(train_m['relationship'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "relationship")


# In[18]:


train_m['relationship'].replace(['Husband', 'Wife'], 'Married', inplace = True)

print(train_m['relationship'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "relationship")


# In[19]:


print(train_m['race'].value_counts(normalize = True) * 100)

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "race")


# In[20]:


print(train_m['gender'].value_counts())

plt.figure(figsize=(5,5))
sns.countplot(data = train_m, y = "gender")


# In[21]:


print(train_m['native-country'].value_counts(normalize = True) * 100)

plt.figure(figsize=(5,10))
sns.countplot(data = train_m, y = "native-country")


# In[22]:


print(train.shape)
print(train_m.shape)


# In[23]:


for x in categorical_columns:
    diccionari = dictionarize(train_m[x])
    train_m[x] = [diccionari[i] for i in train_m[x]]


# In[24]:


train_m.head()


# In[25]:


correlacio = train_m.corr()
plt.figure(figsize=(12,10))
ax = sns.heatmap(correlacio, annot=True, linewidths=0.5)


# In[26]:


relacio = sns.pairplot(train_m)


# In[27]:


train_m2 = train_m.copy()

train_m2 = train_m2[train_m2['race'] == 1]
train_m2 = train_m2[train_m2['native-country'] == 1]

train_m2.drop(columns = {'gender', 'education', 'fnlwgt', 'race', 'native-country'}, inplace = True)


# In[28]:


correlacio = train_m2.corr()
plt.figure(figsize=(12,10))
ax = sns.heatmap(correlacio, annot=True, linewidths=0.5)


# In[29]:


relacio = sns.pairplot(train_m2)


# In[30]:


X = train_m.values[: , :-1]
Y = train_m.values[: , -1]

X_2 = train_m2.values[: , :-1]
Y_2 = train_m2.values[: , -1]


# In[31]:


print(collections.Counter(Y))


# In[32]:


sc = StandardScaler()
X_n = sc.fit_transform(X)
X_n2 = sc.fit_transform(X_2)


# ## Aplicació dels models

# In[33]:


sizes = [0.25, 0.50, 0.75]
for size in sizes:
    x_train, x_test, y_train, y_test = train_test_split(X_n, Y, test_size = size, random_state = 0)
    
    #SVM
    svc = SVC(kernel = 'poly', probability=True)
    svc.fit(x_train, y_train)

    print("Score test - SVM with               ", size, "% of the data:" + str(svc.score(x_test, y_test)))
    print("Score train - SVM with              ", size, "% of the data:" + str(svc.score(x_train, y_train)))
    
    #Logistic Regressor
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)

    print("Score test - Logistic with          ", size, "% of the data:" + str(logreg.score(x_test, y_test)))
    print("Score train - Logistic  with        ", size, "% of the data:" + str(logreg.score(x_train, y_train)))
    
    #KNeighbors
    knn = KNeighborsClassifier(algorithm = 'auto', n_jobs = -1)
    knn.fit(x_train, y_train)

    print("Score test - KNN with               ", size, "% of the data:" + str(knn.score(x_test, y_test)))
    print("Score train - KNN with              ", size, "% of the data:" + str(knn.score(x_train, y_train)))
    
    #Decision Tree
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)

    print("Score test - Decision Tree with     ", size, "% of the data:" + str(clf.score(x_test, y_test)))
    print("Score train - Decision Tree with    ", size, "% of the data:" + str(clf.score(x_train, y_train)))


# In[34]:


sizes = [0.25, 0.50, 0.75]
for size in sizes:
    x_train, x_test, y_train, y_test = train_test_split(X_n2, Y_2, test_size = size, random_state = 0)
    
    #SVM
    svc = SVC(kernel = 'poly', probability=True)
    svc.fit(x_train, y_train)

    print("Score test - SVM with               ", size, "% of the data:" + str(svc.score(x_test, y_test)))
    print("Score train - SVM with              ", size, "% of the data:" + str(svc.score(x_train, y_train)))
    
    #Logistic Regressor
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)

    print("Score test - Logistic with          ", size, "% of the data:" + str(logreg.score(x_test, y_test)))
    print("Score train - Logistic  with        ", size, "% of the data:" + str(logreg.score(x_train, y_train)))
    
    #KNeighbors
    knn = KNeighborsClassifier(algorithm = 'auto', n_jobs = -1)
    knn.fit(x_train, y_train)

    print("Score test - KNN with               ", size, "% of the data:" + str(knn.score(x_test, y_test)))
    print("Score train - KNN with              ", size, "% of the data:" + str(knn.score(x_train, y_train)))
    
    #Decision Tree
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)

    print("Score test - Decision Tree with     ", size, "% of the data:" + str(clf.score(x_test, y_test)))
    print("Score train - Decision Tree with    ", size, "% of the data:" + str(clf.score(x_train, y_train)))


# In[35]:


x_train, x_test, y_train, y_test = train_test_split(X_n, Y, test_size = 0.25, random_state = 0)

svc = SVC(kernel = 'poly', probability=True)
svc.fit(x_train, y_train)

y_predictions = svc.predict(x_test)

acc = accuracy_score(y_test, y_predictions)
prec = precision_score(y_test, y_predictions)
rec = recall_score(y_test, y_predictions)

print(f'Accuracy:{acc}')
print(f'Precision:{prec}')
print(f'Recall:{rec}')
plot_confusion_matrix(svc, x_test, y_test, normalize='true')


# In[36]:


x_train, x_test, y_train, y_test = train_test_split(X_n, Y, test_size = 0.75, random_state = 0)

logreg = LogisticRegression()
logreg.fit(x_train, y_train)

y_predictions = logreg.predict(x_test)

acc = accuracy_score(y_test, y_predictions)
prec = precision_score(y_test, y_predictions)
rec = recall_score(y_test, y_predictions)

print(f'Accuracy:{acc}')
print(f'Precision:{prec}')
print(f'Recall:{rec}')
plot_confusion_matrix(logreg, x_test, y_test, normalize='true')


# In[37]:


x_train, x_test, y_train, y_test = train_test_split(X_n, Y, test_size = 0.25, random_state = 0)

knn = KNeighborsClassifier(algorithm = 'auto', n_jobs = -1)
knn.fit(x_train, y_train)

y_predictions = knn.predict(x_test)

acc = accuracy_score(y_test, y_predictions)
prec = precision_score(y_test, y_predictions)
rec = recall_score(y_test, y_predictions)

print(f'Accuracy:{acc}')
print(f'Precision:{prec}')
print(f'Recall:{rec}')
plot_confusion_matrix(knn, x_test, y_test, normalize='true')


# In[38]:


x_train, x_test, y_train, y_test = train_test_split(X_n, Y, test_size = 0.25, random_state = 0)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

y_predictions = clf.predict(x_test)

acc = accuracy_score(y_test, y_predictions)
prec = precision_score(y_test, y_predictions)
rec = recall_score(y_test, y_predictions)

print(f'Accuracy:{acc}')
print(f'Precision:{prec}')
print(f'Recall:{rec}')
plot_confusion_matrix(clf, x_test, y_test, normalize='true')