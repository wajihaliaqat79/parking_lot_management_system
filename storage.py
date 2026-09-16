class Storage:

    def __init__(self):
        self.spots = {}
        self.tickets = {}
        self.history = {}

    def clear(self):
        self.spots.clear()
        self.tickets.clear()
        self.history.clear()

    def save_spot(self, spot):
        self.spots[spot.spot_id] = spot

    def save_ticket(self, ticket):
        self.tickets[ticket.ticket_id] = ticket

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id)

    def add_visit(self, visit):
        self.history.setdefault(visit.plate, []).append(visit)

    def get_history(self, plate):
        return self.history.get(plate, [])


    