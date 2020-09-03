from api.clients.models import Client
from api import ma

class ClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email')