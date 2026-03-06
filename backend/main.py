from fastapi import FastAPI
import os 
import mysql.connector
app = FastAPI()

@app.get("/")
def home():
    return {"message": "pwdwizard backend is runningggggg test test test"} 

@app.get("/test-db")
def database_test():

    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="pwdwizard"
    )

    return {"database": "works"}