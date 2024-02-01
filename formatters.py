import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv(r'./env/resultados-1188ad0090b5ad16cc900cc78491d2616980840ce0282b67c67dd1562282c846.csv')

# Remover linhas que contenham 0800
df = df[~df['numero_celular'].str.contains('0800')]

# Limpar o formato do número de celular
df['numero_celular'] = df['numero_celular'].replace({'\(': '', '\)': '', '-': '', ' ': ''}, regex=True)

# Adicionar o prefixo +55 ao número de celular
df['numero_celular'] = '+55' + df['numero_celular']

# Salvar o resultado em um novo arquivo CSV
df.to_csv(r'resultado-formatado.csv', index=False)
