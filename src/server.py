from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schemas.schemas import Serie
from src.infra.sqlalchemy.repositorio.series import RespositorioSerie

# criar o banco de dados
criar_db()


app = FastAPI()


@app.post('/series')
def criar_serie(serie: Serie, db: Session = Depends(get_db)):
    serie_criada = RespositorioSerie(db).criar(serie)

    return serie_criada


@app.get('/series')
def listar_serie(db: Session = Depends(get_db)):
    return RespositorioSerie(db).listar()


@app.get('/series/{serie_id}')
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RespositorioSerie(db).obter(serie_id)

    return serie


@app.delete('/series/{serie_id}')
def remover_serie(serie_id: int, db: Session = Depends(get_db)):
    RespositorioSerie(db).remover(serie_id)

    return {'msg': 'Série removida do seu catálogo'}
