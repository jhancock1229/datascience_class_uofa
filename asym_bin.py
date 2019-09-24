import pandas as pd
import numpy as np
import itertools
from math import sqrt

objects = ["One", "Two", "Three", "Four", "Five"]
df = pd.DataFrame({'Objects' : objects,
                   'Color' : ['red', 'green', 'red', 'blue', 'green'],
                   'Weather' : ['sunny', 'cloudy', 'cloudy', 'rainy', 'sunny'],
                   'Education' : ['L', 'H', 'H', 'H', 'L'],
                   'Test' : ['P', 'N', 'P', 'N', 'P'],
                   'Location' : [[1, 8], [3, 4], [5, 7], [6, 2], [9, 10]],
                   'Grade' : ['fair', 'good', 'excellent', 'good', 'fair']
                   },
                  columns=['Objects', 'Color', 'Weather', 'Education', 'Test', 'Location', 'Grade'])
df = df.set_index("Objects")
cc = list(itertools.combinations(objects, 2))
out = pd.DataFrame([df.loc[c, :].sum() for c in cc], index=cc)
print(out)
print(cc)
print(type(cc[0][0]))
x, y = cc[0]
print(x, y)
a = df.loc[x :y, ["Education", "Test"]]
print(a)
print(df.loc[['One', 'Two'], ["Education", "Test"]])
binomial_mapping = {"L" : 1, "P" : 1, "H" : 0, "N" : 0}
ordinal_ranking = {"fair" : 1, "good" : 2, "excellent" : 3}
df['Education'] = df['Education'].map(binomial_mapping)  # maps the Education into numberical value
df['Test'] = df['Test'].map(binomial_mapping)  # maps the Test into numberical value
df['Grade'] = df['Grade'].map(ordinal_ranking)

##############################################
def comparison(i, j, columns, data_frame) :
    q, r, s, t = 0, 0, 0, 0
    if data_frame.loc[i, columns].equals(data_frame.loc[j, columns]) :
        return "Identical"
    else :
        for k in columns :
            if data_frame.loc[i, k] and data_frame.loc[j, k] == 1 :
                q += 1
            if data_frame.loc[i, k] == 1 and data_frame.loc[j, k] == 0 :
                r += 1
            if data_frame.loc[i, k] == 0 and data_frame.loc[j, k] == 1 :
                s += 1
            if data_frame.loc[i, k] and data_frame.loc[j, k] == 0 :
                t += 1

    return ((r + s) / (q + r + s))


for pair in cc :
    pair = list(pair)
    x, y = pair[0], pair[1]
    asymmetric_measure = comparison(x, y, ["Education", "Test"], df)
    print("Objects {} and {}'s Asymmetric Measurement = {}".format(x, y, asymmetric_measure))
#############################
#####################################
def euclidean_distance(x, y) :
    return sqrt(sum([(x - y) ** 2 for x, y in zip(x, y)]))


for pair in cc :
    pair = list(pair)
    x = np.array(df.loc[pair[0], "Location"])
    y = np.array(df.loc[pair[1], "Location"])
    print("Objects {} and {}'s Euclidean Distance = {}".format(pair[0], pair[1], euclidean_distance(x, y)))
##########################################
##########################################


def normalize(r, m):
    return ((r-1)/(m-1))


df.loc["One", "Grade"] = normalize(df.loc["One", "Grade"], 3)
print(df.loc[:, "Grade"])