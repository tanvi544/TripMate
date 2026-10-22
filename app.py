
from flask import Flask, render_template, request

app = Flask(__name__)

trips = {
    "Jaipur": ["Hawa Mahal", "Amber Fort", "City Palace",
               "Jantar Mantar", "Jal Mahal"],
    "Agra": ["Taj Mahal", "Agra Fort", "Mehtab Bagh",
             "Fatehpur Sikri", "Sadar Bazaar"],
    "Manali": ["Solang Valley", "Hadimba Temple",
               "Old Manali", "Atal Tunnel", "Mall Road"],
    "Delhi": ["India Gate", "Red Fort", "Qutub Minar",
              "Lotus Temple", "Akshardham Temple"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plan", methods=["POST"])
def plan():
    destination = request.form["destination"]
    days = int(request.form["days"])
    interest = request.form["interest"]

    places = trips.get(destination, [
        f"Popular places in {destination}",
        f"Local sightseeing in {destination}",
        "Local market",
        "Famous tourist attraction"
    ])

    itinerary = []
    for day in range(days):
        place = places[day % len(places)]
        itinerary.append({
            "day": day + 1,
            "place": place,
            "interest": interest
        })

    budget = days * 2000

    return render_template(
        "result.html",
        destination=destination,
        itinerary=itinerary,
        budget=budget,
        days=days
    )

if __name__ == "__main__":
    app.run(debug=True)