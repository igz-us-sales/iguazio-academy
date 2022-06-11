
from typing import Any, Dict, List, Union
import mlrun
from mlrun.serving.v2_serving import V2ModelServer
from datetime import datetime
import psutil
import numpy as np
import json

class DummyModelServer(mlrun.serving.V2ModelServer):
    def load(self):
        """load and initialize the model and/or other elements"""

    def predict(self, body: dict) -> List:
        """Generate model predictions from sample."""
        print("+++++++++++++++++++ in Dummy Model Prediction ++++++++++++++++++++++")
        feats = np.asarray(body['inputs'])
        print(f'feats shape === >>> {feats.shape}')
        print("+++++++++++++++++++ out Dummy Model Prediction ++++++++++++++++++++++")
        print()
        return feats.shape

def postprocess(event):
    print("+++++++++++++++++++ in Dummy Postprocess ++++++++++++++++++++++")
    print(f'Event keys === >>> {event.keys()}')
    print("+++++++++++++++++++ out Dummy Postprocess ++++++++++++++++++++++")
    print()
    return event

def preprocess(event):
    print("+++++++++++++++++++ in Dummy Preprocess ++++++++++++++++++++++")
    print(f'Event keys === >>> {event.keys()}')
    print("+++++++++++++++++++ out Dummy Preprocess ++++++++++++++++++++++")
    print()
    return event
