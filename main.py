import os

# Get the AZURE_API_KEY environment variable
azure_api_key = os.getenv("AZURE_API_KEY")

def main():
    print(f"The value of AZURE_API_KEY is: {azure_api_key}")
    return azure_api_key

if __name__ == "__main__":
    main()
