from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator, ValidationError
from datetime import datetime, time
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 =  "ZapFlow com Gemini"
    produto2 =  "ZapFlow com chatGPT"
    produto3 = "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    """
    Modelo de dados para as vendas. 

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor de compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade do produto
        produto (ProdutoEnum): categoria do produto
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @field_validator('data')
    def validar_intervalo_data(cls, v):
        inicio_intervalo = datetime(2025,1,31)
        fim_intervalo = datetime(2025,12,31,59,59)

        if not(inicio_intervalo <= v <= fim_intervalo):
            raise ValueError("A data da venda deve estar entre 01/01/2025 e 31/12/2025")
        return v
    @field_validator('produto')
    def categoria_deve_estra_no_enum(cls, v):
        return v

