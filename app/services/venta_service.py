from sqlalchemy.ext.asyncio import AsyncSession
from app.models.venta_tienda import VentaTienda
from app.models.detalle_venta import DetalleVenta
from app.services.base_service import CRUDBase
from app.services.venta_detalle_service import detalle_venta_service # Tu servicio que valida stock

class CRUDVenta(CRUDBase[VentaTienda]):

    async def crear(self, db: AsyncSession, *, obj_in: dict) -> VentaTienda:
        # 1. Separamos los detalles del resto de la data (la cabecera)
        # Esto hace que 'detalles' no intente guardarse en la tabla Venta
        detalles_lista = obj_in.pop("detalles", []) 
        
        # 2. Creamos el objeto de la cabecera (Tabla Venta)
        nueva_venta = VentaTienda(**obj_in)
        db.add(nueva_venta)
        
        # 3. Flusheamos para obtener el ID de la venta recién creada
        await db.flush() 
        
        # 4. Ahora procesamos cada detalle (Tabla DetalleVenta)
        for det in detalles_lista:
            # Aquí usamos el servicio que valida y resta stock
            # Le asignamos manualmente el ID de la venta a cada detalle
            det["venta_id"] = nueva_venta.id
            await detalle_venta_service.crear(db, obj_in=det)

        # 5. Commit final: Todo se guarda al mismo tiempo
        await db.commit()
        await db.refresh(nueva_venta)
        
        return nueva_venta
    
venta_service = CRUDVenta(VentaTienda)