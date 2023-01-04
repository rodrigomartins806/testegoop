import requests
from flask import Flask
import os

def consulta():
    
    url = "https://goop.callbox.com.br/webservice/index_get.php"

    querystring = {"pKey":"5cd2b49345321019804eac5b4501aa72"," Retorno":"1","calldate":"2023-01-03","calldate[start]":"2023-01-03 00:00:00","calldate[end]":"2023-01-03 23:59:00"," comando":"verificaCDR"}
    payload = ""
    headers = {"cookie": "CBXSESSIDWEB=cnc9skp5o4int4u22vnnoa0vv7"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring, timeout=None)

    return response.text


    
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello():

    return consulta(),200

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, 
                log_level='info', reload=True)