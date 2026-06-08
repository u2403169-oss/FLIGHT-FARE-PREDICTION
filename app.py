from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("flight_fare_model.pkl")


from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    # Numerical Features
    Total_Stops = int(data["Total_Stops"])
    Journey_day = int(data["Journey_day"])
    Journey_month = int(data["Journey_month"])
    Dep_hour = int(data["Dep_hour"])
    Dep_min = int(data["Dep_min"])
    Arrival_hour = int(data["Arrival_hour"])
    Arrival_min = int(data["Arrival_min"])
    Duration_hours = int(data["Duration_hours"])
    Duration_mins = int(data["Duration_mins"])

    # One-hot vectors
    Airline_Air_India = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_Jet_Airways = 0
    Airline_Jet_Airways_Business = 0
    Airline_Multiple_carriers = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_Vistara_Premium_economy = 0

    airline = data["Airline"]

    if airline == "Air India":
        Airline_Air_India = 1
    elif airline == "GoAir":
        Airline_GoAir = 1
    elif airline == "IndiGo":
        Airline_IndiGo = 1
    elif airline == "Jet Airways":
        Airline_Jet_Airways = 1
    elif airline == "Jet Airways Business":
        Airline_Jet_Airways_Business = 1
    elif airline == "Multiple carriers":
        Airline_Multiple_carriers = 1
    elif airline == "Multiple carriers Premium economy":
        Airline_Multiple_carriers_Premium_economy = 1
    elif airline == "SpiceJet":
        Airline_SpiceJet = 1
    elif airline == "Trujet":
        Airline_Trujet = 1
    elif airline == "Vistara":
        Airline_Vistara = 1
    elif airline == "Vistara Premium economy":
        Airline_Vistara_Premium_economy = 1

    # Source
    Source_Chennai = 0
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 0

    source = data["Source"]

    if source == "Chennai":
        Source_Chennai = 1
    elif source == "Delhi":
        Source_Delhi = 1
    elif source == "Kolkata":
        Source_Kolkata = 1
    elif source == "Mumbai":
        Source_Mumbai = 1

    # Destination
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0
    Destination_New_Delhi = 0

    destination = data["Destination"]

    if destination == "Cochin":
        Destination_Cochin = 1
    elif destination == "Delhi":
        Destination_Delhi = 1
    elif destination == "Hyderabad":
        Destination_Hyderabad = 1
    elif destination == "Kolkata":
        Destination_Kolkata = 1
    elif destination == "New Delhi":
        Destination_New_Delhi = 1

    features = np.array([[
        Total_Stops,
        Journey_day,
        Journey_month,
        Dep_hour,
        Dep_min,
        Arrival_hour,
        Arrival_min,
        Duration_hours,
        Duration_mins,

        Airline_Air_India,
        Airline_GoAir,
        Airline_IndiGo,
        Airline_Jet_Airways,
        Airline_Jet_Airways_Business,
        Airline_Multiple_carriers,
        Airline_Multiple_carriers_Premium_economy,
        Airline_SpiceJet,
        Airline_Trujet,
        Airline_Vistara,
        Airline_Vistara_Premium_economy,

        Source_Chennai,
        Source_Delhi,
        Source_Kolkata,
        Source_Mumbai,

        Destination_Cochin,
        Destination_Delhi,
        Destination_Hyderabad,
        Destination_Kolkata,
        Destination_New_Delhi
    ]])

    prediction = model.predict(features)

    return jsonify({
        "predicted_fare": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)