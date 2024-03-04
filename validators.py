from datetime import datetime, timedelta
import requests
import argparse

def get_validators_by_operator(operator_id, network):
    url = f"https://api.ssv.network/api/v4/{network}/validators/in_operator/{operator_id}"
    response = requests.get(url)
    if response.status_code == 200:
        validators = response.json().get('validators')
        return validators
    else:
        print("Failed to fetch validators from SSV Network")
        return []

def get_validator_performance(validator_pub_key, api_key, network):
    # Getting the timestamps for the 24h period in question
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    start_timestamp = int(start_time.timestamp())
    end_timestamp = int(end_time.timestamp())
    url = f"https://api.rated.network/v0/eth/validators/{validator_pub_key}/effectiveness?from={start_timestamp}&to={end_timestamp}"
    headers = {'Authorization': f'Bearer {api_key}', 'X-Rated-Network': f"{network}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    parser=argparse.ArgumentParser(description="sample argument parser")
    parser.add_argument("network")
    parser.add_argument("operator_id")
    args=parser.parse_args()
    network = ""
    operator_id = 0
    if args.network != "mainnet" and args.network != "holesky":
        print (f"Wrong network argument value provided: {args.network}")
        return
    else:
        network = args.network
    
    if not args.operator_id:
        print ("Operator id not provided")
        return
    else:
        try:
            operator_id = int(args.operator_id)
        except ValueError:
            print("Operator Id provided is not a number")
    api_key = '<YOUR_KEY>'
    validators = get_validators_by_operator(operator_id, network)
    if validators:
        for validator in validators:
            pub_key = validator.get('public_key')
            if pub_key:
                performance = get_validator_performance(pub_key, api_key, network)
                if performance and 'data' in performance and len(performance['data']) > 0:
                    # Accessing validator performance data from the 'data' array
                    effectiveness = performance['data'][0].get('validatorEffectiveness')
                    avgCorrectness = performance['data'][0].get('avgCorrectness')
                    print(f"Validator {pub_key}: ")
                    print(f"Effectiveness = {effectiveness}")
                    print(f"Average Correctness = {avgCorrectness}")
                else:
                    print(f"Validator {pub_key}: Performance data not available")

if __name__ == "__main__":
    main()

