from pydantic import BaseModel

class UpdateData(BaseModel):
    auth: str
    state_management: str
    market_place: str
    questionnaire: str
    persional: str
    bookings: str
    casesapp: str
    