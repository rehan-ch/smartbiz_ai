from fastapi import FastAPI

app = FastAPI(title="SmartBiz AI - Inventory System")

@app.get("/")
def root():
    return {"message": "Welcome to SmartBiz AI - Inventory Management System"}
