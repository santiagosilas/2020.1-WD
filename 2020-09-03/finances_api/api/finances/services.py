from api import db
from api.finances.models import Record

class RecordService:
    @staticmethod
    def get_all():
        records = Record.query.all()
        return records

    @staticmethod
    def add(*args, **kargs):
        record = Record(*args, **kargs)
        db.session.add(record)
        db.session.commit()
        return record
    