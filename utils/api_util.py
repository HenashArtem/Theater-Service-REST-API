import json
from utils.models import Theatre, Play, Performance, User


def load_data_from_json_file_by_name(filename):
    with open(f'data/{filename}.json', 'r') as file:
        return json.load(file)


def save_data_in_file_by_filename(data, filename):
    with open(f'data/{filename}.json', 'w') as file:
        json.dump(data, file)


def get_next_id(data, entity_type):
    entities = data.get(entity_type, [])
    if entities:
        return max(entity['id'] for entity in entities) + 1
    else:
        return 1


def create_theatre_from_dict(theatre_dict):
    return Theatre(
        theatre_dict['id'],
        theatre_dict['name'],
        theatre_dict['location'],
        theatre_dict['capacity'],
        theatre_dict['rating']
    )


def create_play_from_dict(play_dict):
    return Play(
        play_dict['id'],
        play_dict['title'],
        play_dict['author'],
        play_dict['genre'],
        play_dict['duration']
    )


def create_performance_from_dict(performance_dict):
    return Performance(
        performance_dict['id'],
        performance_dict['theatre_id'],
        performance_dict['play_id'],
        performance_dict['date'],
        performance_dict['time'],
        performance_dict['tickets_sold'],
        performance_dict['ticket_price']
    )


def create_user_from_dict(user_dict):
    return User(
        user_dict['id'],
        user_dict['name'],
        user_dict['email'],
        user_dict['phone'],
        user_dict['address']
    )
