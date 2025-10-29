import os
from dotenv import load_dotenv
# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI


def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        api_key =  os.getenv("API_KEY")
        api_version = os.getenv("API_VERSION")
        api_model = os.getenv("PROJECT_MODEL")

        # Initialize the project client
        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=project_endpoint,
            api_key=api_key,
        )

        # Initialize prompt with system message
        prompt = [
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ] 

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            response = client.chat.completions.create(
                model= api_model,
                messages=prompt,
                max_tokens=4096,
                temperature=1.0,
                top_p=1.0
                )
            completion = response.choices[0].message.content
            print(completion)
            prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()