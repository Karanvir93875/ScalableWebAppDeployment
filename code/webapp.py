from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Update the PostgreSQL connection details below
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/database'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@app.route('/items', methods=['POST'])
def add_item():
    item_data = request.json
    item = Item(name=item_data['name'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
