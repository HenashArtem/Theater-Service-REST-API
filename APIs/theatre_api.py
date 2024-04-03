from flask import Blueprint, jsonify, request
from utils import api_util, logger_util

theatre_api = Blueprint('theatre_api', __name__)
THEATRES_FILENAME = 'theatres'

logger = logger_util.setup_logger('theatre_logger', 'logs/theatre.log')


@theatre_api.route('/theatres', methods=['GET'])
def get_theatres():
    data = api_util.load_data_from_json_file_by_name(THEATRES_FILENAME)
    logger.info('Get theatres')
    return jsonify({'theatres': data['theatres']})


@theatre_api.route('/theatres', methods=['POST'])
def add_theatre():
    data = api_util.load_data_from_json_file_by_name(THEATRES_FILENAME)
    new_theatre_data = request.json
    new_theatre_id = api_util.get_next_id(data, 'theatres')
    new_theatre_data['id'] = new_theatre_id
    data['theatres'].append(new_theatre_data)
    api_util.save_data_in_file_by_filename(data, THEATRES_FILENAME)
    logger.info(f'Added new theatre with ID {new_theatre_id}')
    return jsonify({'message': 'Theatre added successfully'}), 201


@theatre_api.route('/theatres/<int:theatre_id>', methods=['GET'])
def get_theatre(theatre_id):
    data = api_util.load_data_from_json_file_by_name(THEATRES_FILENAME)
    theatre = next((theatre for theatre in data['theatres'] if theatre['id'] == theatre_id), None)
    if theatre:
        logger.info(f'Get theatre with ID {theatre_id}')
        return jsonify(theatre)
    else:
        logger.error(f'Theatre with ID {theatre_id} not found')
        return jsonify({'message': 'Theatre not found'}), 404


@theatre_api.route('/theatres/<int:theatre_id>', methods=['PUT'])
def update_theatre(theatre_id):
    data = api_util.load_data_from_json_file_by_name(THEATRES_FILENAME)
    theatre_data = request.json
    for theatre in data['theatres']:
        if theatre['id'] == theatre_id:
            theatre.update(theatre_data)
            api_util.save_data_in_file_by_filename(data, THEATRES_FILENAME)
            logger.info(f'Updated theatre with ID {theatre_id}')
            return jsonify({'message': 'Theatre updated successfully'}), 200
    logger.error(f'Theatre with ID {theatre_id} not found')
    return jsonify({'message': 'Theatre not found'}), 404


@theatre_api.route('/theatres/<int:theatre_id>', methods=['DELETE'])
def delete_theatre(theatre_id):
    data = api_util.load_data_from_json_file_by_name(THEATRES_FILENAME)
    theatres = data['theatres']
    filtered_theatres = [theatre for theatre in theatres if theatre['id'] == theatre_id]
    if not filtered_theatres:
        logger.error(f'Theatre with ID {theatre_id} not found')
        return jsonify({'message': 'Theatre not found'}), 404
    data['theatres'] = [theatre for theatre in theatres if theatre['id'] != theatre_id]

    for i, theatre in enumerate(data['theatres'], start=1):
        theatre['id'] = i

    api_util.save_data_in_file_by_filename(data, THEATRES_FILENAME)
    logger.info(f'Deleted theatre with ID {theatre_id}')
    return jsonify({'message': 'Theatre deleted successfully'}), 200
