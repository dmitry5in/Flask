from models import Advert
from flask_marshmallow import Marshmallow


mrsh = Marshmallow()


class AdvertSchema(mrsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Advert
    id = mrsh.auto_field(dump_only=True)