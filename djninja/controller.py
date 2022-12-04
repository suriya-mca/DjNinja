# import ninja-api package
from ninja import NinjaAPI
# import router instance from api
from .api import router as main_router

# ninja instance
api = NinjaAPI()

api.add_router("/", main_router)