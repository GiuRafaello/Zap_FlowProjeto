import streamlit as st
import contrato
from pydantic import ValidationError
from datetime import datetime, time

def main():

    #Titulo:
    st.title("Sistema de CRM  e Vendas da ZapFlow -")

    #Entrada p dados:
    email = st.text_input("Campo de texto para inserção do email do Vendedor")
    data = st.date_input("Campo para selecionar a data da venda")
    hora = st.time_input("Hora da venda")
    valor = st.number_input("Valor da Venda")
    quantidade = st.number_input("Qtd Vendida")
    produto = st.selectbox("Campo para escolher o produto.",["ZapFlow com Gemini","ZapFlow com ChatGpt", "ZapFlow com Llama3.0"])

    #Botão Salvar
    if st.button("Salvar"):

        try:

            #Combinando a data e hora selecionadas para criar o datetime.

            data_hora = datetime.combine(data, hora)

            # Validando os dados com Pydantic

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            # Salvando os dados no PostgreSQL
            salvar_no_postgres(venda)
            st.success("Dados validados e salvos com sucesso!")

        except ValidationError as e:
            st.error(f"Erro de validação dos dados: {e}")
        except Exception as e:
            st.error(f"Erro ao salvar os dados: {e}")


if __name__ == "__main__":
    main()
