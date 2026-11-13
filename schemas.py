from pydantic import BaseModel, Field

class VehicleContract(BaseModel):
    seller_name: str = Field(description="ФИО продавца")
    vehicle_year: int = Field(description="Год выпуска")
    price: float | None = Field(default=None, description="Цена в рублях, если указана")
    sign_date: str | None = Field(default=None, description="Дата подписания, если указана")