from datetime import datetime, timedelta
import requests

def get_validators_by_operator(operator_id):
    url = f"https://api.ssv.network/api/v4/mainnet/validators/in_operator/{operator_id}"
    response = requests.get(url)
    if response.status_code == 200:
        validators = response.json().get('validators', [])
        return validators
    else:
        print("Failed to fetch validators from SSV Network")
        return []

def get_validator_performance(validator_pub_key, api_key):
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    start_timestamp = int(start_time.timestamp())
    end_timestamp = int(end_time.timestamp())
    url = f"https://api.rated.network/v0/eth/validators/{validator_pub_key}/effectiveness?from={start_timestamp}&to={end_timestamp}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    operator_id = 2  # Replace this with the operator ID you want to explore
    api_key = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOltdLCJpZCI6IjI1NGZlODZiYTU4NTRiN2E5N2YyNTI5YTE4Y2FjNDQ5Iiwic3ViIjoiMGUzYjdkMjliZjI4NDUxYTllZTcwNzJiNTkxMWViMjgiLCJleHAiOjE3NDAwODQ4NzV9.hCAfFUaro0Lm8KycMepc_1TREatEMPTbYGY5OYdxAMPWLZaAOqLPT-HvmmwA-mVvi8vxap1pZhF1B5EJGS36BQ'  
    validators = get_validators_by_operator(operator_id)
    if validators:
        for validator in validators:
            pub_key = validator.get('public_key')
            if pub_key:
                performance = get_validator_performance(pub_key, api_key)
                if performance and 'data' in performance and len(performance['data']) > 0:
                    # Accessing the first item in the 'data' array
                    effectiveness = performance['data'][0].get('validatorEffectiveness')
                    avgCorrectness = performance['data'][0].get('avgCorrectness')
                    print(f"Validator {pub_key}: ")
                    print(f"Effectiveness = {effectiveness}")
                    print(f"Average Correctness = {avgCorrectness}")
                else:
                    print(f"Validator {pub_key}: Performance data not available")

if __name__ == "__main__":
    main()

