#!/usr/bin/env python3
"""db operations"""
from models.blog import Blog
from models.user import User
from models.base_model import Base
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


classes = {'User': User, 'Blog': Blog}


class DB():
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def new(self, obj) -> None:
        """ add new user or blog to db
        """
        self._session.add(obj)

    def save(self) -> None:
        """Save to db"""
        self._session.commit()

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes.values():
            if cls is None or cls is clss:
                objs = self._session.query(clss).order_by(desc(clss.created_at)).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return (new_dict)
    
    def delete(self, obj=None):
        """delete user or blog"""
        if obj is not None:
            self._session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self._session.remove()

    def get(self, cls, id):
        """A method to retrieve one object"""
        if cls not in classes.values():
            return None
        try:
            return self._session.query(cls).get(id)
        except Exception:
            return None
        
    def find_user_by(self, **kwargs) -> User:
        """query users"""
        try:
            for key in kwargs:
                if not hasattr(User, key):
                    raise InvalidRequestError()
            res = self._session.query(User).filter_by(**kwargs).first()
            if res is None:
                raise NoResultFound()
            return res
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
