
from typing import List, Optional

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        from_attributes = True
        

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]


class UsarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    eh_admin: Optional[bool] = None