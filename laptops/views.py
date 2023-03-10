from django.shortcuts import render


import math

from tqdm import tqdm,trange
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

#KNN
from sklearn.neighbors import KNeighborsRegressor,KNeighborsClassifier

#Linear regression
from sklearn.linear_model import LinearRegression

#Random Forest
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import train_test_split

# from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

from sklearn.preprocessing import StandardScaler
# from math import sqrt
import random
from sklearn.metrics import mean_squared_error, r2_score
# import numpy as np
random.seed(0)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import r2_score,mean_absolute_error

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor,ExtraTreesRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor

# Create your views here.

def index(request):
    return render(request,'landing.html')

def predict(request):
    context={
        'values': request.POST,
    }

    if request.method == "POST":
        ssd = request.POST['ssd']
        ram = request.POST['ram']
        display = request.POST['display'] 
        status = request.POST['status']
        brand = request.POST['brand'].upper()

        excel_file = r'C:\Users\Lenovo\Jupeter\RMT\marketplaces_parsing\Endterm\df.xlsx'
        df = pd.read_excel(excel_file)
        
        label_encoder = preprocessing.LabelEncoder()
        p_brand = df['brand']
        p_status = df['status']

        df['brand'] = label_encoder.fit_transform(df['brand'])
        df['status'] = label_encoder.fit_transform(df['status'])

        brand_v = dict(zip(list(p_brand),df['brand'].to_list()))
        status_v = dict(zip(list(p_status),df['status'].to_list()))

        # model = pd.read_pickle(r"C:\Users\Lenovo\Jupeter\RMT\marketplaces_parsing\Endterm\random.pickle")
        model = pd.read_pickle(r"C:\Users\Lenovo\Jupeter\RMT\marketplaces_parsing\Endterm\random_full_dataset.pickle")


        result = model.predict([[brand_v[brand],display,ssd,ram,status_v[status]]])

        context['predict'] = int(result[0])

    return render(request,"form1.html",context)