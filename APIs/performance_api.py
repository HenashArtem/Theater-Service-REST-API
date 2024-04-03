from flask import Blueprint, jsonify, request
from utils import api_util, logger_util

performance_api = Blueprint('performance_api', __name__)
PERFORMANCES_FILENAME = 'performances'

logger = logger_util.setup_logger('performance_logger', 'logs/performance.log')


@performance_api.route('/performances', methods=['GET'])
def get_performances():
    data = api_util.load_data_from_json_file_by_name(PERFORMANCES_FILENAME)
    logger.info('Get performances')
    return jsonify({'performances': data['performances']})


@performance_api.route('/performances', methods=['POST'])
def add_performance():
    data = api_util.load_data_from_json_file_by_name(PERFORMANCES_FILENAME)
    new_performance_data = request.json
    new_performance_id = api_util.get_next_id(data, 'performances')
    new_performance_data['id'] = new_performance_id
    data['performances'].append(new_performance_data)
    api_util.save_data_in_file_by_filename(data, PERFORMANCES_FILENAME)
    logger.info(f'Added new performance with ID {new_performance_id}')
    return jsonify({'message': 'Performance added successfully'}), 201


@performance_api.route('/performances/<int:performance_id>', methods=['GET'])
def get_performance(performance_id):
    data = api_util.load_data_from_json_file_by_name(PERFORMANCES_FILENAME)
    performance = next((performance for performance in data['performances'] if performance['id'] == performance_id), None)
    if performance:
        logger.info(f'Get performance with ID {performance_id}')
        return jsonify(performance)
    else:
        logger.error(f'Performance with ID {performance_id} not found')
        return jsonify({'message': 'Performance not found'}), 404


@performance_api.route('/performances/<int:performance_id>', methods=['PUT'])
def update_performance(performance_id):
    data = api_util.load_data_from_json_file_by_name(PERFORMANCES_FILENAME)
    performance_data = request.json
    for performance in data['performances']:
        if performance['id'] == performance_id:
            performance.update(performance_data)
            api_util.save_data_in_file_by_filename(data, PERFORMANCES_FILENAME)
            logger.info(f'Updated performance with ID {performance_id}')
            return jsonify({'message': 'Performance updated successfully'}), 200
    logger.error(f'Performance with ID {performance_id} not found')
    return jsonify({'message': 'Performance not found'}), 404


@performance_api.route('/performances/<int:performance_id>', methods=['DELETE'])
def delete_performance(performance_id):
    data = api_util.load_data_from_json_file_by_name(PERFORMANCES_FILENAME)
    performances = data['performances']
    filtered_performances = [performance for performance in performances if performance['id'] == performance_id]
    if not filtered_performances:
        logger.error(f'Performance with ID {performance_id} not found')
        return jsonify({'message': 'Performance not found'}), 404
    data['performances'] = [performance for performance in performances if performance['id'] != performance_id]

    for i, performance in enumerate(data['performances'], start=1):
        performance['id'] = i

    api_util.save_data_in_file_by_filename(data, PERFORMANCES_FILENAME)
    logger.info(f'Deleted performance with ID {performance_id}')
    return jsonify({'message': 'Performance deleted successfully'}), 200
