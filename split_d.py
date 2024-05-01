from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('diabete.csv')
X_train,X_test,y_train,y_test = train_test_split(df[df.columns[:-1]],df[df.columns[-1]],test_size=0.1)

X_test.to_csv('test.csv')