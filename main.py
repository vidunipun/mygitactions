import os
import yaml

# Load the config.yaml file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load the azurekey.yaml file
with open("azurekey.yaml", "r") as f:
    azurekey = yaml.safe_load(f)

def main():
    # Print the contents of the config.yaml file
    print("Contents of config.yaml:")
    print(yaml.dump(config))

    # Print the contents of the config.yaml file
    print("Contents of azurekey.yaml:")
    print(yaml.dump(azurekey))

    # Print the value of the AZURE_API_KEY environment variable
    azure_api_key = os.getenv("AZURE_API_KEY")
    print(f"\nThe value of AZURE_API_KEY is: {azure_api_key}")

    return config

if __name__ == "__main__":
    main()
