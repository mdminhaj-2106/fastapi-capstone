import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH



data = pd.read_csv(DATA_FILE_PATH)
data = data.drop_duplicates()
data = data.drop(columns=['Car_Name'])


X = data.drop(columns=['Selling_Price'])
y = data['Selling_Price'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

num_cols = list(X_train.select_dtypes(include='number').columns)
cat_cols = [col for col in X_train.columns if col not in num_cols]

num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', preprocessing.StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', preprocessing.OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])

regressor = RandomForestRegressor()

rf_model = Pipeline(steps=[
    ('pre', preprocessor),
    ('reg', regressor)
   ])

rf_model.fit(X_train, y_train)


os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_PATH)