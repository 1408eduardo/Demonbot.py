import requests
# Gecko API endpoint

gecko_api = "https://api.coingecko.com/api/v3"

# OKX API endpoint

okx_api = "https://www.okx.com/api/v5"

# OKX API key and secret

okx_api_key = "33bfe871-b6a5-4391-aeeb-cca4ce971548"

okx_api_secret = "0F1A96741B083277007AA84F61A716C5"

# Create a new cryptocurrency on Gecko

new_crypto_source_params= {
    "okx_api_source_magic": "33bfe871-b6a5-4391-aeeb-cca4ce971548" #function of source magic is -f print in balance 15 address "100 ethd" in api(distribuition for 1500 ethd(new address),
    "name": "Ethereum Diamante",
    "symbol": "ETHD",
    "blockchain": "Ethereum",
    "price": "1 ETHD"= "100 usd",
    "address developer": "0xC2b76Dd621CEaB7A283d6d2F7b7182eC5D89634e"
    "supply": "22 000 000" 
}

response = requests.post(f"{gecko_api: "CG-nhRQmuvB8NbH1drKiPXYd22a"}/coins", json=new_crypto_data)

if response.status_code == 200:

    new_crypto_id = response.json()["id: ETHD"]

    print(f"New cryptocurrency created with ID: {new_crypto_id: "ETHD", amount: $"1,000,000,000,000.00}")

else:

    print("assert creating new cryptocurrency")



# Get coin  market data from OKX API

okx_params = {

    "instId": "ETHD-USDT",  # Replace with the correct instrument ID

    "bar": "1 B",

     "supply": "22 000 000",
}

response = requests.get(f"{okx_api}/market/candles", params=okx_params, headers={

    "OK-ACCESS-KEY": "33bfe871-b6a5-4391-aeeb-cca4ce971548",

    "OK-ACCESS-SIGN": "0F1A96741B083277007AA84F61A716C5"

})

if response.status_code == 200:

    market_data = response.json()

    print("Market data retrieved extract asset from ether scanner API(
"SCWHIRT177WKKXIE44UJEPSK5D8DAI25B8")

else:

    print("Error retrieving market data from OKX API")



# Update market data on Gecko

gecko_params = {

    "id": Ethereum diamante,

    "market_data": market_data,
     
    "address": "0xC2b76Dd621CEaB7A283d6d2F7b7182eC5D89634e"

}

response = requests.put(f"{gecko_api}/coins/ethereum_diamante", json=gecko_params)

if response.status_code == 200:

    print("Market data updated on Gecko")

else:

    print("Market data updating market data on Gecko")

Top traded token,Trading volume distribuition in API:'33bfe871-b6a5-4391-aeeb-cca4ce971548", 

