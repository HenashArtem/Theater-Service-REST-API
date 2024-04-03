class Theatre:
    def __init__(self, theatre_id, name, location, capacity, rating):
        self.theatre_id = theatre_id
        self.name = name
        self.location = location
        self.capacity = capacity
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.theatre_id,
            "name": self.name,
            "location": self.location,
            "capacity": self.capacity,
            "rating": self.rating
        }


class Play:
    def __init__(self, play_id, title, author, genre, duration):
        self.play_id = play_id
        self.title = title
        self.author = author
        self.genre = genre
        self.duration = duration

    def to_dict(self):
        return {
            "id": self.play_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "duration": self.duration
        }


class Performance:
    def __init__(self, performance_id, theatre_id, play_id, date, time, tickets_sold, ticket_price):
        self.performance_id = performance_id
        self.theatre_id = theatre_id
        self.play_id = play_id
        self.date = date
        self.time = time
        self.tickets_sold = tickets_sold
        self.ticket_price = ticket_price

    def to_dict(self):
        return {
            "id": self.performance_id,
            "theatre_id": self.theatre_id,
            "play_id": self.play_id,
            "date": self.date,
            "time": self.time,
            "tickets_sold": self.tickets_sold,
            "ticket_price": self.ticket_price
        }


class User:
    def __init__(self, user_id, name, email, phone, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }
