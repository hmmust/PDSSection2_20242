import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder
students_df = pd.read_csv('./part3/students.csv')
students_df['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
oh_encoder = OneHotEncoder(handle_unknown='ignore')
major_ohe= oh_encoder.fit_transform(students_df[['Major']])
feature_names = oh_encoder.get_feature_names_out(['Major'])
encoded_df = pd.DataFrame(major_ohe.toarray(),columns=feature_names)
print(encoded_df) 