# Assignment 3: CSO API
# As per instructions , as short as possible, download the dataset from the CSO API and save it to a file called cso.json.
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
out_file = "cso.json"
import requests
import json
with open(out_file, "w") as f:
    json.dump(requests.get(url).json(), f, indent=4)