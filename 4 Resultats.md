# Resultats
En aquest apartat mostraré quins han sigut els resultats que he obtingut per a cada model.

Testejo els models amb els dos datasets que he generat a l'apartat de Data Mining

Models amb el dataset complet:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/74df5c24e4cfd37611ef017e4484c7f8c3f1ef2e/images/Scores%20models%201.PNG)

Models amb el dataset reduït:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/74df5c24e4cfd37611ef017e4484c7f8c3f1ef2e/images/Scores%20models%202.PNG)

Per resumir els resultats he agafat els millors valors obtinguts de cada model:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Compare%20Models.PNG)

Amb aquesta imatge podem afirmar que el dataset amb el que obtenim millors resultats és aquell
que no hem modificat. Tot i així, la diferencia entre els dos datasets és molt petita.

Per últim, mostraré les matrix confusion obtingudes per a cada model:

### SVM
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Confusion%20Matrix%20SVM.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Stats%20SVM.PNG)


### Logistic Regressor
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Confusion%20Matrix%20Logistic.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Stats%20Logistic.PNG)


### KNN
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Confusion%20Matrix%20KNN.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Stats%20KNN.PNG)


### Decision Tree
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Confusion%20Matrix%20Decision%20Tree.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Stats%20Decision%20Tree.PNG)


Com a observació de tots el models podria dir que l'accuracy de mitja és d'un 80%, sent això bastant positiu. El valor del recall
és molt baix i això pot ser un indicador de que les dades no acaben d'estar balancejades.

Per confirmar aquesta hipòtesi, mostro la distribució general de la variable target, per així confirmar que efectivament
no hi ha un balanceig adequat de les dades.

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/faa7aa5a988b7c315ae87f0abbd935695df1f0ed/images/Data%20Distribution.PNG)

Per finalitzar, comentaré una serie de conclusions a la secció *5 Observacions i conclusions*.
