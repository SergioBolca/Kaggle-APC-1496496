# Data Mining
A partir d'una visió general de les dades, començo a realitzar les modificacions pertinents.

En primer lloc, faig un drop d'aquelles fileres que tinguin valors NaN. Abans d'això comprobo si he de fer el drop tant per al conjunt de test com per al de train:
```
print(db_train.isnull().sum())
print(db_test.isnull().sum())
```
![NaN Train](https://user-images.githubusercontent.com/72317069/145294350-7e0dcca6-5d8b-4bea-adf3-68f908afbfde.png)
![NaN Test](https://user-images.githubusercontent.com/72317069/145294353-627c5a62-b19e-4315-a8c6-ba1a915092c7.png)


Només aplico dropna() al conjunt de train, ja que el conjunt de test no te valors NaN:
```
db_train = db_train.dropna()
```
