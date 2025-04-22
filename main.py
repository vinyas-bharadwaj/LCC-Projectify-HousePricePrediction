from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

class PricePrediction(BaseModel):
    area: float
    bedrooms: int
    age: int


@app.post("/predict")
def predict(data: PricePrediction):
    # Load the model from the pickle file
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    
    # Prepare the input data for prediction
    input_data = [[data.area, data.bedrooms, data.age]]

    # Make the prediction
    prediction = model.predict(input_data)

    # Return the prediction result
    return {"predicted_price": prediction[0]}