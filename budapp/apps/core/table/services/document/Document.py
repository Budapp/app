class Document(object):
    def __init__(self, table, fields_data):
        self.table = table
        self.fields_data = fields_data

    def register(self):
        print("Registering...")
