import pandas as pd
from sklearn.datasets import load_iris

#create object
iris = load_iris()

#Create dataframe with four feature variables
df = pd.DataFrame(iris.data, columns=iris.feature_names)

#view top 5 rows
df.head()

#add new col with species name, which will be prediction
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

df.head()