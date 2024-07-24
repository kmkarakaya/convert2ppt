import google.generativeai as genai
import os
import json

def generate_json(data_dir):
    gemini_api_key = os.getenv('GEMINI_API_KEY')

    docs = [doc for doc in os.listdir(data_dir) if doc.endswith('.txt')]
    
    prompts = []
    for doc in docs:
        with open(os.path.join(data_dir, doc), 'r', encoding='utf-8') as file:
            text = file.read()
            prompts.append(text)

    system_prompt = """<Your system prompt here>"""  # Keep your prompt here

    genai.configure(api_key=gemini_api_key)

    from google.generativeai.types import HarmCategory, HarmBlockThreshold
    
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        system_instruction=system_prompt,
        generation_config={"response_mime_type": "application/json"},
        safety_settings=safety_settings
    )

    for i, prompt in enumerate(prompts):
        print(f"Attempting to generate content for: {docs[i]}")  # Log the document being processed

        for attempt in range(3):
            try:
                response = model.generate_content(prompt)

                if hasattr(response, 'candidates') and response.candidates:
                    first_candidate = response.candidates[0]
                    text = first_candidate.text if hasattr(first_candidate, 'text') else None
                    safety_ratings = getattr(first_candidate, 'safety_ratings', None)

                    if safety_ratings:
                        print("The response was blocked due to safety concerns.")
                        print(f"Safety Ratings: {safety_ratings}")
                        print(response.prompt_feedback)
                        break
                    
                    if text:
                        break
                    else:
                        print("No valid text found in the response candidate.")
                else:
                    print("No candidates returned in the response.")
                    break

            except Exception as e:
                print(f"An error occurred while generating content: {str(e)}")
                continue

        if text:
            try:
                json_data = json.loads(text)
                filename = docs[i].replace('.txt', '.json')
                full_path = os.path.join(data_dir, filename)
                with open(full_path, 'w') as file:
                    json.dump(json_data, file)
                print(f"JSON for {docs[i]} saved to {filename}")
            except json.JSONDecodeError:
                print(f"Failed to parse JSON for {docs[i]}.")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
        else:
            print(f"No text generated for {docs[i]}, skipping JSON conversion.")