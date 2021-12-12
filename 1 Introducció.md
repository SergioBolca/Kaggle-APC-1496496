# Introducció
La base de dades amb la qual he treballat per a realitzar aquest treball s'anomena 'Income Dataset', de l'usuari Mustafa 
Fatakdawala, obtinguda de la plataforma Kaggle.

El tòpic d'aquesta base de dades, com el seu nom indica, és a partir d'una sèrie de paràmetres, predir si el salari serà 
major de $50k o no. Ens trobem en un problema propi de classificació, idoni per aplicar aprenentatge computacional.

Abans d'entrar en matèria comentar que, per aquesta base de dades, l'usuari proporciona dos .csv: train.csv i test.csv.
Aclarir que en el meu cas només he treballat amb train.csv, ja que a l'hora de comprovar els models no podia fer-ho amb test.csv, ja
que no té una columna de target com a tal i, per tant, no tinc uns valors de referència per contrastar les prediccions dels models
amb els valors reals.

Per començar a treballar el primer que he fet és un anàlisi de les dades i els atributs que té la pròpia base de dades:

| Atribut | Descripció | Rang |
| ---------- | ---------- | :----------: |
| Age | Edat de la persona | 17 - 90 |
| Workclass | Tipus d'ofici | Categòrica |
| Fnlwgt | Salari final | 13.5k - 1.49m |
| Education | Nivell acadèmic | Categòrica |
| Educational-num | Nivell acadèmic en números | 1 - 16 |
| Marital-status | Estat civil | Categòrica |
| Occupation | Ofici | Categòrica |
| Relationship | Relació | Categòrica |
| Race | Raça de la persona | Categòrica |
| Gender | Gender | Male - Female |
| Capital-gain | Guany de capital | 0 - 100k |
| Capital-loss | Pèrdua de capital | 0 - 4356 |
| Hours-per-week | Hores que fa la persona per setmana | 1 - 99 |
| Native-country | Lloc de naixement | Categòrica |
| Income_>50k | Variable objectiu que indica si el salari és > 50k o <= 50k | 0 - 1 |

Com es pot veure, la base de dades està composta per 8 variables categòriques, 6 numèriques i 1 target, que en aquest cas seria 
*income_>50K*. Cal posar èmfasi en les variables categòriques, ja que serà necessari un tractament d'aquestes per poder treballar
amb dades numèriques a tota la base de dades i així aplicar posteriorment els diferents models.

Tota aquesta part de tractament de la base de dades està explicada al següent apartat: *2. Data Mining*.
