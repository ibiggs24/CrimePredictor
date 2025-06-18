import requests
import pandas as pd

all_data = []
base_url = "https://api.census.gov/data/2020/dec/pl"
key = os.getenv("CENSUS_API_KEY")

counties = ["031"] 

for county in counties:
    params = {
        "get": "P1_001N,GEO_ID",
        "for": "block group:*",
        "in": f"state:17 county:{county}",
        "key": "ed4e30a96252d67ba2556be9732ce1d2f78cdd7f"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        all_data.append(df)
        print(f"Fetched data for county {county}")
    else:
        print(f"Failed for county {county} with status {response.status_code}")

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv("blockgroup_population_2020.csv", index=False)
    print("All data saved to blockgroup_population_2020.csv")
else:
    print("No data fetched.")
