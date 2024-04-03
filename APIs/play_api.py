from flask import Blueprint, jsonify, request
from utils import api_util, logger_util

play_api = Blueprint('play_api', __name__)
PLAYS_FILENAME = 'plays'

logger = logger_util.setup_logger('play_logger', 'logs/play.log')


@play_api.route('/plays', methods=['GET'])
def get_plays():
    data = api_util.load_data_from_json_file_by_name(PLAYS_FILENAME)
    logger.info('Get plays')
    return jsonify({'plays': data['plays']})


@play_api.route('/plays', methods=['POST'])
def add_play():
    data = api_util.load_data_from_json_file_by_name(PLAYS_FILENAME)
    new_play_data = request.json
    new_play_id = api_util.get_next_id(data, 'plays')
    new_play_data['id'] = new_play_id
    data['plays'].append(new_play_data)
    api_util.save_data_in_file_by_filename(data, PLAYS_FILENAME)
    logger.info(f'Added new play with ID {new_play_id}')
    return jsonify({'message': 'Play added successfully'}), 201


@play_api.route('/plays/<int:play_id>', methods=['GET'])
def get_play(play_id):
    data = api_util.load_data_from_json_file_by_name(PLAYS_FILENAME)
    play = next((play for play in data['plays'] if play['id'] == play_id), None)
    if play:
        logger.info(f'Get play with ID {play_id}')
        return jsonify(play)
    else:
        logger.error(f'Play with ID {play_id} not found')
        return jsonify({'message': 'Play not found'}), 404


@play_api.route('/plays/<int:play_id>', methods=['PUT'])
def update_play(play_id):
    data = api_util.load_data_from_json_file_by_name(PLAYS_FILENAME)
    play_data = request.json
    for play in data['plays']:
        if play['id'] == play_id:
            play.update(play_data)
            api_util.save_data_in_file_by_filename(data, PLAYS_FILENAME)
            logger.info(f'Updated play with ID {play_id}')
            return jsonify({'message': 'Play updated successfully'}), 200
    logger.error(f'Play with ID {play_id} not found')
    return jsonify({'message': 'Play not found'}), 404


@play_api.route('/plays/<int:play_id>', methods=['DELETE'])
def delete_play(play_id):
    data = api_util.load_data_from_json_file_by_name(PLAYS_FILENAME)
    plays = data['plays']
    filtered_plays = [play for play in plays if play['id'] == play_id]
    if not filtered_plays:
        logger.error(f'Play with ID {play_id} not found')
        return jsonify({'message': 'Play not found'}), 404
    data['plays'] = [play for play in plays if play['id'] != play_id]

    for i, play in enumerate(data['plays'], start=1):
        play['id'] = i

    api_util.save_data_in_file_by_filename(data, PLAYS_FILENAME)
    logger.info(f'Deleted play with ID {play_id}')
    return jsonify({'message': 'Play deleted successfully'}), 200
