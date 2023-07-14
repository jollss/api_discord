import subprocess
import requests
import json
import os
from decouple import config
entorno=config('entorno_ci_cd')
lineas = subprocess.check_output(['git', 'log', '-1', '--no-merges'], stderr=subprocess.STDOUT).decode("utf-8").split("\n")
try:
  autor=lineas[1]
  fecha=lineas[2]
  descripcion=lineas[4]
except:
  autor="test"
  fecha="test"
  descripcion="test"
mensaje="Entorno: {0} \n {3} \n {1} \n Descripcion:{2}".format(entorno,fecha,descripcion,autor)
url=""
name_server=config('name_server')
headers = {  'Content-Type': 'application/json'}
payload = json.dumps({
  "username": name_server,
  "avatar_url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/017.png",
  "content": "CI/CD",
  "tts": False,
  "embeds": [
    {
      "id": 645327724,
      "description": mensaje,
      "fields": []
    }
  ],
  "components": [],
  "actions": {}
})
resp = requests.post(url, headers=headers, data=payload)