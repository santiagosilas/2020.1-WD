from flask import Flask, jsonify, request, abort 
from api.finances.models import Record, RecordSchema
from api import db, ma

from . import finances_blueprint as blueprint


@blueprint.errorhandler(404)
def not_found(error):
    print('error', error)
    return jsonify({'error': 'Not found'}), 404


@blueprint.route('/api/finances/test')
def test():
    return 'to do.'


@blueprint.route('/api/finances/records', methods=['GET'])
def get_records():
    records = Record.query.all()
    records_schema = RecordSchema(many=True)
    return records_schema.jsonify(records)