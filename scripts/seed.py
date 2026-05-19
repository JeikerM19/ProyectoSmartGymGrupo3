import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.base import Base
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.maquina import Maquina
from app.models.categoria_maquina import CategoriaMaquina
from app.models.plan_suscripcion import PlanSuscripcion
from app.models.producto_tienda import ProductoTienda
from app.security import hash_password

# Usamos la URL de SQLite estándar (sincrónica) para no requerir aiosqlite
DATABASE_URL = "sqlite:///./sql_app.db"

def seed():

    engine = create_engine(DATABASE_URL)
    
    # Crea las tablas físicamente en el archivo .db
    print("Sincronizando tablas en la base de datos local...")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        print("Verificando datos existentes...")
        # Comprobamos si ya existen roles para no duplicar datos
        if session.query(Rol).first():
            print("--- INFO: La base de datos ya tiene datos. Saltando carga. ---")
            return

        print("Iniciando carga de datos...")
        
        # 1. Crear Roles básicos
        admin_rol = Rol(nombre="Administrador")
        entrenador_rol = Rol(nombre="Entrenador")
        cliente_rol = Rol(nombre="Cliente")
        financiero_rol = Rol(nombre="Financiero")
        session.add_all([admin_rol, entrenador_rol, cliente_rol, financiero_rol])
        session.flush() # Flush para obtener los IDs de los roles

        admin_user = Usuario(
            nombre="Alex Barreto", 
            email="admin@smartgym.com", 
            password=hash_password("12345"), 
            rol_id=admin_rol.id,
            estado="activo"
        )
        usuario_user = Usuario(
            nombre="Manuel", 
            email="usuario@smartgym.com", 
            password=hash_password("12345"),
            rol_id=cliente_rol.id,
            estado="activo"
        )
        session.add(admin_user)
        session.add(usuario_user)

        cardio = CategoriaMaquina(nombre="Cardio")
        session.add(cardio)
        session.flush()
        
        bici = Maquina(
            nombre="Bicicleta Estática v1", 
            categoria_id=cardio.id, 
            descripcion="Para calentamiento", 
            estado="Operativa"
        )
        session.add(bici)

        session.commit()
        print("¡Carga completada con éxito!")
        print(f"Ya puedes iniciar sesión con: admin@smartgym.com / 12345")

    except Exception as e:
        print(f"Error durante la carga: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    seed()