import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import datetime


train_df = pd.read_csv('dados/train.csv')
teste_df = pd.read_csv('dados/test.csv')


lr_model = LinearRegression()


#separar dataset  em 70% para treinamento e 30% para validação
#regressão logistica
#taxa de acerto do modelo
#melhorar modelo
#usar modelo do dataset de teste
#criar answer.csv com inscrição e nota

print(train_df['TP_DEPENDENCIA_ADM_ESC'].corr(train_df['NU_NOTA_REDACAO']))

#cov = train_df.cov()
#corr = train_df.corr()