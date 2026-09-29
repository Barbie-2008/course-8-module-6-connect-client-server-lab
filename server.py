from flask import Flask, jsonify, request
from flask_cors import CORS
from data import events

app = Flask(__name__)
CORS(app)


# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [{"id": 1, "title": "Hiking in Mount Kenya"},
          {"id": 2, "title": "Yoga in the park"}
          ]
# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Event Catalog API!"})

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events), 200
# TASK: Create a POST route for "/events"
@app.route('/events', methods=['POST'])
def create_events():
    # This route should:
    # 1. Get the JSON data from the request
    data = request.get_json()
    # 2. Validate that "title" is provided
    if not data or not isinstance(data.get('title'), str) or not data['title'].strip():
        return jsonify({"error": "Bad Request: 'title' is required"}), 400
    # 3. Create a new event with a unique ID and the provided title
    new_id = max([e['id'] for e in events], default=0) + 1
    new_event = {
        "id": new_id,
        "title": data['title']
    }
    # 4. Add the new event to the events list
    events.append(new_event)
    # 5. Return the new event with status code 201
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
