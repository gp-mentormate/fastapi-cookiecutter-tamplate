from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class DBSessionMixinInterface(ABC):
    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass


class SQLAlchemySessionMixin(DBSessionMixinInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
