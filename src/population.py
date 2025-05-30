import requests

def estimate_population(lat, lon):
    try:
        fcc_url = f"https://geo.fcc.gov/api/census/block/find?latitude={lat}&longitude={lon}&format=json"
        fcc_response = requests.get(fcc_url)
        fcc_data = fcc_response.json()

        state_fips = fcc_data['County']['FIPS'][:2]
        county_fips = fcc_data['County']['FIPS'][2:]
        tract_code = fcc_data['Block']['FIPS'][5:11]

        census_url = (
            f"https://api.census.gov/data/2020/dec/pl"
            f"?get=P1_001N&for=tract:{tract_code}&in=state:{state_fips}+county:{county_fips}"
        )
        response = requests.get(census_url)
        data = response.json()

        population = int(data[1][0])
        return population

    except Exception as e:
        print(f"[!] Population lookup failed: {e}")
        return None
