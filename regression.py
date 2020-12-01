
import numpy as np 
import pandas as pd 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import linear_model

#various new tools we'll be using for this week! :0
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

url = 'https://github.com/millenopan/DGMI-Project/blob/master/insurance.csv?raw=true'
data = pd.read_csv(url)


#sex
le = LabelEncoder()
le.fit(data.sex.drop_duplicates()) 
data.sex = le.transform(data.sex)
# smoker or not
le.fit(data.smoker.drop_duplicates()) 
data.smoker = le.transform(data.smoker)
#region
le.fit(data.region.drop_duplicates()) 
data.region = le.transform(data.region)


X = data.drop(['charges'], axis = 1)
y = data.charges

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=83)

rf = RandomForestRegressor(n_estimators = 200, n_jobs = -1) 
# n_estimators = 200 means 200 trees, n_jobs = -1 uses all your CPU cores to compute them
rf.fit(X_train,y_train)
rf_pred_train = rf.predict(X_train)
rf_pred_test = rf.predict(X_test)

def predict(age, sex, bmi, children, smoker, region):
	sex = sex.lower()
	smoker = smoker.lower()
	region = region.lower()
	if sex == "female":
		num_sex = 0
	else:
		num_sex = 1
	if smoker == "yes":
		num_smoker = 1
	else:
		num_smoker = 0
	if region == "southwest":
		num_region = 3
	elif region == "southeast":
		num_region =2
	elif region == "northwest":
		num_region = 1
	else:
		num_region = 0

	return rf.predict(np.array([age, num_sex, bmi, children, num_smoker, num_region]).reshape(1, -1))


