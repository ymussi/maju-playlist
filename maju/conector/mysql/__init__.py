import os
from sqlalchemy import create_engine
from maju.config import read_config
from maju.conector.sql import SQLDBContext


def mysql_engine(schema, pool_size=1, max_overflow=25):
    dbname = read_config().get("schema", schema)
    con_str = read_config().get("database", dbname)
    engine = create_engine("{}/{}".format(con_str, schema),
                           pool_size=pool_size, max_overflow=max_overflow, pool_recycle=30 * 60)
    return engine

class CadastroDBContext(SQLDBContext):

    def __init__(self, engine):
        super().__init__(engine)