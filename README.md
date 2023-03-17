# Review Processing Model

## two set of Review dataset were Used:
1.  Reviews.csv: amazon product review dataset
2.  Review2.csv: IMDB movie Review dataset

## Model:

###   Naive Baye's model:
used python inbuild bayes model

```
from sklearn.naive_bayes import MultinomialNB
```
1. Accuracy: 0.8483126110124334

###   MyOwnModel:
the method Used:  score = Summation of(1 + log(tf))


## Testing:
```
Test no: 0
Accuracy: 0.805
precision: 0.41
test size:  200
correct:  161
number of negative Reviews: 200
negative Review detected: 82

Test no: 1
Accuracy: 0.775
precision: 0.385
test size:  200
correct:  155
number of negative Reviews: 200
negative Review detected: 77

Test no: 2
Accuracy: 0.72
precision: 0.395
test size:  200
correct:  144
number of negative Reviews: 200
negative Review detected: 79

Test no: 3
Accuracy: 0.735
precision: 0.35
test size:  200
correct:  147
number of negative Reviews: 200
negative Review detected: 70

Test no: 4
Accuracy: 0.69
precision: 0.26
test size:  200
correct:  138
number of negative Reviews: 200
negative Review detected: 52

Test no: 5
Accuracy: 0.745
precision: 0.38
test size:  200
correct:  149
number of negative Reviews: 200
negative Review detected: 76

Test no: 6
Accuracy: 0.79
precision: 0.375
test size:  200
correct:  158
number of negative Reviews: 200
negative Review detected: 75

Test no: 7
Accuracy: 0.71
precision: 0.445
test size:  200
correct:  142
number of negative Reviews: 200
negative Review detected: 89

Test no: 8
Accuracy: 0.785
precision: 0.415
test size:  200
correct:  157
number of negative Reviews: 200
negative Review detected: 83

Test no: 9
Accuracy: 0.71
precision: 0.27
test size:  200
correct:  142
number of negative Reviews: 200
negative Review detected: 54

average accuracy: 0.7464999999999999
average precision: 0.3685

```
