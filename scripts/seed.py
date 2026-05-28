import sys
import os
import asyncio
from datetime import datetime, date, time, timedelta

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.base import Base
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.cliente import Cliente
from app.models.entrenador import Entrenador
from app.models.maquina import Maquina
from app.models.categoria_maquina import CategoriaMaquina
from app.models.ticket_mantenimiento import TicketMantenimiento
from app.models.disciplina import Disciplina
from app.models.sesion_programada import SesionProgramada
from app.models.reserva import Reserva
from app.models.control_acceso import ControlAcceso
from app.models.plan_suscripcion import PlanSuscripcion
from app.models.membresia_cliente import MembresiaCliente
from app.models.pago import Pago
from app.models.producto_tienda import ProductoTienda
from app.models.venta_tienda import VentaTienda
from app.models.detalle_venta import DetalleVenta
from app.models.evaluacion_biometrica import EvaluacionBiometrica

from app.core.security import hash_password
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
            print("INFO: La base de datos ya tiene datos.")
            return

        admin_rol = Rol(nombre="Administrador", estado="activo")

        entrenador_rol = Rol(nombre="Entrenador", estado="activo")

        cliente_rol = Rol(nombre="Cliente", estado="activo")

        session.add_all([admin_rol, entrenador_rol, cliente_rol])

        await session.flush()

        admin_user = Usuario(
            nombre="Alex Admin",
            email="admin@gym.com",
            password=hash_password("Admin123*"),
            rol_id=admin_rol.id,
            estado="activo",
        )

        entrenador_user = Usuario(
            nombre="Carlos Entrenador",
            email="carlos@gym.com",
            password=hash_password("Entrenador123*"),
            rol_id=entrenador_rol.id,
            estado="activo",
        )

        cliente_user = Usuario(
            nombre="Manuel Cliente",
            email="manuel@gym.com",
            password=hash_password("Cliente123*"),
            rol_id=cliente_rol.id,
            estado="activo",
        )

        session.add_all([admin_user, entrenador_user, cliente_user])

        await session.flush()

        perfil_entrenador = Entrenador(
            especialidad="Crossfit Avanzado",
            usuario_id=entrenador_user.id,
            estado="activo",
        )

        perfil_cliente = Cliente(
            cedula="V-12345678",
            telefono="0414-1234567",
            fecha_registro=date.today(),
            usuario_id=cliente_user.id,
            estado="activo",
        )

        session.add_all([perfil_entrenador, perfil_cliente])

        await session.flush()

        cat_cardio = CategoriaMaquina(
            nombre="Cardio",
            descripcion="Máquinas de resistencia cardiovascular",
            estado="activo",
        )

        session.add(cat_cardio)

        await session.flush()

        caminadora = Maquina(
            nombre="Caminadora Pro",
            descripcion="Cinta de correr con inclinación",
            categoria_id=cat_cardio.id,
            estado="activo",
        )

        session.add(caminadora)

        await session.flush()

        ticket = TicketMantenimiento(
            descripcion="Cambio de banda elástica",
            fecha_apertura=datetime.utcnow(),
            costo=150.00,
            maquina_id=caminadora.id,
            usuario_id=admin_user.id,
            estado="activo",
        )

        session.add(ticket)

        crossfit = Disciplina(
            nombre="Crossfit", descripcion="Entrenamiento funcional", estado="activo"
        )

        session.add(crossfit)

        await session.flush()

        sesion_hoy = SesionProgramada(
            nombre="Extreme Bike",
            fecha=date.today(),
            hora_inicio=time(18, 0),
            hora_fin=time(19, 0),
            cupo_maximo=20,
            disciplina_id=crossfit.id,
            entrenador_id=perfil_entrenador.id,
            estado="activo",
        )

        session.add(sesion_hoy)

        await session.flush()

        reserva = Reserva(
            fecha_reserva=datetime.utcnow(),
            cliente_id=perfil_cliente.id,
            sesion_id=sesion_hoy.id,
            estado="activo",
        )

        session.add(reserva)

        evaluacion = EvaluacionBiometrica(
            fecha=date.today(),
            peso=78.5,
            estatura=1.75,
            porcentaje_grasa=16.5,
            cliente_id=perfil_cliente.id,
            observaciones="Buen avance muscular",
            estado="activo",
        )

        session.add(evaluacion)

        acceso = ControlAcceso(
            cliente_id=perfil_cliente.id,
            mensaje="Acceso permitido - Mensualidad al día",
            estado="activo",
        )

        session.add(acceso)

        plan_basico = PlanSuscripcion(
            nombre="Mensualidad Básica", precio=35.00, duracion_dias=30, estado="activo"
        )

        session.add(plan_basico)

        await session.flush()

        membresia = MembresiaCliente(
            fecha_inicio=date.today(),
            fecha_vencimiento=date.today() + timedelta(days=30),
            estado="activo",
            cliente_id=perfil_cliente.id,
            plan_id=plan_basico.id,
        )

        session.add(membresia)

        await session.flush()

        pago = Pago(
            monto=35.00,
            metodo_pago="Zelle",
            membresia_id=membresia.id,
            usuario_id=admin_user.id,
            estado="activo",
        )

        session.add(pago)

        agua = ProductoTienda(
            nombre="Botella de Agua 1L", precio=1.50, stock=100, estado="activo"
        )

        session.add(agua)

        await session.flush()

        venta = VentaTienda(total=3.00, cliente_id=perfil_cliente.id, estado="activo")

        session.add(venta)

        await session.flush()

        detalle = DetalleVenta(
            cantidad=2,
            venta_id=venta.id,
            producto_id=agua.id,
            estado="activo",
        )

        session.add(detalle)

        await session.commit()

        print("¡ÉXITO! Seed ejecutado correctamente.")

if __name__ == "__main__":
    asyncio.run(seed())
