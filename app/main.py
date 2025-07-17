from fastapi import FastAPI
from app.api import products

app = FastAPI(title="SmartBiz AI - Inventory System")
# Include the products router
app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
  return {"message": "Welcome to SmartBiz AI - Inventory Management System"}
