from sqlalchemy import select
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RespositorioSerie():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, serie: schemas.Serie):
        db_serie = models.Serie(titulo=serie.titulo,
                                ano=serie.ano,
                                genero=serie.genero,
                                qtd_temporadas=serie.qtd_temporadas)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)

        return db_serie

    def listar(self):
        series = self.db.query(models.Serie).all()
        return series

    def obter(self, serie_id: int):
        stmt = select(models.Serie).filter_by(id=serie_id)
        serie = self.db.execute(stmt).scalar_one()
        return serie

    def remover(self, serie_id: int):
        serie = self.obter(serie_id)

        self.db.delete(serie)
        self.db.commit()
