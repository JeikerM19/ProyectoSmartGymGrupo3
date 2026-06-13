from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base_service import CRUDBase
from app.models.producto_tienda import ProductoTienda
from app.core.exceptions import ReglaNegocioException 

class CRUDProductoTienda(CRUDBase[ProductoTienda]):
    
    async def crear(self, db: AsyncSession, *, obj_in: dict) -> ProductoTienda:
        stock = obj_in.get("stock")


        if stock is not None and stock <= 0:
            raise ReglaNegocioException(
                codigo_interno="ERR_STOCK_INVALIDO",
                mensaje=f"No se puede registrar el producto. El stock inicial ({stock}) no puede ser negativo ni cero."
            )
        elif stock is None:
            raise ReglaNegocioException(
                codigo_interno="ERR_STOCK_REQUERIDO",
                mensaje="El campo 'stock' es obligatorio para registrar un producto en la tienda."
            )

        return await super().crear(db, obj_in=obj_in)

producto = CRUDProductoTienda(ProductoTienda)