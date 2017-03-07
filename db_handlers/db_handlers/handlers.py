from db_handlers.models import Client, Visits


class VisitsHandler:

    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, client_id, gender):
        new_visit = Visits(client_id=client_id, gender=gender)
        self.db_session.add(new_visit)

    def delete(self, identifier):
        pass

    def update(self, identifier, **kwargs):
        pass

    def get_all(self):
        results = self.db_session.query(Visits).all()
        return [x._to_dict() for x in results if x is not None]

    def get(self, identifier):
        visit = self.db_session.query(Visits).get(identifier)
        if not visit:
            return None
        else:
            return visit._to_dict()


class ClientHandler:

    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, client_id):
        new_client = Client(id=client_id)
        self.db_session.add(new_client)

    def delete(self, identifier):
        pass

    def update(self, identifier, **kwargs):
        pass

    def get_all(self):
        results = self.db_session.query(Client).all()
        return [x._to_dict() for x in results if x is not None]

    def get(self, identifier):
        client = self.db_session.query(Client).get(identifier)
        if not client:
            return None
        else:
            return client._to_dict()
