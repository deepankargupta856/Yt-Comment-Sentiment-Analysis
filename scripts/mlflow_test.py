import mlflow
import random

mlflow.set_tracking_uri("http://ec2-13-53-74-103.eu-north-1.compute.amazonaws.com:5000/")

with mlflow.start_run():
    
    mlflow.log_param("param1",random.randint(1,5000))