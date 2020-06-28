from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func, asc
from sqlalchemy_utils import generic_repr

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from maju.conector.mysql import mysql_engine

session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=mysql_engine("maju_playlist")))

Base = declarative_base()
Base.query = session.query_property()


@generic_repr
class CRUDMixin:
    """
    Mixin that adds convenience methods for CRUD (create, read, update, delete) operations.
    """

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        session.add(self)
        if commit:
            try:
                session.commit()
            except Exception as exc:
                print(f'Error in function create_obj, exception: {exc} ')
                session.rollback()
                raise
            finally:
                session.close()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        session.delete(self)
        return commit and session.commit()

    def as_dict(self, filter_columns=None, enum_values=None):
        """
        :param `filter_columns` lista de colunas que serão filtradas do resultado final
        :param `enum_values`  flag para indicar se você deseja retornar os valores em tipo Enum ou seus Valores.
        """
        dret = {}

        if not filter_columns:
            filter_columns = []

        for column in self.__table__.columns:
            if column.name in filter_columns:
                continue

            val = getattr(self, column.name)

            if enum_values:
                if isinstance(val, Enum):
                    val = val.value

            dret[column.name] = val
        return dret
    
    @classmethod
    def get_statistics(cls):
        instance = session.query(cls.city, \
            func.count(cls.city).label('count'), \
            func.max(cls.created).label('last_created')).group_by(cls.city).\
                order_by(cls.city.asc())
        return instance

class Model(CRUDMixin, Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        if any(
                (isinstance(record_id, (str, bytes)) and record_id.isdigit(),
                 isinstance(record_id, (int, float))),
        ):
            return cls.query.get(int(record_id))
        return None