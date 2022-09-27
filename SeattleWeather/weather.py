import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

seattle_df = pd.read_csv("seattle-weather.csv")
# print(seattle_df.to_string())
# print(seattle_df.head())
# print(seattle_df.describe())
# print(seattle_df.isnull().sum())
print(seattle_df['temp_max'].mode())
print(pd.value_counts(seattle_df['temp_max']).plot.bar())
pd.value_counts(seattle_df['temp_max']).plot.bar()
seattle_df['temp_max'].mode()