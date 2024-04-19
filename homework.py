import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
print('\n')
data['robot'] = 1
data['human'] = 1
for i in range(len(data)):
    if data['whoAmI'].loc[i] == 'human':
        data.loc[i, "human"] = 1
        data.loc[i, "robot"] = 0
    elif data['whoAmI'].loc[i] == 'robot':
        data.loc[i, "human"] = 0
        data.loc[i, "robot"] = 1
data = data.drop('whoAmI', axis=1)
print(data.head())