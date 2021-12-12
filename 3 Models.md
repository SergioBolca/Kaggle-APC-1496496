# Models
Per resoldre aquest problema de Machine Learning he decidit utilitzar 4 models diferents per així poder
comparar-los entre ells. Els models en qüestió són:

- SVM
- Logistic Regressor
- KNN
- Decision Tree

He triat aquests 4 models ja que són els que més hem tractat tant a l'assignatura d'APC com a l'assignatura
de CRI i per tant amb els que estic més familiaritzat.

## Implementació
A continuació mostraré com he implementat cada model, quina opció he triat per a cadascun i el perqué.

### SVM
Per a l'SVM he decidit assignar al paràmetre *kernel* = poly. Això l'indica que serà polinomial l'equació,
ja que tinc diverses variables.

### Logistic Regressor
Per al Logistic Regressor he deixat tots els paràmetres a default.

### KNN
Per al KNN he assignat al paràmetre *n_jobs* = 1. Això l'indica al model que utilitzi tots els processadors. Els valor
dels veins mitjançant decideix el valor l'he deixat per defecte, per tant  *n_neighbors* = 5.

### Decision Tree
Per últim, a l'igual que al Logistic Regressor he deixat els paràmetres per defecte


## Codi
Com es pot veure, per a tots els models la majoria de paràmetres els he deixat per defecte. Això és degut a que he decidit
donar més importancia a aplicar cross-validation per així comprovar si el tamany de cada train set afectava als
resultats de cada model. 

Per aplicar aquest cross-validation he dividit les dades de test en un 0.25, 0.50 i 0.75 de les dades
mitjançant la funció train_test_split.

El codi final per aplicar els models és el següent:

```
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
```

A la següent secció *4. Resultats* mostraré els diferents resultats obtinguts per cada model.
