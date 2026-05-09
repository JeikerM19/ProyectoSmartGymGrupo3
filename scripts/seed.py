import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.base import Base
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.maquina import Maquina
from app.models.categoria_maquina import CategoriaMaquina
from app.models.plan_suscripcion import PlanSuscripcion
from app.models.producto_tienda import ProductoTienda

# Credenciales obtenidas de tu docker-compose.yml
DATABASE_URL = "postgresql://admin_gym:ucla_computacion_2026@localhost:5433/smartgym_db"

def seed():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        print("Iniciando carga de datos...")
        roles_existentes = session.query(Rol).first()

        if roles_existentes:
            print("--- INFO: La base de datos ya tiene datos. Saltando carga para evitar duplicados. ---")
            return
            
        admin_rol = Rol(nombre="Administrador")
        entrenador_rol = Rol(nombre="Entrenador")
        cliente_rol = Rol(nombre="Cliente")
        session.add_all([admin_rol, entrenador_rol, cliente_rol])
        session.flush()

        admin_user = Usuario(
            nombre="Alex Barreto", 
            email="admin@smartgym.com", 
            password="ucla_2026_pass", 
            rol_id=admin_rol.id
        )
        session.add(admin_user)

        cardio = CategoriaMaquina(nombre="Cardio" )
        fuerza = CategoriaMaquina(nombre="Fuerza")
        flexibilidad = CategoriaMaquina(nombre="Flexibilidad")
        session.add_all([cardio, fuerza, flexibilidad])
        session.flush()

        maquinas = [
            Maquina(nombre="Cinta de Correr T80", categoria_id=cardio.id,descripcion="Cinta de correr de 80cm", estado="Operativa"),
            Maquina(nombre="Eliptica Pro", categoria_id=cardio.id,descripcion="Eliptica de 80cm", estado="Operativa"),
            Maquina(nombre="Prensa de Piernas", categoria_id=fuerza.id, descripcion="Prensa de piernas adjustable", estado="Mantenimiento"),
            Maquina(nombre="Banco de Pecho", categoria_id=fuerza.id, descripcion="Banco de pecho adjustable", estado="Operativa"),
            Maquina(nombre="Estacion de Poleas", categoria_id=fuerza.id, descripcion="Estacion de poleas multiusos", estado="Operativa")
        ]
        session.add_all(maquinas)

        planes = [
            PlanSuscripcion(nombre="Plan Mensual", precio=30.00, duracion_dias=30),
            PlanSuscripcion(nombre="Plan Anual", precio=300.00, duracion_dias=365)
        ]
        session.add_all(planes)

        productos = [
            ProductoTienda(nombre="Proteina Whey 1kg", precio=45.50, stock=20),
            ProductoTienda(nombre="Termo Inteligente", precio=15.00, stock=50),
            ProductoTienda(nombre="Toalla Microfibra", precio=8.00, stock=100)
        ]
        session.add_all(productos)

        session.commit()
        print("¡Carga completada con exito!")

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    seed()