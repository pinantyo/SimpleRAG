from sqlalchemy import Row
from typing import Tuple
from data import models
from data.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

def create_db():
    models.Base.metadata.create_all(engine)

def drop_db():
    models.Base.metadata.drop_all(engine)

def reset_db():
    drop_db()
    create_db()

    
class ContextDB:
    def create(self, context:str) -> None:
        with Session(engine) as session: 
            context = models.ContextInformation(context=context)
            session.add(context)
            session.commit()


    def get(self, ) -> None:
        with Session(engine) as session:
            query = select(models.ContextInformation)
            result = session.execute(query)
            return result.all()
        

    def find(self, id) -> None:
        with Session(engine) as session:
            query = select(models.ContextInformation).filter_by(id=id)
            result = session.execute(query)
            return result
        
    def update(self, id, context) -> None:
        with Session(engine) as session:
            query = models.ContextInformation
            query.id = id
            query.context = context
            session.add(query)
            session.commit()

    def delete(self, ):
        with Session(engine) as session:
            session.delete(models.ContextInformation)
            session.commit()