import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cached_prediction, set_cached_prediction


model = joblib.load(settings.MODEL_PATH)


def make_prediction(data: dict):
    cached_key = " ".join([str(val) for val in data])
    cached_data = get_cached_prediction(cached_key)
    
    if cached_data:
        return cached_data
    
    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]
    set_cached_prediction(cached_key, prediction)
    return prediction