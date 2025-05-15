import pandas as pd

#Função para converter coluna de data
def converter_para_datetime(data_str):
    try:
        mes, ano = data_str.strip().split()
        return pd.to_datetime(f"{ano}-{meses[mes]}-01")
    except Exception:
        return pd.NaT  

meses = {
    'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04',
    'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08',
    'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
}


caminho_csv = 'dados_ipca.csv'

df = pd.read_csv(caminho_csv, sep=';', skiprows=1)


df.columns = ['Codigo_territorio', 'Nivel_territorial', 'Brasil_codigo', 'Brasil', 'Variavel_codigo', 'IPCA_variavel', 'Mes_codigo', 'Mês_Ano', 'Codigo_grupo', 'Grupo', 'Unidade', 'Porcentagem' , 'Valor']

df.drop(columns=['Codigo_territorio', 'Nivel_territorial', 'Brasil_codigo', 'Brasil', 'Variavel_codigo', 'IPCA_variavel', 'Mes_codigo', 'Codigo_grupo', 'Unidade', 'Porcentagem'], inplace=True)

df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

df['Mês_Ano'] = df['Mês_Ano'].apply(converter_para_datetime)

df_pivot = df.pivot_table(index='Mês_Ano', columns='Grupo', values='Valor', aggfunc='first')

df_final = df.pivot(index="Mês_Ano", columns="Grupo", values="Valor").reset_index()

ordem_colunas = [ "Mês_Ano", "Índice geral", "1.Alimentação e bebidas", "2.Habitação", "3.Artigos de residência",  "4.Vestuário", "5.Transportes", "6.Saúde e cuidados pessoais", "7.Despesas pessoais",  "8.Educação", "9.Comunicação"]

df_final = df_final[ordem_colunas]

df_final.columns = ["Mês_Ano", "Índice geral", "Alimentação e bebidas", "Habitação", "Artigos de residência",
    "Vestuário", "Transportes", "Saúde e cuidados pessoais", "Despesas pessoais",
    "Educação", "Comunicação" ]

df_final.head()

# Salva o novo arquivo
df_final.to_csv('dados_ipca_transformados.csv', sep=';', index=False, encoding='utf-8-sig')
print("Transformação concluída. Arquivo salvo como 'dados_ipca_transformados.csv'.")