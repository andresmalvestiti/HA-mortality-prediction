import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import pandas as pd
import re

def outlier_diagnostic_plots(df, variable):
    fig,axes = plt.subplots(1,3,figsize=(20,4))

    sns.histplot(df[variable], bins=30,ax=axes[0], kde=True)
    axes[0].set_title('Histograma')
    
    stats.probplot(df[variable], dist="norm", plot=axes[1])
    axes[1].set_title('QQ')
    
    # boxplot    
    sns.boxplot(y=df[variable],ax=axes[2])
    axes[2].set_title('Box&Whiskers')

def is_string_or_number(value):
    return isinstance(value, (str, int, float, np.number))

def print_column_with_nan(df: pd.DataFrame, percentage_treshold: float = 0) -> None:
    for column in df.columns:
        na_count = sum(df[column].isna())
        na_percentage = ((na_count * 100) / len(df))
        if na_percentage >= percentage_treshold:
            print(f"{column} NaNs: {na_count} - {na_percentage}%")

def get_columns_with_nan(df: pd.DataFrame):
    columns_nan = []
    for column in df.columns:
        na_count = sum(df[column].isna())
        if na_count > 0:
            columns_nan.append(column)
    return columns_nan
        
# Función para limpiar los caracteres no deseados
def clean_value(value):
    if isinstance(value, str):
        value = value.strip()  # Hacer un trim
        if value == '':
            return np.nan
        return re.sub(r'[^0-9.,]', '', value)
    elif not isinstance(value, (int, float)):
        return np.nan
    return value

def outlier_diagnostic_plots(df, variable):
    fig,axes = plt.subplots(1,3,figsize=(20,4))

    sns.histplot(df[variable], bins=30,ax=axes[0], kde=True)
    axes[0].set_title('Histograma')
    
    stats.probplot(df[variable], dist="norm", plot=axes[1])
    axes[1].set_title('QQ')
    
    # boxplot    
    sns.boxplot(y=df[variable],ax=axes[2])
    axes[2].set_title('Box&Whiskers')