'''
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\Salary_Data.csv"),encoding = "Latin 1")
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
x_train,x_test,y_train,y_test=train_test_split(x,y)
test_size=0.3
random_state=0
model=LinearRegression()
model.fit(x_train,y_train)
#from here the testing of the data starts
y_pred=model.predict(x_test)
r2=r2_score(y_test,y_pred)
print("R_SquarredError",r2)
plt.scatter(x_train,y_train)
plt.plot(x_test,y_pred)
plt.show()
'''
'''
#random_state purpose? To shuffle the data.
#in y_pred, why x_test and not x_train? Coz of testing.


##From first hour lec which we missed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\Salary_Data.csv"),encoding = "Latin 1")

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

model=LinearRegression() #Creates a linear regression model
model.fit(x,y)          #Fits it to the dataset (x, y).

y_pred=model.predict(x) #Predicts Y values using the trained model.
r2=r2_score(y,y_pred)#Calculates R² score,which measures how well your model fits the data

print("R_Squared error",r2)

mae = mean_absolute_error(y, y_pred)
print("MAE = ", mae)


mse=mean_squared_error(y,y_pred)
print("MSE= ",mse)

rmse=np.sqrt(mse)
print("RMSE= ",rmse)

plt.scatter(x,y)
plt.plot(x,y_pred)
plt.show()
'''



'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error , mean_absolute_error, root_mean_squared_error
data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\Salary_Data.csv"),encoding = "Latin 1")
print(data.head())
x=data[['YearsExperience']].values
y=data['Salary'].values
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size =0.2, random_state = 42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred= model.predict(x_test)
print(model.coef_)
print(model.intercept_)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
print("R2 : ",r2)
print("Mean square error: ",mse)
print("Mean absolute error: ",mae)
print("Root mean square error: ",rmse)

plt.scatter(x,y)
plt.plot(x, model.predict(x), color = 'red')
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Simple Linear regression")
plt.show()

'''


'''
##Multilinear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\ecommerce_customers_unit1.csv"),encoding = "Latin 1")
print(data.head())
print(data.columns)
print(data.dtypes)
data = data.dropna()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['gender'] = le.fit_transform(data['gender'])

x=data[['age','gender']].values
y = data['churned'].values
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test, = train_test_split(x,y, test_size = 0.2, random_state = 42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Coefficent:",model.coef_)
print("Intercept:",model.intercept_)
print("R2 Score:",r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))


'''



'''
##Polynomial Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder

data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\Position_Salaries.csv"),encoding ="Latin 1")
print(data.head)
print(data.columns)
print(data.dtypes)
##le = LabelEncoder()
##data['Position']=le.fit_transform(data['Position'])
x=data[['Level']].values
y=data['Salary'].values
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
model = LinearRegression()
model.fit(x_poly, y)
y_pred = model.predict(x_poly)

plt.scatter(x,y, color='blue')
plt.plot(x,y_pred, color='red')
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.show()
print("R2 Score:", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
'''

'''
####Logistic Regression
##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, confusion_matrix
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data = sns.load_dataset("titanic")
print(data.head())
print(data.columns)
print(data.dtypes)

#data['age'].fillna(data['age'].mean(), inplace=True)    ##causes warning
##data['embarked'].fillna(data['embarked'].mode()[0], inplace=True)
data['age'] = data['age'].fillna(data['age'].mean())
data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])

data.drop(
    ['deck', 'alive', 'class', 'who', 'adult_male', 'embark_town'],
    axis=1,
    inplace=True
)
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'])
data['alone'] = le.fit_transform(data['alone'])

x = data.drop('survived', axis=1)
y = data['survived']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

'''
'''
#KNN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, confusion_matrix
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\Position_Salaries.csv"),encoding ="Latin 1")
print(data.head)
print(data.columns)
print(data.dtypes)
x=data[['Level']].values
y=data['Salary'].values
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
'''


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, confusion_matrix
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

data=pd.read_csv(("E:\\D drive\\SEM 5\\234\\Position_Salaries.csv"),encoding ="Latin 1")
print(data.head())
print(data.columns)
print(data.dtypes)
x=data[['Level']].values
y=data['Salary'].values

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4, random_state = 40)
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy:",accuracy_score(y_test, y_pred))


print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))
'''


'''
#DEcision TREE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
data = pd.read_csv(("E:\\D drive\\SEM 5\\234\\Position_Salaries.csv"),encoding ="Latin 1")
print(data.head())
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data['Position'] = le.fit_transform(data['Position'])

x=data[['Position','Level']].values
y=data['Salary'].values
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size =0.2, random_state=42)
model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Confusion Matrix:",confusion_matrix(y_test,y_pred))
/'''


'''
#SVM
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
data = pd.read_csv(("E:\\D drive\\SEM 5\\234\\Position_Salaries.csv"),encoding ="Latin 1")
print(data.head())
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data['Position'] = le.fit_transform(data['Position'])

x=data[['Position','Level']].values
y=data['Salary'].values

scaler = StandardScaler()
x= scaler.fit_transform(x)
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size =0.2, random_state=42)
model = SVC(kernel='linear')
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# from sklearn.metrics import roc_auc_score

# roc_auc = roc_auc_score(y_test, y_pred[:, 1])
# print("ROC_AUC:", roc_auc)
'''