## Introducció
La base de dades amb la qual he treballat per a realitzar aquest treball s'anomena 'Income Dataset', de l'usuari Mustafa Fatakdawala, obtinguda de la plataforma Kaggle.

El tòpic d'aquesta base de dades, com el seu nom indica, és a partir d'una sèrie de paràmetres, predir si el salari serà major de $50k o no. Ens trobem en un problema propi
de classificació, idoni per aplicar aprenentatge computacional.

Per començar a treballar el primer que he fet és un anàlisi de les dades i els atributs que té la pròpia base de dades:

| Atribut | Descripció | Rang |
| ---------- | ---------- | ---------- |
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
