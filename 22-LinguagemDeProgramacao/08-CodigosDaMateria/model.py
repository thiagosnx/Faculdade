import pandas as pd
# importa bibliotecas e voce pode usar um alias para abreviar a biblioteca
# como por exemplo "pandas as pd"
dataFrame = {
    'Survived': [0, 1, 1, 1, 0],
    'Pclass': [3, 1, 3, 1, 3],
    'Name': ['Mr. Owen Harris Braund',
             'Mrs. John Bradley (Florence Briggs Thayer Cumings)',
             'Miss. Laina Heikkinen',
             'Mrs Jacques Heath (Lily May Peel) Futrelle',
             'Mr. William Henry Allen'],
    'Sex': ['male', 'female', 'female', 'female', 'male'],
    'Age': [22.0, 38.0, 26.0, 35.0, 35.0],
    'Siblings/Spouses Aboard': [1, 1, 0, 1, 0],
    'Parents/Children Aboard': [0, 0, 0, 0, 0],
    'Fare': [7.2500, 71.2833, 7.9250, 53.1000, 8.0500]
}
df_titanic = pd.DataFrame(dataFrame)
print(df_titanic)

homensnotitanic = df_titanic['male']
print(homensnotitanic)