pip install beautifulsoup4


import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_table_from_url(url, table_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table', {'class': table_name})
    df = pd.read_html(str(table))[0]
    return df

def main():
    st.title('Extracción de tabla de una página web')

    url = st.text_input('Introduce la URL de la página:')
    table_name = st.text_input('Introduce el nombre de la tabla a extraer:')
    
    if st.button('Extraer tabla'):
        try:
            df = extract_table_from_url(url, table_name)
            st.write(df)

            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="tabla.csv">Descargar archivo CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

        except:
            st.error('No se pudo extraer la tabla de la página')

if __name__ == '__main__':
    main()
