from flask import Flask, jsonify, request

app = Flask(__name__)

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        contact = Contact(name, phone_number)
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.phone_number
        return "Kontak tidak ditemukan"

address_book = AddressBook()

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name')
    phone_number = data.get('phone_number')
    address_book.add_contact(name, phone_number)
    return jsonify({'message': 'Kontak berhasil ditambahkan'})

@app.route('/contacts/<name>', methods=['DELETE'])
def remove_contact(name):
    address_book.remove_contact(name)
    return jsonify({'message': 'Kontak berhasil dihapus'})

@app.route('/contacts/<name>', methods=['GET'])
def search_contact(name):
    phone_number = address_book.search_contact(name)
    return jsonify({'phone_number': phone_number})

if __name__ == '__main__':
    app.run(debug=False)
