# Data Mining
En aquest apartat explicaré el processament que he realitzat de les dades, juntament amb el raonament i les
decisions que he pres per posteriorment aplicar els models.

Abans de tot, mostraré la versió inicial de la base de dades per així poder contrastar-la amb la versió que obtingui
després de realitzar les modificacions.

Els següents fragments de codi mostren el tamany de la base de dades, les primeres 5 files i una descripció de les
estadísitques més rellevants:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Shape%20inicial.PNG)

```
train.head()
```
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Head%20inicial.PNG)

``` 
train.describe() 
```
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Describe%20inicial.PNG)

## NaN Values
Per començar amb el Data Mining, lo primer que me fixat és si n'hi han valors NaN a la base de dades. Mitjançant
el següent fragment de codi mostro si n'hi ha i en quines columnes en concret es troben:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/NaN%20inicial.PNG)

Com es pot veure si que n'hi ha valors NaN, i per tant faig un drop d'aquelles fileres que continguin:
``` 
train_m.dropna(inplace = True)
```
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Shape%20NaN.PNG)

## Variables Categòriques
El següent pas és analitzar i tractar totes les variables categòriques. Com he comentat a la Introducció n'hi ha 8:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Categorical%20columns.PNG)

A continuació aniré comentant cada variable, mostrant un recompte dels seus atributs, la seva distribució i els canvis, 
en cas de n'hi hagin. Però abans d'això, mencionar dos petits canvis que he realitzat:

He fet un rename de la variable *income_>50K* per que s'entengui millor quina és la variable objectiu:
```
train_m.rename(columns = {'income_>50K':'target'}, inplace = True)
```
He fet drop de la columna *educational-num* ja que és redundant amb la columna *education*:
```
train_m.drop(columns = {'educational-num'}, inplace = True)
```


### Workclass
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Workclass%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Workclass%20values.PNG)

Modificacions:
- He eliminat la classe *Without Pay* ja que no aporta gaire informació al tenir poques mostres
- Les classes State-gov, Federal-gov, i Local-gov les he combinat en una única classe *Government*
- Les classes Self-emp-not-inc i Self-emp-inc les he combinat en una única classe *Self-emp*

La distribució final de la variable quedaria:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Workclass%20plot%20modified.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Workclass%20values%20modified.PNG)



### Education
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Education%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Education%20values.PNG)

Modificacions:
- Les classes Preschool, 1st-4th i 5th-6th les he combinat en una única classe *Elementary-School*
- La classe 7th-8th la he substituit per *Middle-School* per així seguir un format
- Les classes 9th, 10th, 11th i 12th les he combinat en una única classe *High-School*
- Les classes HS-grad, Bachelors, Some-college, Assoc-voc i Assoc-acdm les he combinat en una única classe *College*
- Les classes Prof-school, Masters i Doctorate les he combinat en una única classe *Postgrade*

Per fer totes aquestes modificacions m'he basat en dos links que indiquen com és classifica el sistema educatiu en els EEUU,
ja que com més endavant mostraré, la majoria de les persones de la base de dades són dels EEUU.

Els links mencionats són:

https://iicana.org/asesoria-educativa/sistema-educativo-de-estados-unidos/

https://terralinda.srcs.org/pf4/cms2/view_page?d=x&group_id=1569050662403&vdid=i37d2axmn48u

La distribució final de la variable quedaria:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Education%20plot%20modified.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Education%20values%20modified.PNG)



### Marital Status
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Marital-status%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Marital-status%20values.PNG)

Modificacions:
- Les classes Married-civ-spouse, Married-spouse-absent i Married-AF-spouse les he combinat en una única classe *Married*

Per fer aquesta modificació també m'he basat en dos links que indiquen com és classifica els estats civils en els EEUU.

Els links mencionats són:

https://www.census.gov/library/visualizations/interactive/marital-status-in-united-states.html

https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=61748&CVD=61748&CLV=0&MLV=1&D=1

La distribució final de la variable quedaria:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Marital-status%20plot%20modified.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Marital-status%20values%20modified.PNG)



### Occupation
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Occupation%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Occupation%20values.PNG)

Per aquesta variable he decidit no realitzar cap modificació ja que totes les tenen uns values equilibrats.



### Relationship
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Relationship%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Relationship%20values.PNG)

Modificacions:
- Les classes Husband i Wife les he combinat en una única classe *Married*

He decidit realitzar aquesta modificació ja que considero que Married engloba tant Husband com Wife

La distribució final de la variable quedaria:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Relationship%20plot%20modified.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Relationship%20values%20modified.PNG)



### Race
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Race%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Race%20values.PNG)

Per aquesta variable no he realitzat cap modificació. Si que es pot observar perfectament que la majoria de les mostres d'aquesta
variable són de la classe 'White' i per tant segurament podrem descartar aquesta variable en un futur.



### Gender
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Gender%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Gender%20values.PNG)

Per aquesta variable no he realitzat cap modificació.



### Native-country
Distribució Inicial:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Native-country%20plot.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Native-country%20values.PNG)

Per aquesta variable no he realitzat cap modificació, però arribo a la mateixa conclusió que amb la variable *Race*, ja que la
majoria de les mostres són de la classe 'United-States', i per tant probablement la podrem descartar.



## Estandarització de les variables
Un cop visualitzades i tractades les variables categòriques és necessari convertir aquestes categories en valors numèrics. Això ho he implementat
mitjançant el següent bucle:

```
for x in categorical_columns:
    diccionari = dictionarize(train_m[x])
    train_m[x] = [diccionari[i] for i in train_m[x]]
```

La funció dictionarize està declarada a l'inici del codi i s'encarrega d'enumerar els valors únics de cada variable:

```
def dictionarize(data):
    valors_unics = data.unique()
    return { j: i + 1 for i, j in enumerate(valors_unics) }
```

Finalment, la base de dades quedaria de la següent forma:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Head%20final.PNG)

Mostro la correlació que hi ha entre variables tant amb un heatmap com amb un pairplot:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Heatmap%201.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Pairplot%201.png)

Clarament es veu que hi ha variables que no tenen cap correlació entre elles i la variable target i per tant decideixo fer un drop
d'aquestes. Les variables que elimino són: gender, education, fnlwgt, race i native-country.

```
train_m2 = train_m.copy()

train_m2 = train_m2[train_m2['race'] == 1]
train_m2 = train_m2[train_m2['native-country'] == 1]

train_m2.drop(columns = {'gender', 'education', 'fnlwgt', 'race', 'native-country'}, inplace = True)
```

Guardo aquest nou dataset en una altra variable per poder comprovar més tard quin dona millors resultats amb els models.

El heatmap i pairplot que obtinc ara són:

![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Heatmap%202.png)
![Image text](https://github.com/SergioBolca/Kaggle-APC-1496496/blob/01ace1c17a9af0748cfed5aac95cbb1113325f46/images/Pairplot%202.png)


Per finalitzar el procés de data mining, realitzo una normalització de les dades, ja que com s'ha pogut apreciar no totes
tenen el mateix rang. Per tant utilitzo StandardScaler de la llibreria sklearn:

```
X = train_m.values[: , :-1]
Y = train_m.values[: , -1]

X_2 = train_m2.values[: , :-1]
Y_2 = train_m2.values[: , -1]
```






