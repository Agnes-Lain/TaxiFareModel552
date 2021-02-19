# write some code for the API here

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from TaxiFareModel.trainer import Trainer
import pandas as pd
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

# @app.get("/predict_fared")
# def predict(pickup_datetime,
#             pickup_longitude,
#             pickup_latitude,
#             dropoff_longitude,
#             dropoff_latitude,
#             passenger_count):
#     # transfer data to X_test
#     # X = pd.DataFrame({'key':'1',
#     #                    "pickup_datetime": pickup_datetime,
#     #                    "pickup_longitude": float(pickup_longitude),
#     #                    "pickup_latitude": float(pickup_latitude),
#     #                    "dropoff_longitude": float(dropoff_longitude),
#     #                    "dropoff_latitude": float(dropoff_latitude),
#     #                    "passenger_count": int(passenger_count)},
#     #                    index=[0])

#     pickup_datetime = '2013-07-06 17:18:00 UTC'
#     pickup_longitude = 41
#     pickup_latitude = 41
#     dropoff_longitude = 41
#     dropoff_latitude = 41
#     passenger_count = 2

#     X = pd.DataFrame(dict(
#             key=['2013-07-06 17:18:00.000000119'],
#             pickup_datetime=[pickup_datetime],
#             pickup_longitude=[float(pickup_longitude)],
#             pickup_latitude=[float(pickup_latitude)],
#             dropoff_longitude=[float(dropoff_longitude)],
#             dropoff_latitude=[float(dropoff_latitude)],
#             passenger_count=[int(passenger_count)]))
#     # call the model to predict

#     model = joblib.load('model.joblib')
#     fare = model.predict(X)
#     # # return the result
#     return {'predict_fare': fare}

@app.get("/predict_fare")
def predict(pickup_datetime,
            pickup_longitude,
            pickup_latitude,
            dropoff_longitude,
            dropoff_latitude,
            passenger_count):

    # pickup_datetime = '2013-07-06 17:18:00 UTC'
    # pickup_longitude = 41
    # pickup_latitude = 41
    # dropoff_longitude = 41
    # dropoff_latitude = 41
    # passenger_count = 2

    X = pd.DataFrame(dict(
            key=['2013-07-06 17:18:00.000000119'],
            pickup_datetime=[pickup_datetime],
            pickup_longitude=[float(pickup_longitude)],
            pickup_latitude=[float(pickup_latitude)],
            dropoff_longitude=[float(dropoff_longitude)],
            dropoff_latitude=[float(dropoff_latitude)],
            passenger_count=[int(passenger_count)]))

    model = joblib.load('model.joblib')

    fare = model.predict(X)

    print(type(fare))

    return {'predict_fare': fare[0]}
