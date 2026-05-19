import sys
import os
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.base import Base
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.maquina import Maquina
from app.models.categoria_maquina import CategoriaMaquina
from app.security import hash_password
from app.core.config import settings


DATABASE_URL = settings.database_url

engine = create_async_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        result = await session.execute(select(Rol))
        if result.scalars().first():
            print("INFO: DB ya tiene datos. Seed cancelado.")
            return

        # ROLES
        admin_rol = Rol(nombre="Administrador")
        entrenador_rol = Rol(nombre="Entrenador")
        cliente_rol = Rol(nombre="Cliente")
        financiero_rol = Rol(nombre="Financiero")

        session.add_all([admin_rol, entrenador_rol, cliente_rol, financiero_rol])
        await session.flush()

        # USUARIOS
        admin_user = Usuario(
            nombre="Alex Barreto",
            email="admin@smartgym.com",
            password=hash_password("12345"),
            rol_id=admin_rol.id,
            estado="activo",
        )

        usuario_user = Usuario(
            nombre="Manuel",
            email="usuario@smartgym.com",
            password=hash_password("12345"),
            rol_id=cliente_rol.id,
            estado="activo",
        )

        session.add_all([admin_user, usuario_user])

        # CATEGORÍA
        cardio = CategoriaMaquina(nombre="Cardio")
        session.add(cardio)
        await session.flush()

        # MÁQUINA
        bici = Maquina(
            nombre="Bicicleta Estática v1",
            categoria_id=cardio.id,
            descripcion="Para calentamiento",
            estado="Operativa",
        )

        session.add(bici)

        await session.commit()
        print("OK: Seed ejecutado correctamente")


if __name__ == "__main__":
    asyncio.run(seed())
