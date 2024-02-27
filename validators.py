
import requests

def get_validators_by_operator(operator_id):
    url = f"https://api.ssv.network/api/v4/mainnet/validators/in_operator/{operator_id}"
    response = requests.get(url)
    validators = response.json()['validators']
    if response.status_code == 200:
        return validators
    else:
        print("Failed to fetch validators from SSV Network")
        return []
def get_validator_performance(validator_pub_key, api_key):
    url = f"https://api.rated.network/api/v0/eth/validators/{validator_pub_key}/effectiveness"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch performance for validator {validator_pub_key}")
        return None

def main():
    operator_id = 2  # Replace this with the operator ID you want to explore
    api_key = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOltdLCJpZCI6IjI1NGZlODZiYTU4NTRiN2E5N2YyNTI5YTE4Y2FjNDQ5Iiwic3ViIjoiMGUzYjdkMjliZjI4NDUxYTllZTcwNzJiNTkxMWViMjgiLCJleHAiOjE3NDAwODQ4NzV9.hCAfFUaro0Lm8KycMepc_1TREatEMPTbYGY5OYdxAMPWLZaAOqLPT-HvmmwA-mVvi8vxap1pZhF1B5EJGS36BQ'
    validators = get_validators_by_operator(operator_id)
    if validators:
        for validator in validators:
            pub_key = validator['public_key']
            performance = get_validator_performance(pub_key, api_key)
            if performance:
                print(f"Validator {pub_key}: Performance over 24h: {performance}")
            else:
                print(f"Validator {pub_key}: Performance data not available")

if __name__ == "__main__":
    main()
