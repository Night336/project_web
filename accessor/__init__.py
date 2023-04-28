from accessor.categorie import CategoryAccessor
from accessor.brand import BrandAccessor
from accessor.user import UserAccessor
from accessor.product import ProductAccessor
from accessor.orders import OrdersAccessor
from accessor.revews import ReviewAccessor


class Accessor(CategoryAccessor, BrandAccessor, UserAccessor, ProductAccessor, OrdersAccessor, ReviewAccessor):
    pass
