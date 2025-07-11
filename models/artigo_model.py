from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.configs import settings


class ArtigoModel(settings.DBBaseModel):
    __tablename__ = 'artigos'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(256))
    url_fonte = Column(String(256))
    descricao = Column(String(256))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')