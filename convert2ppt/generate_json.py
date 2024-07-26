
import os
import json
from convert2ppt import connect_gemini

def attempt_generating_json(model, prompt):
    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            json_data = json.loads(response.text)
            # If the JSON data is loaded successfully, break the loop
            break
        except json.JSONDecodeError:
            # If loading the JSON data fails and this is not the last attempt, try again
            if attempt < 2:
                print(f"\t\tAttempt {attempt + 1} to generate valid JSON failed. Trying again...")
            else:
                print(f"\t\tAll attempts to generate valid JSON failed. Skipping this document.")
                json_data = None
    return json_data

def generate_json(data_dir):
    
    model=connect_gemini()
    docs = [doc for doc in os.listdir(data_dir) if doc.endswith('.txt')]
    
    prompts = []
    for doc in docs:
        with open(os.path.join(data_dir, doc), 'r', encoding='utf-8') as file:
            text = file.read()
            prompts.append(text)

    print(f"\nContent generations started for {len(docs)} documents.")  
    print(f"Please wait while the LLM model generates the content...")

    for i, prompt in enumerate(prompts):
       
        print(f"\tAttempting to generate content in a JSON format for: {docs[i].replace('.txt', '')}")  
        json_data = attempt_generating_json(model, prompt)
        if json_data is None:
            print(f"\tFailed to generate a valid JSON for {docs[i]}. Skipping this document.")
            continue
        filename = docs[i].replace('.txt', '.json')
        full_path = os.path.join(data_dir, filename)
        with open(full_path, 'w') as file:
            json.dump(json_data, file)
        print(f"\tSuccessfully generated a valid JSON & saved to {filename}")
    print("All content generations completed successfully.")
