from litestar import Litestar
from app.controlers import AuthorController, BookController,ClientController
from app.database import sqlalchemy_config

app = Litestar([AuthorController, BookController,ClientController], debug=True, plugins=[sqlalchemy_config])
