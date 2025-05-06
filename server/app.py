from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
# with open('model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# Load the airports data
airports = pd.read_csv('airports.csv')

# Change the predict endpoint to use GET with query parameters
@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Parse query parameters
        day_of_week = request.args.get('day_of_week')
        airport_id = request.args.get('airport_id')

        if day_of_week is None or airport_id is None:
            return jsonify({'error': 'day_of_week and airport_id are required'}), 400

        # Prepare input for the model
        input_df = pd.DataFrame([{'day_of_week': day_of_week, 'airport_id': airport_id}])

        # Make prediction
        prediction = model.predict_proba(input_df)
        delay_chance = prediction[0][1]  # Assuming the second column is the delay probability
        confidence = max(prediction[0]) * 100

        # Return prediction as JSON
        return jsonify({'delay_chance': delay_chance, 'confidence': confidence})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/airports', methods=['GET'])
def get_airports():
    try:
        # Sort airports by name
        sorted_airports = airports.sort_values(by='name')
        result = sorted_airports[['id', 'name']].to_dict(orient='records')

        # Return sorted list as JSON
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)