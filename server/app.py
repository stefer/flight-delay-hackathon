from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Load the model
# with open('model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# Load the airports data
airports = pd.read_csv('airports.csv')

# Initialize Flask-RESTX API
api = Api(app, version='1.0', title='Flight Delay Prediction API',
          description='API for predicting flight delays.',
          doc='/swagger/')  # Explicitly set the Swagger UI endpoint

# Define namespaces
ns = api.namespace('api', description='Flight Delay operations')

# Define models for Swagger documentation
predict_model = ns.model('Predict', {
    'day_of_week': fields.String(required=True, description='Day of the week'),
    'airport_id': fields.String(required=True, description='Airport ID')
})

response_model = ns.model('Response', {
    'delay_chance': fields.Float(description='Chance of delay'),
    'confidence': fields.Float(description='Confidence level')
})

# Update predict endpoint
@ns.route('/predict')
class Predict(Resource):
    @ns.expect(predict_model, validate=True)
    @ns.marshal_with(response_model)
    def get(self):
        try:
            # Parse query parameters
            day_of_week = request.args.get('day_of_week')
            airport_id = request.args.get('airport_id')

            if day_of_week is None or airport_id is None:
                ns.abort(400, 'day_of_week and airport_id are required')

            # Prepare input for the model
            input_df = pd.DataFrame([{'day_of_week': day_of_week, 'airport_id': airport_id}])

            # Make prediction
            prediction = model.predict_proba(input_df)
            delay_chance = prediction[0][1]  # Assuming the second column is the delay probability
            confidence = max(prediction[0]) * 100

            # Return prediction as JSON
            return {'delay_chance': delay_chance, 'confidence': confidence}
        except Exception as e:
            ns.abort(400, str(e))

# Update airports endpoint
@ns.route('/airports')
class Airports(Resource):
    def get(self):
        try:
            # Sort airports by name
            sorted_airports = airports.sort_values(by='name')
            result = sorted_airports[['id', 'name']].to_dict(orient='records')

            # Return sorted list as JSON
            return result
        except Exception as e:
            ns.abort(500, str(e))

# Add namespace to the API
api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True)