from fastapi import APIRouter, Depends
from numpy import double
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_curr_user
from app.services.model_service import make_prediction

router = APIRouter()

class CarFeatures(BaseModel):
    Year: int
    Predent_Price: double
    Kms_Driven: double
    Owner: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    
    
@router.post('/predict')
def predict_price(car: CarFeatures, user = Depends(get_curr_user), _=Depends(get_api_key)):
    prediction = make_prediction(car.model_dump())
    return {'Predicted Price': prediction}
    