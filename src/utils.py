from sqlalchemy.ext.asyncio import AsyncSession


class DBSessionMixin:
    def __init__(self, session: AsyncSession):
        self.session = session
